# Encoder settings for Premiere



---



---



---

which encoder and settings for going to  premier

---



---



---

Excellent — you’re configuring OBS for a **Premiere Pro workflow**, which is smart because the encoder and container format matter a lot for smooth editing and minimal re-encoding.  

Let’s look at your current settings and then I’ll show the optimal configuration for **Premiere** on macOS.

---

### 🔍 What You Have
- **Recording Format:** Fragmented MOV (.mov)  
- **Video Encoder:** Apple VT H264 Software Encoder  
- **Audio Encoder:** CoreAudio AAC  
- **Audio Track:** 1  
- **Rescale Output:** Disabled  
- **Output Mode:** Advanced  
- **Container:** MOV (fragmented)

This will *work* — Premiere can read `.mov` just fine — but “Fragmented MOV” can occasionally cause playback lag or red frames during import because Premiere sometimes prefers complete moov atoms at the start of a file (non-fragmented). The difference is subtle: fragmented MOV is better for streaming, not editing.

---

### ✅ Recommended Settings for Smooth Editing in Premiere

**Recording Format:**  
- Use **MOV** or **MP4** (non-fragmented).  
  - `MOV` keeps timecode and metadata better.  
  - `MP4` has smaller file headers and is widely supported.  
  - Avoid “Fragmented” for editing.

**Video Encoder (macOS):**
- If you have an Apple Silicon Mac (M1/M2/M3):  
  → **Apple VT H.264 Hardware Encoder** (or **H.265/HEVC** if you want higher efficiency).  
  This uses the chip’s hardware acceleration, freeing CPU load and giving faster real-time encoding.

- If you’re on an Intel Mac:  
  → **Apple VT H.264 Software Encoder** is fine, but you can try **x264** (OBS’s software encoder) if you want more bitrate control and constant quality at the cost of CPU.

**Key OBS setting for Premiere compatibility:**  
- **Profile:** *High*  
- **Level:** *4.2* (for 1080p60)  
- **Bitrate:** 20,000–50,000 kbps for high-quality 1080p editing footage  
- **Color Range:** Full  
- **Color Space:** Rec. 709 (Premiere’s default)

You’ll find these in:
`Settings → Output → Recording → Encoder Settings (gear icon)`  
and also under  
`Settings → Video → Color Format`.

**Audio Encoder:**  
- **CoreAudio AAC** (keep it).  
- Bitrate: 320 kbps stereo.  
- Sample rate: 48 kHz (matches Premiere’s project default).

**File Path and Naming:**  
- Keep your current path fine: `/Users/garygreen/Video_Projects/OBS_feeds`  
- You can enable “Generate File Name without Space” if your Premiere imports sometimes choke on spaces.

---

### ⚙️ Optional: Master Quality Workflow
If you need pristine, edit-friendly master files (for color grading or heavy VFX):
- Recording Format: **MOV**
- Video Encoder: **ProRes 422 HQ** (only available via plugins or OBS builds with Apple ProRes)
- Bitrate: automatic; large files, but zero generation loss.
Premiere loves ProRes.

---

### Summary Table

| Setting | Recommended for Premiere |
|----------|--------------------------|
| Recording Format | MOV (non-fragmented) |
| Encoder | Apple VT H.264 Hardware |
| Profile | High |
| Level | 4.2 |
| Bitrate | 20–50 Mbps (CBR or VBR) |
| Audio | CoreAudio AAC, 48 kHz, 320 kbps |
| Color Space | Rec. 709, Full Range |
| Container | MOV |
| Split Files | Off (Premiere reads long files fine) |

---

Switch those and click **Apply → OK**, then test-record a 30-second clip and drop it into Premiere. You’ll see faster imports, no red frames, and smoother playback on the timeline.

---

I have mac studio2'

---

Perfect — that’s a **Mac Studio M2 (Max or Ultra)**, right? That’s great news because those chips have **dedicated ProRes and H.264/H.265 (HEVC) hardware encoders** built right into the silicon. You can lean on that for *broadcast-quality* recordings that Premiere reads natively and edits like butter.  

Here’s the setup that will give you pristine, low-latency, zero-conversion footage straight into Premiere:

---

### 🎥 **Best OBS Recording Settings for Premiere on Mac Studio (M2 Max/Ultra)**

**1. Recording Format**  
→ `MOV` (not *Fragmented MOV*)  
Reason: the non-fragmented `.mov` keeps timecode and metadata clean, and Premiere’s QuickTime importer is tuned for it.  

**2. Video Encoder**  
→ `Apple VT H.264 Hardware Encoder` **or** `Apple VT HEVC (H.265) Hardware Encoder`  
- **Use H.264** if you’ll share files widely or edit on mixed systems.  
- **Use HEVC (H.265)** if you’re staying on Apple hardware and want smaller file sizes with the same quality.  
- Both use the M2’s hardware encoder—zero CPU strain.

