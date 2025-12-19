from __future__ import annotations

import os
import sys
import urllib.request
from dotenv import load_dotenv

import argparse
import json
from pathlib import Path
from typing import Any
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed


def _extract_url(response: Any) -> str | None:
    """Try common shapes for a URL in the video response."""
    # handle object attributes, dict shapes, and lists
    if response is None:
        return None
    if isinstance(response, dict):
        # common shape: {"data":[{"url":"..."}]}
        data = response.get("data")
        if isinstance(data, list) and data:
            return data[0].get("url")
        return response.get("url")
    # object-like
    if hasattr(response, "url"):
        return getattr(response, "url") or None
    data = getattr(response, "data", None)
    if isinstance(data, list) and data:
        first = data[0]
        if isinstance(first, dict):
            return first.get("url")
        return getattr(first, "url", None)
    return None


def _generate_video(client: Any, **kwargs: Any) -> Any:
    """Handle different SDK method names for video generation."""
    # support both 'openai.OpenAI' with client.videos.generate and older client.videos.create
    videos = getattr(client, "videos", None)
    if videos is None:
        raise SystemExit("Client has no 'videos' attribute — check installed OpenAI SDK.")
    if hasattr(videos, "generate"):
        return videos.generate(**kwargs)
    if hasattr(videos, "create"):
        alt_kwargs = kwargs.copy()
        if "duration" in alt_kwargs and "seconds" not in alt_kwargs:
            # API expects string values like "4", "8", "12" for seconds
            alt_kwargs["seconds"] = str(alt_kwargs.pop("duration"))
        return videos.create(**alt_kwargs)
    raise SystemExit("Installed openai package has no video generation support. Upgrade openai.")


def _as_dict(obj: Any) -> dict:
    """Normalize response to a dict for simple status/url checks."""
    if obj is None:
        return {}
    if isinstance(obj, dict):
        return obj
    # try dataclass/SDK object that exposes __dict__ or attributes
    try:
        return {k: getattr(obj, k) for k in dir(obj) if not k.startswith("_") and not callable(getattr(obj, k))}
    except Exception:
        return {"raw": obj}


def _retrieve_video(client: Any, video_id: str) -> Any:
    """Try common retrieval method names to get updated video status."""
    videos = getattr(client, "videos", client)
    for name in ("get", "retrieve", "get_video", "fetch"):
        fn = getattr(videos, name, None)
        if not fn:
            continue
        # try common calling conventions
        for kwargs in ({"id": video_id}, {"video_id": video_id}, {"videoId": video_id}, {}):
            try:
                if kwargs:
                    return fn(**kwargs)
                return fn(video_id)
            except TypeError:
                # try different signature next
                continue
            except Exception:
                # propagate real errors (auth/other)
                raise
    raise SystemExit("Unable to retrieve video status: no compatible SDK method found.")


def _wait_for_completion(client: Any, video_id: str, timeout: int = 600, interval: int = 5) -> Any:
    """Poll until the video status is terminal or timeout reached."""
    import time

    deadline = time.time() + timeout
    last_progress = None
    print(f"Polling video {video_id} for completion (timeout {timeout}s)...", flush=True)
    while time.time() < deadline:
        resp = _retrieve_video(client, video_id)
        d = _as_dict(resp)
        status = d.get("status") or d.get("state") or ""
        progress = d.get("progress")
        if progress is None:
            # try to infer progress from nested structures
            try:
                progress = int(getattr(resp, "progress", 0))
            except Exception:
                progress = None
        if progress is not None and progress != last_progress:
            print(f"progress: {progress}%, status: {status}", flush=True)
            last_progress = progress
        else:
            print(f"status: {status}", flush=True)
        url = _extract_url(resp)
        if url:
            return resp
        if status and status.lower() in ("succeeded", "completed", "failed", "error"):
            return resp
        time.sleep(interval)
    raise SystemExit("Timed out waiting for video to complete.")


def _save_bytes(data: bytes, out_dir: str, vid: str) -> str:
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_name = f"{vid}_{timestamp}.mp4"
    out_path = Path(out_dir) / out_name
    with open(out_path, "wb") as f:
        f.write(data)
    return str(out_path)


def _download_via_sdk(videos_obj: Any, video_id: str, out_dir: str) -> str | None:
    """Try the SDK download_content helper and return saved file path or None."""
    downloader = getattr(videos_obj, "download_content", None)
    if not downloader:
        return None
    try:
        resp = downloader(video_id=video_id, variant="video")
        # resp may be a binary stream-like or have .content
        data = None
        if hasattr(resp, "read"):
            data = resp.read()
        elif hasattr(resp, "content"):
            data = getattr(resp, "content")
        elif isinstance(resp, (bytes, bytearray)):
            data = bytes(resp)
        if data:
            return _save_bytes(data, out_dir, video_id)
    except Exception:
        # swallow and fallback
        return None
    return None


def _download_via_url(url: str, out_dir: str, api_key: str | None = None) -> str | None:
    """Download a video from a URL. If URL requires auth, try Authorization header with api_key."""
    try:
        req = urllib.request.Request(url)
        if api_key:
            req.add_header("Authorization", f"Bearer {api_key}")
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
            if data:
                # derive id-ish name from URL
                vid = url.split("/")[-1].split("?")[0][:40]
                return _save_bytes(data, out_dir, vid)
    except Exception:
        return None
    return None


