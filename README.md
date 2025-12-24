# Video Generation CLI

A small CLI wrapper around the OpenAI video API that takes prompts (single or batch) and saves the resulting MP4s. Progress is printed while polling, and downloads are attempted via SDK helper, public URL, and a direct content fallback.

## Prerequisites
- Python 3.10+ and `pip`
- Dependencies: `openai`, `python-dotenv` (install in your venv: `python -m pip install openai python-dotenv`)
- `.env` at the repo root (`/Users/garygreen/Code/Israel in Egypt/.env`) with `OPENAI_API_KEY=<your key>`; the script prints the key prefix it is using.

## Entry Points
- From repo root: `./run_video.sh ...`
- From inside `video creation/`: `./run_video.sh ...`
- Via the installed launcher: `israel-video ...` (points to the same script)
- Direct Python: `python "video creation/video_generation.py" ...`

## CLI Usage
```
./run_video.sh --prompt "a description" \
               --size 1280x720 \
               --seconds 4 \
               --outdir "/Users/garygreen/Code/Israel in Egypt/videos" \
               --concurrency 1
```

Flags:
- `--prompt` / `-p`: single prompt string.
- `--prompt-file` / `-f`: path to a newline file or JSONL with a `prompt` field per line.
- `--size`: resolution, e.g., `1280x720` or `1792x1024`.
- `--seconds`: `4`, `8`, or `12`.
- `--concurrency`: number of parallel jobs; beware of rate limits.
- `--outdir`: optional. Defaults to `/Users/garygreen/Code/Israel in Egypt/videos` if omitted or set to `videos`.

## Examples
- Single prompt:
  ```
  israel-video --prompt "misty desert sunrise, cinematic" --seconds 4 --size 1280x720
  ```
- Batch from JSONL:
  ```
  israel-video --prompt-file "/Users/garygreen/Code/Israel in Egypt/video creation/prompts/edomtojudean.jsonl" \
               --seconds 12 --size 1792x1024 --concurrency 2
  ```

## Behavior Notes
- The script prints which `.env` it loaded and the API key prefix; if you see a short prefix (26 chars), clear any exported `OPENAI_API_KEY` (`unset OPENAI_API_KEY`) so the `.env` value is used.
- Output videos default to the repo `videos/` directory; a custom `--outdir` is honored.
- Progress/status is printed every few seconds while polling; Ctrl+C cancels.
- Download attempts: SDK helper, then public URL, then direct content endpoint. Expired URLs will 404; rerun the job to regenerate if that happens.