**3. Encoder Profile (gear icon beside the encoder name)**  
- Profile: `High`  
- Level: `4.2` (for 1080p60) or `5.1` (for 4K60)  
- Rate Control: `CBR` (constant bitrate) or `VBR` with a high minimum.  
- Bitrate:  
  - 1080p → 25,000–50,000 kbps  
  - 4K → 80,000–120,000 kbps  

**4. Audio Encoder**  
→ `CoreAudio AAC`  
- Bitrate: 320 kbps  
- Sample Rate: 48 kHz (matches Premiere’s default project setting)  

**5. Color Settings**  
`Settings → Video → Advanced`:  
- Color Format: `NV12` or `P010` (if using HDR/10-bit)  
- Color Space: `Rec. 709`  
- Color Range: `Full`  

**6. Optional: ProRes Recording (Master Workflow)**  
If you need editing masters or plan color-grading in DaVinci/Premiere:  
- Install **OBS Apple ProRes plug-in** (free, GitHub project: *obs-ffmpeg-prores*).  
- Then choose `ProRes 422 LT` (smaller files) or `422 HQ` (master quality).  
Premiere handles ProRes natively, and the M2 chip encodes it in hardware.

**7. Storage Path**  
→ Keep your path `/Users/garygreen/Video_Projects/OBS feeds` — just ensure that drive is **APFS or HFS+**, not FAT/exFAT, so it supports large files.

---

### ⚡ TL;DR Configuration Snapshot
| Setting | Recommended |
|----------|--------------|
| **Format** | MOV |
| **Encoder** | Apple VT H.264 Hardware Encoder |
| **Bitrate** | 25–50 Mbps (1080p) / 80–120 Mbps (4K) |
| **Profile/Level** | High @ 4.2 (1080p) |
| **Audio** | CoreAudio AAC 48 kHz 320 kbps |
| **Color Space** | Rec. 709 Full |
| **Container** | MOV (non-fragmented) |

---

Once you apply these, Premiere will read your OBS clips instantly—no “Conforming” delay, no red-frame glitches, and playback will stay real-time even at full-resolution preview.

---

Can I lose entire recordings if I don't do a fragmented? Like, depending on how I stop or try to pause or if it corrupts or something.

---

Excellent and very practical question — you’re thinking like a producer *and* an engineer.  

Here’s the deal in plain language:

---

### 🧩 What “Fragmented MOV” Actually Does  
A **fragmented MOV (fMP4)** writes your recording in *chunks* while you’re capturing. That means if OBS or your computer crashes mid-recording, the file is *still playable up to the crash point*. It’s like saving every few seconds instead of only at the end.  

By contrast, a **normal MOV or MP4** writes all the media first, *then* finalizes the file header (the “moov atom”) when you stop recording. If that stop command never completes — power outage, system freeze, OBS crash — the header never gets written, and the file is unreadable until it’s repaired.  

---

### ⚠️ So yes — with non-fragmented MOV or MP4:
- If OBS closes *normally* → File is perfect.  
- If OBS crashes or you force-quit → File might be unreadable.  
- You can often **repair it** using ffmpeg (`ffmpeg -i broken.mov -c copy fixed.mov`) or QuickTime’s rebuild trick, but it’s not guaranteed.  

With **fragmented MOV**, crashes rarely cost you the whole file. Premiere or VLC will just open what was written before the crash.

---

### 💡 Practical Workflow Advice  
If you’re doing **long takes** (over 30 minutes) or **live streams** where you can’t redo a take:
- Keep **Fragmented MOV** *on* for safety.  
- Then, when finished, **transcode** the final files into standard MOVs before importing to Premiere. That’s a quick rewrap—no re-encoding needed. Command line example:  
  ```bash
  ffmpeg -i input.mov -c copy output.mov
  ```
  That just merges the fragments into a single continuous container.

If you’re doing **short, repeatable studio takes** (like A-roll, interviews, pickups), you can confidently record to **non-fragmented MOV** for direct Premiere editing. Just make sure you always hit **Stop** cleanly before closing OBS.

---

### ⚖️ In short
| Situation | Safer Choice | Premiere-Ready Choice |
|------------|---------------|------------------------|
| Long live takes / risk of crash | Fragmented MOV | (then rewrap) |
| Short, controlled sessions | Non-fragmented MOV | ✅ Import directly |
| Need absolute editing stability | ProRes MOV | ✅ Native + robust |

---

So, you won’t *automatically* lose recordings if you use normal MOV — but you *could* if something crashes before OBS finishes writing the file header. Fragmented is your insurance; non-fragmented is your editing convenience. You just pick which risk to minimize.