def _init_client_from_env() -> Any:
    """Load .env (search upward from this file), verify OPENAI_API_KEY, and return an OpenAI client."""
    # search upwards from the directory that contains this file for a .env file
    start = Path(__file__).resolve()
    env_path = None
    for p in (start.parent, *start.parents):
        candidate = p / ".env"
        if candidate.exists():
            env_path = candidate
            break
    # fallback to cwd/.env if none found above
    if env_path is None:
        candidate = Path.cwd() / ".env"
        if candidate.exists():
            env_path = candidate
    # load if found, otherwise let load_dotenv use defaults (env vars)
    load_dotenv(dotenv_path=env_path if env_path and env_path.exists() else None)
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if env_path:
        print(f"Loaded .env from: {env_path}", flush=True)
    # debug helper: show which key prefix is in use (masked)
    if api_key:
        print(f"Using OPENAI_API_KEY prefix: {api_key[:8]}... (len={len(api_key)})", flush=True)
    else:
        raise SystemExit(f"OPENAI_API_KEY not set. Add it to .env (searched up from {start}) or export it in your shell.")
    try:
        from openai import OpenAI  # type: ignore
    except Exception:
        import openai as openai_legacy  # type: ignore
        openai_legacy.api_key = api_key
        return openai_legacy
    return OpenAI(api_key=api_key)


def generate_for_prompt(prompt: str, out_dir: str, seconds: str = "4", size: str = "1280x720") -> dict:
    """
    Full flow for a single prompt:
      - init client
      - create (or create_and_poll) video job
      - poll/await completion
      - attempt to download via SDK, public URL, or direct content endpoint
    Returns metadata dict with id, saved path (or None), and response object.
    """
    # verify helper presence
    required = ["_generate_video", "_wait_for_completion", "_download_via_sdk", "_download_via_url", "_save_bytes", "_extract_url"]
    for name in required:
        if name not in globals() or not callable(globals()[name]):
            raise SystemExit(f"Required helper '{name}' not found or not callable in this file. Add/restore it before using generate_for_prompt.")

    client = _init_client_from_env()
    videos = getattr(client, "videos", client)

    print("Generating:", prompt)
    resp = None
    vid = None

    # Always create then poll ourselves so we can show status updates
    try:
        resp = _generate_video(client, model="sora-2-pro", prompt=prompt, size=size, duration=seconds)
        vid = getattr(resp, "id", None) or (resp.get("id") if isinstance(resp, dict) else None)
        if vid:
            resp = _wait_for_completion(client, vid, timeout=1800, interval=5)
    except Exception as e:
        return {"prompt": prompt, "error": f"creation/poll failed: {e}", "id": None, "saved": None, "response": None}

    # find id and URL
    vid = getattr(resp, "id", None) or (resp.get("id") if isinstance(resp, dict) else None)
    public_url = _extract_url(resp)

    saved = None
    # 1) try SDK helper
    try:
        saved = _download_via_sdk(videos, vid, out_dir) if vid else None
    except Exception as e:
        print("SDK download attempt raised:", e)

    # 2) try public URL
    if not saved and public_url:
        try:
            saved = _download_via_url(public_url, out_dir, api_key=os.environ.get("OPENAI_API_KEY"))
        except Exception as e:
            print("URL download attempt raised:", e)

    # 3) final fallback: direct content endpoint using same key
    if not saved and vid:
        try:
            url = f"https://api.openai.com/v1/videos/{vid}/content?variant=video"
            req = urllib.request.Request(url)
            req.add_header("Authorization", f"Bearer {os.environ.get('OPENAI_API_KEY')}")
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            if data:
                saved = _save_bytes(data, out_dir, vid)
        except Exception as e:
            print("Direct content download failed:", e)

    return {"prompt": prompt, "id": vid, "saved": saved, "response": resp}


def _read_prompts_from_file(path: str) -> list[str]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)
    if p.suffix.lower() in (".jsonl",):
        out = []
        with p.open() as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    obj = json.loads(line)
                    if isinstance(obj, dict) and "prompt" in obj:
                        out.append(obj["prompt"])
                except Exception:
                    continue
        return out
    # default: newline-separated prompts
    return [l.strip() for l in p.read_text().splitlines() if l.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate videos from prompts and auto-download.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--prompt", "-p", help="Single prompt string.")
    group.add_argument("--prompt-file", "-f", help="File with prompts (newline or JSONL with 'prompt' field).")
    parser.add_argument("--size", default="1280x720", help="Video size (e.g. 1280x720 or 1792x1024).")
    parser.add_argument("--seconds", default="4", choices=["4","8","12"], help="Duration seconds string (4/8/12).")
    parser.add_argument("--outdir", default="videos", help="Directory to save videos.")
    parser.add_argument("--concurrency", type=int, default=1, help="Number of parallel generation threads.")
    args = parser.parse_args()

    out_dir = args.outdir
    Path(out_dir).mkdir(parents=True, exist_ok=True)

    if args.prompt:
        prompts = [args.prompt]
    else:
        prompts = _read_prompts_from_file(args.prompt_file)

    results = []
    if args.concurrency > 1:
        with ThreadPoolExecutor(max_workers=args.concurrency) as ex:
            futures = {ex.submit(generate_for_prompt, p, out_dir, seconds=args.seconds, size=args.size): p for p in prompts}
            for fut in as_completed(futures):
                try:
                    results.append(fut.result())
                except Exception as e:
                    results.append({"prompt": futures[fut], "error": str(e)})
    else:
        for p in prompts:
            try:
                results.append(generate_for_prompt(p, out_dir, seconds=args.seconds, size=args.size))
            except Exception as e:
                results.append({"prompt": p, "error": str(e)})

    print("SUMMARY:")
    print(json.dumps(results, default=str, indent=2))


if __name__ == "__main__":
    main()
