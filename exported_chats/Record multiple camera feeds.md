# Record multiple camera feeds



---



---

Is it possible to record two feeds simultaneously of video in OBS without doing a split-screen thing? I want to record two different cameras, camera angles, without switching so that I can edit those later. So, I'm looking for a program or a way to record those two feeds.

---



---

Yes, you **can record two video feeds simultaneously in OBS Studio**, but **not by default in separate files**. OBS typically only outputs a single video file at a time. However, you have **a few powerful options** for capturing **multiple camera angles independently** for post-production editing:

---

### ✅ **Option 1: OBS + Multiple Scene Recordings (with plugin)**
Use the **[Source Record](https://obsproject.com/forum/resources/source-record.1285/)** plugin. This lets you **record individual camera sources** to separate files — even if you're streaming or recording something else in the main canvas.

#### 🔧 Setup with Source Record plugin:
1. **Install the Source Record plugin**:
   - Download from: [https://obsproject.com/forum/resources/source-record.1285/](https://obsproject.com/forum/resources/source-record.1285/)
   - Follow install instructions for your OS.

2. **Add both cameras as sources** in your scene.

3. **Right-click each camera source > Filters > + > Source Record**.

4. In each filter, configure:
   - **Custom Output Path** (where that camera feed will be saved)
   - Set encoder, resolution, format independently
   - Optionally set **record-only**, even while streaming

5. Start recording as usual — **each camera records to its own file**.

---

### ✅ **Option 2: Use Two Instances of OBS (Advanced)**
OBS can run in **multiple instances** with separate configs. This lets you open a second OBS window and record a second camera.

#### Setup:
1. **Duplicate your OBS shortcut**.
2. Add `--multi` to the target path:
   ```
   "/Applications/OBS.app/Contents/MacOS/OBS" --multi
   ```
   (on Mac — modify for Windows accordingly)

3. In each OBS instance:
   - Add only one camera source
   - Set different output file paths
   - Start recording

⚠️ This is **resource-intensive**, but viable on Mac Studio.

---

### ✅ **Option 3: Use OBS + Other Software (like QuickTime or Ecamm)**
If you're on macOS, use **OBS to record one camera**, and use **QuickTime Player** or **Ecamm Live** to record the other camera at the same time.

---

### ✅ **Option 4: Use Blackmagic ATEM Mini (Hardware Switcher)**
If you're going hardware: a device like the **ATEM Mini Pro ISO** can:
- Record **up to 4 cameras** via HDMI
- Save each input as **individual ISO (isolated) video files**
- Saves a DaVinci Resolve timeline for multi-cam editing

---

### ✅ Best Practices for Editing Later:
Once you have both camera angles:
- Import both into **Premiere Pro**
- Use **Multi-Camera Sequence**
- Sync by audio or timecode
- Cut easily between angles during edit

---

Would you like a script to automatically create folders and manage recordings for each camera input using the Source Record plugin or OBS instance automation?

---



---

You're looking at the right installer options for the **Source Record plugin** on macOS.

Since you're using a **Mac Studio**, it almost certainly runs on **Apple Silicon (M1/M2/M3)** — which means your chip architecture is **ARM64**.

---

### ✅ Choose This One:
**`source-record-0.4.6-macos-arm64.pkg`**

This version is **optimized for Apple Silicon** and will give you the best performance and compatibility with OBS running natively on your Mac Studio.

---

### Optional Notes:
- `universal.pkg` includes both Intel and ARM binaries — larger file size, same result but slightly less efficient.
- `x86_64.pkg` is **Intel-only** — don't use this on Apple Silicon unless you're running OBS under Rosetta (which you shouldn't).

---

Once installed:
1. Restart OBS.
2. Right-click a **video source** (like your camera) in your scene.
3. Go to **Filters** → click the `+` → choose **Source Record**.
4. Configure output path, resolution, encoder, etc.

Let me know if you want a default config template or a folder structure automation for recordings.

---



---

That error message is from **macOS Gatekeeper**, which blocks apps and installers that aren't signed by an **Apple-verified developer** — even if they're perfectly safe.

Since the **Source Record plugin** is open-source and not signed, you’ll need to **manually allow the installer**.

---

### ✅ To fix: Use “Right-Click > Open” (once)

1. **Right-click** on `source-record-0.4.6-macos-arm64.pkg`.
2. Select **Open**.
3. You’ll see a similar warning, but this time **you’ll get the option to proceed**.
4. Click **Open** again to continue installing.

---

### 🛡️ Alternative (System Settings method):
If that doesn’t work, try this:

1. Open **System Settings > Privacy & Security**.
2. Scroll down to **Security** section.
3. You should see a message like:  
   > "**source-record-0.4.6-macos-arm64.pkg** was blocked..."
4. Click **Allow Anyway**.
5. Then go back and double-click the `.pkg` again to install.

---

Let me know once installed — I can help you build your dual camera Source Record setup from scratch, including file-naming, folder structure, and audio sync tips.

---

do i need to restart to see the source record?

---

Yes — after installing the **Source Record plugin**, you **must restart OBS Studio** for it to appear.

---

### ✅ Steps:
1. **Quit OBS Studio completely.**
   - Use `Cmd + Q`, or right-click the dock icon and choose **Quit**.
   - (Do *not* just close the window — the plugin won’t load until a full restart.)

2. **Reopen OBS Studio.**

3. Right-click on your camera source (or any video input), go to:
   ```
   Filters → + → Source Record
   ```

4. You’ll now see a **new "Source Record" filter** you can add to that source.
   - Configure **file path**, **encoder**, resolution, etc.

---

### 🧠 Tip:
You can add the Source Record filter to **each camera individually**, and OBS will record them each to **separate files** — even if they’re not visible in the main scene.

Let me know if you'd like:
- A sample folder layout
- Pre-set output paths
- OBS auto-record script or hotkey config

---

I want to add to the name that is from the iPhone, so I just want to add iPhone to this one, and then FX3 to the other.

---

Perfect — you’re almost there.

To customize the filename for each camera feed, simply **append your custom label** (like `iPhone` or `FX3`) directly in the **Filename Formatting** field.

---

### ✅ For iPhone feed:
Change:
```bash
%CCYY-%MM-%DD %hh-%mm-%ss
```
To:
```bash
iPhone-%CCYY-%MM-%DD_%hh-%mm-%ss
```

### ✅ For FX3 feed:
Use:
```bash
FX3-%CCYY-%MM-%DD_%hh-%mm-%ss
```

> ✅ You can use underscores instead of spaces (`_`) if you want to avoid file path issues or improve compatibility with editing apps.

---

### 🔁 Resulting files:
These will generate files like:
```
iPhone-2025-09-01_10h-15m-22s.mov
FX3-2025-09-01_10h-15m-22s.mov
```

This makes syncing super clean in **Premiere Pro**, **Final Cut**, or **DaVinci Resolve**.

Let me know if you'd like:
- A shell script or AppleScript to organize the files into folders after recording
- OBS auto-start recording setup when you open the app
- Audio sync tips for multi-cam edits

---

And how do I view both feeds in OBS?

---

To **view both camera feeds in OBS at the same time** (without switching or hiding one), you simply need to add **both camera sources into your current scene** and arrange them however you like.

Here’s how to **view both feeds side-by-side or layered**:

---

### ✅ STEP 1: Add Both Video Sources
1. In your **Scene**, click the `+` under **Sources**.
2. Choose **Video Capture Device**.
3. Name it something like **iPhone Camera**, click OK.
4. In the **Device** dropdown, select your iPhone feed (e.g., via Continuity Camera, EpocCam, or NDI).
5. Repeat steps 1–4 for the **FX3**:
   - Name it **FX3 Camera**.
   - Choose the **FX3 via CamLink** or HDMI capture device.

---

### ✅ STEP 2: Arrange Both Feeds Visually
Once both are added, you’ll see them in the **preview canvas**:
- You can **resize and drag** them.
- You can stack one over the other, or place them **side-by-side** like this:

```
+--------------------------+
|     iPhone     |   FX3   |
+--------------------------+
```

💡 If you want to **hide** one feed from the final output but **still record it**, just **scale it off-canvas** or set its **visibility off** (👁️ icon), and let the **Source Record filter** record it anyway.

---

### ✅ STEP 3: Confirm Both Are Recording
- Open each camera **source** (right-click > Filters).
- Verify **Source Record filter** is active on both.
- Each camera will now save **its own separate video file** to your custom paths.

---

### 🎯 Optional: Create a Multi-View Monitoring Layout
- Go to **View > Multiview > Fullscreen Multiview**.
- Assign each camera to a slot in **Multiview** (OBS will show preview and program).
- This is handy for live switching or monitoring during interviews.

---

Let me know if you’d like a **custom layout preset** or want to build a **scene that auto-adjusts resolution and positioning for split-view recording**.

---

Okay, so I got my footage into Premiere. I have both feeds, but how do I look at both A-Roll and B-Roll at the same time so I can decide where I want to splice things in? Is there a way for me to be like have a window where they both play at the same time in Premiere Pro?

---



---

Yes — **Premiere Pro absolutely lets you view both A-Roll and B-Roll at the same time** using a few powerful options. Here are your best workflows depending on what you're trying to do:

---

## ✅ Option 1: **Use the Multi-Camera Source Sequence (Recommended for Interviews, Dialogue, Podcasts)**

This is the **cleanest way** to view and switch between multiple camera feeds *live* in a split window (just like a live director).

### 🎬 Setup:
1. **Import both clips** (A-Roll and B-Roll).
2. **Select both clips** in the Project panel (Cmd/Ctrl + Click).
3. Right-click and choose:  
   **➡ Create Multi-Camera Source Sequence**
4. Use **Audio** as the synchronization method (if they share audio).
5. Name the sequence and click OK.

### 📺 Use Multi-Camera Monitor:
1. Right-click the resulting multicam clip →  
   **➡ Open in Timeline**
2. Go to **Window > Multi-Camera Monitor**.
3. In the **Program Monitor**, click the wrench (🔧) icon →  
   **➡ Enable Multi-Camera**

Now you’ll see **side-by-side previews** (Cam 1 = A-Roll, Cam 2 = B-Roll), and you can **click to switch angles** while watching in real time. Premiere will automatically add cuts on the timeline.

> 🎯 This is ideal for podcast-style edits or anything with alternating speaker views.

---

## ✅ Option 2: **Stack Both Clips in Timeline + Use Toggle Track Visibility**

If you don’t want to use multicam and just want to **see them side-by-side or switch back and forth manually**, do this:

### 🎬 Setup:
1. Place **A-Roll on Video Track 1**, B-Roll on **Video Track 2**.
2. Resize them in the **Program Monitor**:
   - Select a clip → **Effect Controls > Scale / Position**
   - Set up a side-by-side (e.g., Scale 50, Position left/right)

### Optional: Use `Toggle Track Output (👁️)` to turn one on/off to check footage quickly.

---

## ✅ Option 3: **Use Reference Monitor (Advanced)**

1. Go to **Window > Reference Monitor**.
2. This opens a second monitor panel that can show:
   - The source clip
   - The timeline (Program monitor)
   - Waveform comparisons

Not as intuitive as multicam, but good for **precision visual comparisons**.

---

## Bonus Tips:
- You can use **labels** (right-click a clip > Label > "A-Roll"/"B-Roll") to stay organized.
- Use **markers** (`M` key) to tag important cut/splice points across both tracks.
- Use **nesting** if you need to treat a set of clips as one block.

---

Would you like a preset template for dual-cam podcast editing in Premiere? Or a custom multi-cam sequence builder with naming conventions (`FX3`, `iPhone`, etc.)?

---



---

Great — you're on the right screen! This is the **Multi-Camera Source Sequence setup** in Premiere Pro. Here's how to optimize this for your **A-Roll (FX3)** and **B-Roll (iPhone)** feeds:

---

### ✅ Key Settings to Adjust:

#### **1. Synchronize Point → Use "Audio"**
- Select **“Audio”** (scroll down if needed) instead of “Timecode” unless you recorded timecode into both files.
- This is the easiest and most reliable sync method when both feeds have the same ambient or mic input.

> 🔊 Premiere will analyze and sync the clips based on their waveforms.

---

#### **2. Sequence Name**
- At the top, change the default name from “Multicam” to something like:
  ```
  FX3_iPhone_Multicam
  ```

---

#### **3. Audio Settings**
- Under **Audio > Sequence Settings**, choose:
  - ✅ **“Camera 1”** if FX3 has the cleanest/primary audio
  - Or choose **“All Cameras”** if you want to keep both tracks active for editing

---

#### **4. Camera Names**
- Switch to:
  ```
  Use Clip Names
  ```
  So your cameras show up in the Multi-Camera Monitor as:
  - "FX3"
  - "iPhone"
  
  …instead of just “Camera 1,” “Camera 2.”

---

### ✅ Final Checklist Before Clicking “OK”:
| Setting                    | Recommended |
|---------------------------|-------------|
| **Synchronize Point**     | Audio       |
| **Move to Processed Bin** | ✅ Enabled  |
| **Sequence Preset**       | Automatic   |
| **Audio Source**          | Camera 1 or All Cameras |
| **Camera Names**          | Use Clip Names |

---

### 💡 After You Click "OK":
1. A new **Multicam clip** will appear in your project bin.
2. Right-click that clip → **New Sequence from Clip**.
3. Open the **Program Monitor**, click the **Wrench (🔧)** icon →  
   ✅ Enable **Multi-Camera View**.
4. Press play and click camera angles live to insert edits!

---

Want me to generate a template folder structure and file naming system (`/Multicam/Processed`, `/Audio/`, `/Exports/`, etc.) for your project?

---



---

Thanks for the screenshots — the issue is now very clear.

---

## ⚠️ Problem: Premiere Pro **can't open your .mov files**
The error `"We were unable to open the file on disk"` typically happens when:

1. The file is **corrupted or incomplete** (e.g., not finalized).
2. The format is technically `.mov` but **wrapped incorrectly** (like `fragmented_mov`).
3. Premiere doesn't recognize the **codec or container** due to non-standard writing.

---

### ✅ Solution: **Avoid `fragmented_mov`** format

You're currently using:
```plaintext
Rec Format: fragmented_mov
```

This format is **designed for streaming**, not for post-production editing. It's **not finalized properly**, which is why Premiere can't read it.

---

### ✅ Recommended Recording Formats:
In the **Rec Format** dropdown (see your second screenshot), use **one of the following**:

#### 🟢 Best option (for Mac + Premiere):
- `mov` → Safe, QuickTime standard, ideal for FX3/iPhone workflows

#### 🟢 Second-best:
- `mkv` → Stable and safe for recording (requires remuxing before import)

---

### 🔁 Fix Instructions:

#### 1. In OBS:
- Go to each **Source Record filter**
- Change:
  ```
  Rec Format: fragmented_mov
  ```
  ✅ To:
  ```
  mov
  ```

#### 2. Re-record a short test file.

---

### 💡 Bonus: If you used `mkv`, you can remux:
- OBS menu → `File > Remux Recordings`
- Select `.mkv` file → convert to `.mp4` or `.mov`

---

### 🧼 Tip: Clean filenames (no spaces)
Avoid spaces in filenames — e.g., change:
```
iPhone-2025-09-01 15-38-13.mov
```
to:
```
iPhone_2025-09-01_15-38-13.mov
```

Use underscores in the `Filename Formatting` field:
```plaintext
iPhone_%CCYY-%MM-%DD_%hh-%mm-%ss
```

---

Let me know if you want a script or OBS preset to auto-apply these clean settings. Once you re-record with `mov`, you should be able to import and multicam with zero issues.

---

I wasn't using Fragmented Movie. I was using Movie. The screenshot I sent you doesn't say Fragmented Movie. It says Movie. So that's not the problem. So we're trying to figure out what happened here. It wasn't that because I wasn't using Fragmented Movie. I was using .MOV.

---

Thanks for the clarification — you're absolutely right. The screenshot shows that **`mov`** (not `fragmented_mov`) was selected, so let's rule that out.

---

## 🕵️ Let’s troubleshoot what **is** causing the import failure.

The error message:
> `"We were unable to open the file on disk"`

means Premiere **sees the file path**, but **cannot decode or access the media stream**. That narrows it down to the **file itself**, not just the format extension.

---

### 🔍 Top suspects now:

#### ✅ 1. **File was not finalized correctly (OBS write error)**
- OBS can fail to properly finalize a `.mov` if:
  - OBS was quit/crashed during recording
  - System shut down before buffer flushed
  - Source Record plugin glitched on write

> 🧪 **Test this**: Right-click one of the `.mov` files and **open it in QuickTime or VLC**.
- If it fails or has no duration, it’s likely corrupted.
- If it plays: it’s valid, and we shift to a codec/container issue.

---

#### ✅ 2. **Wrong codec inside .mov**
OBS lets you choose **container (.mov)** separately from **video codec** like H.264, HEVC, ProRes, etc.

- Premiere Pro struggles with some non-standard `.mov` encodings (especially HEVC from iPhones).

> 🧪 **Test this**:
1. Right-click the file in Finder > Get Info
2. Or run in Terminal:
   ```bash
   ffprobe "iPhone-*.mov"
   ```
3. Or drop it into **MediaInfo** (free tool):  
   [https://mediaarea.net/en/MediaInfo](https://mediaarea.net/en/MediaInfo)

You're looking to find:
- **Video Codec**: e.g., `avc1` (H.264), `hvc1` (HEVC)
- **Audio Codec**: e.g., `aac`, `pcm`

If it's **HEVC (hvc1)** and Premiere doesn’t have HEVC license activated, it will fail to import.

---

#### ✅ 3. **File permissions / sandboxing issue**
macOS privacy restrictions can block access, even if the file exists.

> 🧪 **Check this**:
1. Right-click the file > Get Info
2. Scroll down to “Sharing & Permissions” and **ensure you have read/write**
3. Open **System Settings > Privacy & Security > Files and Folders**  
   → Make sure **Premiere Pro** has access to the **folder**

---

#### ✅ 4. **File path length or characters**
Premiere can fail to open files with:
- Spaces in folder or filenames
- Excessive path length
- Unicode/special characters

> 🧪 **Fix this**:
1. Move both `.mov` files to a short path like:
   ```
   ~/Desktop/TestClips/
   ```
2. Rename them:
   ```
   iPhone.mov
   FX3.mov
   ```

Try importing from there.

---

### 🔁 Final Check — Re-encode with ffmpeg
If the file plays in VLC/QuickTime but still fails in Premiere:

```bash
ffmpeg -i "iPhone.mov" -c:v libx264 -preset fast -crf 18 -c:a aac -movflags +faststart "iPhone_fixed.mp4"
```

This **rewrites the container and stream** without quality loss (visually).

---

Let me know which of the files plays (if any), and I can give you a tailored fix or a re-encode script.

---

record mode?

---

Thanks — you're looking at the **Source Record “Record Mode”** setting. This determines **when the plugin actually saves the file**.

---

## 🔧 Here's what each option means:

### ✅ **Always** (recommended)
> Records **as soon as OBS is open**, whether or not you're officially "recording" in OBS.

- ✅ Best for capturing **everything** without needing to remember to hit record.
- Works **independently** of your main OBS recording button.
- Ideal for your use case (auto-saves FX3/iPhone feeds into separate files for editing).

---

### ▶️ **Recording**
> Starts saving only **when you click “Start Recording”** in OBS.

- Tied to OBS’s global record toggle.
- Good if you want manual control and syncing with a main video stream.

---

### 📡 **Streaming**
> Starts only when you click **“Start Streaming.”**

- Only useful if you're streaming live (not your current workflow).

---

### ⚙️ **Streaming or Recording**
> Starts if you do **either** recording or streaming.

- Useful if you're doing **hybrid livestream + local record** setups.

---

### 🪞 **Virtual Camera**
> Starts saving **only when OBS Virtual Camera** is turned on.

- Only relevant if you’re feeding OBS as a webcam into Zoom or Discord, etc.

---

## 🧠 Recommendation for you:

### Set **Record Mode** to:
```
Always
```
on **both** FX3 and iPhone Source Record filters

> 🔒 Ensures you don’t accidentally miss a recording just because you forgot to hit the main OBS record button.

---

Let me know if you want to automate folder creation or set an OBS profile where this is always enabled for each camera.

---

That would take massive amounts of drive space. It would just be recording all the time, wouldn't it?

---

You're absolutely right — and **yes**, if you choose **“Always”**, **OBS will record each source's feed continuously** from the moment you launch OBS, which **can eat up drive space fast**, especially with high-bitrate `.mov` files from multiple cameras.

---

## 🧠 Better Option for You:  
### 🔘 Set **Record Mode** to → `Recording`

This means:
- The Source Record **only records** when you click **“Start Recording”** in OBS.
- You maintain full control: no idle disk writes, no surprise 100GB folders.

---

### 🔧 Here's your optimal setup:

| Setting             | Value                      |
|---------------------|----------------------------|
| **Record Mode**     | `Recording` ✅             |
| **Rec Format**      | `mov` ✅                    |
| **Filename Format** | `FX3-%CCYY-%MM-%DD_%hh-%mm-%ss.mov` |
| **Folder Path**     | Organized per session or date |

---

## Bonus Tip: Clean Multi-Cam Workflow

1. Set **both** Source Record filters (FX3 and iPhone) to `Recording`.
2. When ready, hit OBS’s **Start Recording** button.
3. OBS records its own full scene (if you want)  
   ➕ each camera writes its own `.mov` file simultaneously.
4. All files = same start time = **perfect for multicam sync.**

---

Would you like:
- A script to **auto-create date-based folders** for each recording session?
- Or an **OBS scene collection + profile preset** with these settings pre-saved?

---



---

You're getting the **"Audio Synchronize Failure"** in Premiere because **one or more of your clips doesn’t have usable or matching audio** for automatic waveform syncing.

---

## 🧭 Here's what's likely happening:

### 🚫 Common reasons for this error:
1. **One of the clips has no audio** (e.g. silent or muted mic).
2. One track uses **a different mic**, different distance, or ambient audio that doesn’t line up enough.
3. OBS Source Record sometimes **outputs silent video** if the camera source had no mic.
4. **Different sample rates** (e.g. 44.1 kHz vs. 48 kHz) can throw off syncing.

---

## ✅ How to Fix It

### 🔍 Step 1: Check each clip's audio
- Double-click both clips in your Premiere Project panel.
- Open each in the **Source Monitor**.
- Do you see **waveforms**?
  - If one clip has **no waveform at all**, it's silent — and that’s the issue.
  - If both have visible waveform data but **look different**, then the audio may be too unalike to match automatically.

---

### 🔧 Step 2: Manual Sync (if needed)
If automatic audio sync fails, you can still:

1. **Drag both clips into the timeline**
2. Zoom in on waveforms (press `+`)
3. **Manually align the waveforms** by dragging one clip until the peaks match
4. Right-click both clips > **"Link"** once aligned

> 🧠 Pro Tip: If one file has no usable audio at all, **record a scratch audio track** (e.g. from your phone) next time for sync reference.

---

### 💡 Step 3 (Recommended): Use a separate audio recorder
For best multi-cam workflow:
- Use a **dedicated mic (e.g. lav or boom)** into a recorder or the FX3
- Sync all video to **that one master audio track**
- This is **industry standard** for post-production

---

### 🔁 Optional Workaround: Use time-based sync instead
If your clips have **similar start times**, try:
1. Right-click clips > **Create Multi-Camera Source Sequence**
2. Choose **“Timecode”** or **“In Points”**
3. (Only works if both clips have usable timecode or were started at the same moment)

---

Would you like a script or action setup to **auto-inject a click or slate sound at the beginning of every recording** for future sessions? That makes syncing foolproof.

---

The recording literally starts and stops at the same time all the time, so all I need to do is drop them in and they should be synced. Or is this for another reason like syncing down the road or something when I clip them, because they're not going to continue to sync up like that if I clip them, are they?

---

You are **exactly right** — and you're thinking ahead in all the right ways. Let’s break it down clearly:

---

## ✅ YES: Your OBS Source Record feeds **start and stop at the same time**, so they are already **perfectly in sync** when placed at the beginning of the timeline (00:00:00:00).

So:

> 🔹 If you **don’t clip** or cut the footage, you don’t need to sync anything at all.

---

## 🧠 BUT — when you **start cutting and editing**, that’s when things can go out of sync:

### 🎬 Here's why:
- When you trim or ripple edit **just one angle**, you'll **break alignment** between A-roll and B-roll.
- If you’re not using **linked or grouped clips**, those edits won’t ripple across both tracks.

---

## ✅ Best Practice: Use a **Multi-Camera Sequence** (with “In Point” or manual sync)

Since your clips are:
- Same start time ✅
- Same frame rate ✅
- Matching duration ✅

You can just:
1. Drop both into a **sequence** starting at 0:00.
2. Select both → Right-click → **"Create Multi-Camera Source Sequence"**
3. Choose:
   ```
   Synchronize using: In Points
   ```

You don’t need audio sync — just set in-points at the start (`I` on both), and Premiere will sync that way.

Now you get:
- 🖥️ Split-screen viewing (A/B at once)
- 🔁 One synced clip for editing
- 🎬 Easy switching between angles
- ⛑ Sync protection if you ripple/edit

---

## 🎯 Your workflow:
If you're always recording two feeds from OBS at exactly the same time:
- ⏱ Just trim both clips to the same start manually (or use In Points)
- 🧷 Keep them grouped, linked, or in a multi-cam clip
- 🪢 That way, they stay **glued together** through the whole editing process

---

Let me know if you want:
- A custom **multi-cam editing preset**
- A script that auto-aligns clips by filename and duration
- A macro to auto-cut both angles at once when editing manually

---

the iphone footage comes out smaller. I ahd to transform this clip but now its not Not part of the multicam composition. I just layered the clip on top of them so that I could zoom in on it. But what I actually want to do is zoom in on the one that has been processed and turned into the multicam view. But as you can see, it's much too small, and so I pulled the other one in to try to crop it. I could zoom in, but I don't think that's the right way. How do I get these sizes to match in the multicam view?

---

Ah yes — this is a **classic mismatch** between two camera sources with different **resolution**, **aspect ratio**, or **scaling metadata**, and you're seeing it play out inside your **Multi-Camera Source Sequence**.

---

## 🔧 Here's exactly what's happening:

1. Your **iPhone footage** is being interpreted by Premiere as **smaller** — likely due to:
   - Variable resolution (e.g. 1920×1080 vs 3840×2160)
   - Different pixel aspect ratio
   - Metadata (e.g. OBS "fit to canvas" or Source Record quirks)
   - Or a different **frame size** baked into the Source Record encoding

2. When you dropped that into a **Multi-Camera Sequence**, Premiere **preserved that scale** to avoid clipping — so the clip looks **tiny** compared to your FX3 feed.

3. You tried to fix it by adding the raw clip separately and scaling that — but that **breaks the multicam pipeline** and leaves you manually syncing, layering, and switching, which defeats the purpose.

---

## ✅ SOLUTION: Match scaling **inside the multicam sequence**

Let’s fix this the right way.

---

### ✅ STEP 1: Open the Multicam Source Sequence
- Right-click your multicam clip in the Project panel
- Choose:  
  **➡ “Open in Timeline”**
- You’ll now see **Camera 1** and **Camera 2** on separate tracks

---

### ✅ STEP 2: Scale the smaller clip
- Select the **smaller-looking video track** (likely iPhone)
- Go to **Effect Controls > Motion > Scale**
- Adjust `Scale` until it matches the other clip (usually 150% or 200% depending on difference)

> 🎯 You are now scaling **within the source**, not on the final multicam clip — so you retain all multicam functionality while fixing the appearance.

---

### ✅ STEP 3: Close the source sequence and return to your timeline
- Now when you cut between angles in the multicam timeline, the **scale will already match**.
- No need to layer duplicate clips or manually crop/zoom.

---

## 🧠 Bonus: Set Default Scale Behavior (Optional)
To avoid this in the future:

1. Go to **Preferences > Media**
2. Find:  
   **“Default Media Scaling”**  
   Change it to:
   ```
   Set to Frame Size
   ```
   or
   ```
   Scale to Frame Size
   ```
   depending on your workflow preference.

---

Would you like a template multicam sequence with auto-scaling baked in, or a preset that normalizes scale between different cameras for future sessions?

---

is it better to send the scene or the feed when recording dual in OBS. audio come through ua thunderbolt (apollo) not cameras.  

---

Great question — and your setup is serious pro-level: **dual camera feeds** via OBS + **audio via Apollo over Thunderbolt**. Here's the definitive answer for your workflow:

---

## ✅ Short Answer:
> **Send the individual camera *feeds*** using the **Source Record plugin** — not the whole scene.

---

## 🎯 Why? Because:

### 1. **You want clean ISO (isolated) recordings**
- Recording the **scene** bakes in overlays, scaling, switching, etc.
- Recording each **feed** via **Source Record** gives you:
  - Raw FX3 footage ✅
  - Raw iPhone footage ✅
  - No visual interference (cropping, layout, OBS transforms)
  - Ideal for multicam editing later in Premiere

---

### 2. **Audio is captured independently (Apollo)**
- Since your **audio is not coming from the cameras**, the best practice is to **record your Apollo audio in the OBS main track only** (via OBS’s global recording), or **via DAW** (Logic, LUNA, etc.).
- Most cameras will have **no useful audio** — and even if they do, it won’t match Apollo's timing perfectly.

---

## 🔧 Recommended Workflow for Dual Recording:

### 🎥 In OBS:
- **Scene**: Used for monitoring, live layout, livestream preview
- **Each camera source**:  
  - Apply **Source Record filter**
  - Set `Record Mode: Recording`
  - Set unique filenames like `FX3-%timestamp%` and `iPhone-%timestamp%`

### 🔊 In OBS > Settings > Audio:
- Route **Apollo Thunderbolt** input as **primary mic** into OBS
- Enable **global recording** if you want a "guide track" or visual sync reference

> Alternatively: **Record your Apollo audio separately** in your DAW. This gives perfect latency-free control and backup WAVs.

---

### 🧠 Bonus: Sync Strategy
To sync in Premiere later:
- Use the **Apollo audio track** (either OBS master or WAV from DAW) as the **master reference**
- Line up the two Source Record `.mov` files by start time
- If there's no usable audio in the video, use **start time matching** or clap/visual cue

---

## ✅ Summary
| What to Record               | How                                 |
|-----------------------------|--------------------------------------|
| FX3 feed                    | Source Record plugin (record mode: `Recording`) |
| iPhone feed                 | Source Record plugin (record mode: `Recording`) |
| Master audio (Apollo)       | In DAW **or** OBS main track         |
| OBS scene (optional)        | Use OBS global recorder if you want a reference/monitor track |

---

Want a sample OBS setup file (`.json`) that pre-wires all of this for dual cam + Apollo sync with matching filenames and folders?

---

I don't know what you mean by the main the main track in OBS. It's just an audio input so you know it's a track. So if the audio is going there, I have several other microphones to that I'll be using. I'm using... well that doesn't matter. So how do I record the audio is the point. Do I need to do it through source monitor or something or because I don't think I picked it up in the last two videos from either of those. So where is it getting recorded to? Do I need to assign it?

---

Got it — thank you for clarifying. Since you're using **Apollo Thunderbolt** and multiple mics, let’s make sure you’re **actually recording the audio** — and understand *where it goes* inside OBS.

You're absolutely right: if you didn’t **explicitly assign or record the audio input**, it probably didn’t get saved in the Source Record plugin videos (which usually don’t record global audio unless told to).

---

## ✅ SHORT ANSWER:
> **You must assign your Apollo input to the main OBS Audio Mixer AND use OBS’s main recording** if you want guaranteed audio capture.

---

## 🔊 Here’s the breakdown:

### 🎧 Audio in OBS comes from:
- **Audio Input Capture** sources (like your Apollo)
- Routed through the **Audio Mixer**
- Only recorded if:
  - You’re using **OBS's main recording** (Settings > Output > Recording)
  - **OR** you've added the audio manually to a Source Record filter (which is NOT default behavior)

---

## 🔥 THE PROBLEM:
The **Source Record plugin does *not*** include global audio **by default**.

So unless:
1. You added the Apollo mic source as a **filter to the video Source Record** (advanced), **or**
2. You were recording through **OBS’s main recording system**...

→ Then **your audio was not recorded** in those individual camera files.

---

## ✅ How to Record Your Audio the Right Way

### 🔧 Option 1: Use OBS's Main Recording
1. In OBS:
   - Go to **Settings > Output > Recording**
   - Set your output path + format (`.mov` or `.mkv`)
2. In your scene:
   - Add **“Audio Input Capture”**
   - Select **Apollo Thunderbolt** or appropriate mic interface
   - Confirm it shows up in the **Audio Mixer**
3. Hit **Start Recording** in OBS

✅ This will create a file with:
- **Audio from Apollo**
- **Your full scene** (but NOT the isolated FX3/iPhone feeds — those still come from Source Record)

---

### 🎯 Option 2: Record Audio in a DAW (Better for Multitrack Setup)
1. Open **Logic Pro**, **LUNA**, or any DAW
2. Arm track(s) for record from Apollo inputs
3. Record simultaneously while using OBS

✅ You'll get **clean WAV files** that are sample-accurate and multitrack

Later, sync to your OBS video using:
- **Manual alignment**
- **Clap slate**
- **Time start alignment**

---

### 🔧 Option 3 (Advanced): Add Global Audio to Source Record Filters (Not Recommended for Complex Setups)
This requires:
- Adding audio filters manually per Source Record feed
- Complicated, and can **duplicate or misalign** audio streams
- Best to use Option 1 or 2

---

## ✅ Checklist: Are You Capturing Audio?

| Check | Description |
|-------|-------------|
| 🔲 | Audio source (Apollo or mic) is added in OBS as “Audio Input Capture” |
| 🔲 | You see levels bouncing in the **Audio Mixer** |
| 🔲 | You are using **OBS's main recording**, OR recording audio in your DAW |
| 🔲 | You've tested the output file and confirmed audio is present |

---

Would you like a drag-and-drop OBS scene file that includes:
- Pre-assigned Apollo input
- Pre-wired Source Record filters
- Sync test slate
- Organized folders for recordings?

I can build one for your exact setup.

---



---

Perfect — this screenshot clears up **exactly what’s happening** and shows that you’re very close to a solid dual-feed + audio recording setup.

---

## 🧠 What You're Doing Right:
- ✅ You've added a **Source Record filter to your audio input** (`RODE Combined`)
- ✅ You’ve set **Record Mode** to `Recording`
- ✅ You’re capturing clean audio from multiple mics, **routed through OBS**

But... there are **two key issues** here:

---

## ❌ Issue 1: You’re using `fragmented_mov`
> This format may **not be reliably readable in Premiere Pro** and may not finalize properly — especially for audio-only tracks.

---

## ✅ Fix 1: Change Rec Format to `mov`
- In your **RODE Combined > Source Record audio** settings:
  - Change `Rec Format` to:
    ```
    mov
    ```

This ensures **maximum compatibility** with Premiere and most DAWs/editors. It also guarantees the file is properly finalized.

---

## ❌ Issue 2: You may still not be recording **video + audio in sync**
Right now, your:
- Camera feeds (FX3, iPhone) are recording via their **own Source Record filters**
- Audio is being recorded separately via a **Source Record filter on your mic source**

But these will be **3 separate files**:  
- `FX3.mov`  
- `iPhone.mov`  
- `RODE_Combined.mov`

So syncing them in Premiere will require **manual timeline alignment** unless you use a clap/slate or start-time-based sync.

---

## ✅ Best Practice Going Forward

### 🧩 Option 1: Full OBS Scene Recording (for backup + reference)
In **OBS Settings > Output > Recording**:
- Set to `.mov` or `.mkv`
- Include all audio/video
- Use this file as a **sync reference** if needed

### 🎯 Option 2: Use DAW for Audio (preferred for pro setup)
- Use Logic, LUNA, or even QuickTime to record the Apollo or RODE mixdown
- Get a clean `.wav` file with **no encoding loss**
- Drop that into Premiere along with your video feeds and sync manually

---

## ✅ Summary of What to Do Now:
| Task | Action |
|------|--------|
| 🔁 | **Change audio Source Record filter to `mov`** ✅ |
| 🎛 | Verify that **audio levels are active** in mixer (✅ as seen) |
| 📁 | Confirm the audio file actually writes to disk by testing |
| 🧪 | Do a **slate/clap** at the start of a recording session for easy sync in Premiere |
| 🗂 | Keep clean folder structure like `/Recordings/YYYY-MM-DD/` for organization |

---

Let me know and I can generate a custom OBS profile for you with:
- Dual camera Source Records
- Audio Source Record filter set to `.mov`
- Folder structure and filename templating
- Optional sync slate overlay or tone generator

---

I'm already doing that. I have the full scene thing recorded. I found that. It has the audio or whatever, but not the separate files. That's fine. I'm only recording... This is all synced up when I hit record, so the audio and the video are already synced up. So all I have to do is drop them in at the beginning. The files should be the same size as the video. It should stop and start at the same time, so it shouldn't be an issue.

---

✅ **Exactly — you're doing it right.**  
If you’re recording everything at once (video feeds + audio) and they all **start/stop with the OBS record button**, and you’ve:

- 🎥 Source Record filters on each camera (FX3, iPhone)
- 🎙️ Source Record filter on your combined audio (RODE/Apollo)
- 🧱 All recordings triggered by OBS “Start Recording”
- 🕐 No editing mid-recording or sync drift

👉 Then yes — **everything will line up perfectly** just by dropping all the files into the timeline at `00:00:00`.

---

### 🧠 What This Means for Your Workflow:

| Component        | Source            | Output File                     | Sync Needed? |
|------------------|-------------------|----------------------------------|---------------|
| FX3 video        | Source Record      | `FX3-2025-09-01_15-38-45.mov`    | ❌ No         |
| iPhone video     | Source Record      | `iPhone-2025-09-01_15-38-45.mov` | ❌ No         |
| Audio (Apollo)   | Source Record on mic source | `RODE-Combined-2025-09-01_15-38-45.mov` | ❌ No         |
| Scene Reference  | OBS global recorder | `FullScene-2025-09-01.mov`       | ❌ Only for backup/reference |

---

## 🎯 What to Watch Out For:
Just these two things:

1. **Filename mismatch or delay**
   - If filenames are timestamped with slightly different seconds, line up by **start time**, not name.
   - Always align to `00:00:00` in Premiere manually (don't trust metadata start time).

2. **Visual scaling mismatch (which you already saw)**
   - Fix via **opening the multicam source sequence**, and scaling the smaller feed

---

## 🧱 Final Suggestion for Post Workflow
When importing into Premiere:

1. Drop:
   - `FX3.mov` to V1
   - `iPhone.mov` to V2
   - `RODE-Combined.mov` to A1
2. Line them all up at 00:00
3. Optionally group (`Cmd+G`) or nest them
4. Save as "Synced Composite"

---

You're officially running a **pro-grade multicam setup**. Let me know if you want:
- A **timeline preset** template for Premiere
- A script to **auto-rename and sort OBS files**
- A visual sync overlay (clapboard/slate) baked into OBS for future shoots

---

Review how to split screens in Premiere Pro. I selected the two clips I want, A-cam and B-cam. And I created a multi-camera sequence. I don't see the sequence here. I'm thinking that the next step would be to try the sequence at timeline. I created a multi-camera sequence by selecting the two clips in the bins and then right-clicking. Should I drag the two clips to the timeline now? And then what do I need to do?

---



---



---

Great — you’re right on the edge of **multi-camera editing glory** in Premiere Pro. Let’s walk you through exactly how to **split-screen view**, **edit**, and **switch between A-cam and B-cam**.

---

## ✅ STEP-BY-STEP: Multicam Editing in Premiere Pro

---

### ✅ **Step 1: Create the Multi-Camera Source Sequence (you already did)**
- You selected A-cam and B-cam → Right-click →  
  ✅ **“Create Multi-Camera Source Sequence”**
- You probably named it something like `Multicam_01`

> ⚠️ You will NOT see it in the timeline automatically — Premiere creates the multicam clip in the **bin**.

---

### ✅ **Step 2: Locate the Multicam Clip**
- Go to the **Project panel / bin** where you created the sequence
- Look for the new multicam clip:
  - It has a **filmstrip + stacked camera icon**
  - It’s **not** one of your original A or B clips
  - Example: `Multicam_01` or whatever you named it

---

### ✅ **Step 3: Create an Editable Timeline**
1. **Right-click** the multicam clip in the bin
2. Select:  
   ```
   New Sequence from Clip
   ```

🟢 This opens the timeline with the multicam clip ready to edit

---

### ✅ **Step 4: Enable Multi-Camera View**
1. In the **Program Monitor**, click the **wrench icon (🔧)**
2. Select:  
   ✅ **Multi-Camera View**

Now you'll see a **side-by-side view**:
- Left side = Camera 1 (A-roll), Camera 2 (B-roll)
- Right side = your active program playback

---

### ✅ **Step 5: Play & Switch Angles Live**
- Press spacebar to play
- **Click on a camera** in the Multi-Cam panel to switch views
- Premiere **adds an edit cut automatically** every time you click

---

### ✅ Step 6: Refine Edits (Optional)
- Use the **Rolling Edit Tool (N)** to adjust cut points
- Right-click cuts to **change camera angle**
- You can even apply effects (zoom, LUTs, etc.) after the multicam is flattened

---

### ✅ 🔥 Optional: Split-Screen View of Both Cameras
If you want **both angles on-screen at once** (not switching):
1. **Open the Multi-Camera Source Sequence** (right-click → Open in Timeline)
2. Go to each clip (A-cam, B-cam) and:
   - Scale to 50%
   - Position one left, one right (Effect Controls → Position)

That creates a **side-by-side split screen**, instead of switching between angles.

---

## 🎯 Summary:
| Action                          | What to Do                             |
|----------------------------------|-----------------------------------------|
| Create Multicam Source Sequence | ✅ Done |
| Locate multicam clip in bin     | Find it in the Project panel |
| Create sequence from it         | Right-click → New Sequence from Clip |
| Enable Multi-Camera view        | Wrench (🔧) in Program Monitor |
| Split-screen (optional)         | Open source seq → scale + position |

---

Let me know if you want:
- A multicam template project
- A macro to auto-create split screen
- A shortcut layout for switching/editing more quickly

---

fx30 is smaller

---

Thanks for the screenshot — it confirms what you’re seeing:

- You’re in **Multi-Camera View** in Premiere Pro.
- **Camera 2 (FX30)** appears **smaller** than the others in the preview grid.
- On the right (Program Monitor), the **output is showing Camera 2**, and it’s clearly smaller than fullscreen.

---

## 🧠 Why This Happens:

The **FX30 clip** was likely recorded at a different resolution or **OBS scaled it down** during Source Record (e.g. due to a filter or canvas mismatch). Premiere is preserving that smaller scale **inside the Multi-Camera Source Sequence**.

---

## ✅ How to Fix It (Properly)

You need to **scale the FX30 clip up inside the Multi-Camera Source Sequence**, not in the final timeline.

---

### 🔧 Step-by-Step Fix:

1. **In the Project Panel**:
   - Right-click the **multi-camera source sequence**
   - Choose 👉 **"Open in Timeline"**

2. You’ll now see your **FX3 and FX30** camera tracks (V1, V2, etc.)

3. **Select the FX30 clip** (whichever is the smaller one)

4. Go to **Effect Controls > Motion > Scale**
   - Increase the **Scale** until it matches the full-frame size of your FX3 footage (e.g. from 50% → 100%, or 100% → 150%, depending)

5. Close that timeline tab.

6. Go back to your multicam sequence — now FX30 should **appear full size** in the Multi-Camera view and in the final Program Monitor.

---

## 🧼 Bonus Tip (for future sessions):

To avoid this mismatch:
- Ensure OBS is recording **all sources at the same base resolution** (e.g. 1920×1080 or 4K)
- In OBS > Settings > Video:
  - Set both the **Base (Canvas) Resolution** and **Output Resolution** to match your target (e.g., 1920x1080)

---

Let me know if you'd like:
- A preset multicam source sequence template
- A script to auto-match scale and position across clips
- OBS Source Record settings pre-matched for camera resolution targets

---

so now i want to adjust gamma etc 

---

Perfect — if you want to **adjust gamma, contrast, color, exposure, etc.** on your multicam angles in **Premiere Pro**, here’s the clean and professional way to do it:

---

## 🎯 GOAL:
Apply **color correction (e.g. gamma adjustments)** to each **camera feed separately**, **before** multicam switching.

This ensures that every angle **looks consistent** before you cut between them.

---

## ✅ STEP-BY-STEP: Adjust Gamma & Color Per Camera in Multicam

### 🔧 Step 1: Open the Multicam Source Sequence
1. In your **Project Panel**, right-click your **multicam clip**  
   ➤ Select **“Open in Timeline”**
2. This opens the sequence where each camera is on its own track:
   - V1 = FX3
   - V2 = FX30
   - etc.

---

### 🎛 Step 2: Apply Gamma Correction to Each Camera Clip
1. **Select the camera clip** (e.g., FX30 on V2)
2. Go to **Window > Lumetri Color**
3. Under **Lumetri > Basic Correction**, adjust:
   - ✅ **Gamma**: via the **Midtones (Exposure + Contrast)** sliders
   - ✅ Or tweak via **Curves** > **RGB Curve** (drag midpoint up/down)
4. You can also adjust:
   - Exposure
   - Highlights/Shadows
   - Saturation
   - Contrast
   - White balance (Temp/Tint)

📌 **Repeat for each camera track** if needed

---

### 🧪 Pro Tip: Use Adjustment Layers (Optional)
If you want non-destructive control:
1. Go to **Project Panel > New Item > Adjustment Layer**
2. Drag the layer above a single camera track in the **source sequence**
3. Apply **Lumetri Color** to the adjustment layer instead

This keeps your color correction modular and tweakable later.

---

### 🪞 Step 3: Return to Main Multicam Sequence
- Now when you cut between cameras, the **corrected color** will carry over
- All edits downstream reflect these changes

---

## 🎥 Optional: Match Color Between Cameras
1. Select a clip (e.g., FX30)
2. Go to **Lumetri > Color Wheels & Match**
3. Click **Comparison View**
4. Select another angle as the reference (e.g., FX3)
5. Click **Apply Match** to automatically balance exposure/gamma

---

Let me know if you want:
- A **preset LUT for FX3/FX30/iPhone matching**
- A batch gamma fix using adjustment layers
- A side-by-side split screen to fine-tune live with scopes

---

Those adjustment layers and structures don't actually make any sense, given what I'm seeing here. I don't... Every time you go back to what you had to do, or what I was trying to think was, I'm already there. Here is the adjustment layer, as I said. This is the fan, this is the output at the top of there, and... You know, there's no way to really go from here. I can't add it to the layer.

---

Thanks for the screenshot — you're absolutely right to call out that this doesn’t behave like a typical timeline setup, because you’re working directly inside a **Multi-Camera Source Sequence**, and **adjustment layers won’t behave the way you'd expect in this context**.

---

## 🔎 What You’re Looking At:
You’re inside the **Multi-Camera Source Sequence timeline**, where:
- Each camera clip is laid out as its own **full-length video layer** (V1, V2, V3…)
- The final multicam output will reference this sequence, but:
  - **Adjustment layers don’t apply properly** unless added in the **target sequence** (the actual timeline where you switch between angles)
  - And **Lumetri Color or gamma settings** must be applied **directly to the clip**, or via **nesting**

---

## ✅ Solution Options for Gamma / Color Correction

---

### 🔧 Option 1: **Apply Lumetri directly to the camera clip**
Since you’re already in the **source sequence**, just:

1. **Select the clip** (e.g. the FX30 on V3)
2. Go to **Lumetri Color panel** (Window > Lumetri Color)
3. Apply your gamma / curve / exposure correction directly here
4. **Repeat for each camera** as needed

✅ This ensures each camera is corrected *before* it hits your multicam sequence

---

### 🛠 Option 2: Use Nesting if You Need an Adjustment Layer
Adjustment layers **only affect layers beneath them**, and in this case, the multicam structure doesn’t allow for that.

Instead:

1. **Nest each camera clip**
   - Right-click each clip (e.g., FX3 on V1) → **Nest...**
   - Name it accordingly (`FX3_Nested`)
2. Drag your **Adjustment Layer** above the nested clip
3. Apply **Lumetri Color** to the adjustment layer

✅ Gives you modular control, but adds one more level of nesting

---

### 🎯 Option 3: Apply Gamma Fix to Final Sequence (Not Recommended for Per-Cam Correction)
You *can* apply an adjustment layer in your final edited multicam sequence — but it will affect **all angles equally**, which defeats the point of correcting per-camera gamma differences.

---

## 🧠 Key Insight:
> The **Multi-Camera Source Sequence** acts like a pre-comp — it’s **not a normal editing timeline**. So you **must apply color/gamma fixes directly to the source clips** inside it — or use **nested clips + adjustment layers** if you want more control.

---

## ✅ What to Do Now:
| Task | Action |
|------|--------|
| 🎥 Gamma off in FX30 | Apply Lumetri to V3 (FX30) in the multicam source sequence |
| 🎛 Need overall look | Use Adjustment Layer in final timeline |
| 🎨 Per-cam LUTs | Apply in source sequence or to nested clips |

---

Let me know if you'd like:
- A Lumetri preset to match FX3 to iPhone/FX30
- A side-by-side frame for live color balancing
- A gamma test chart overlay you can use inside OBS or Premiere

---

These instructions aren't really getting me there, so... I got the color wheels to match. How do I click... I got the comparison view, but how do I select another angle as a reference? It doesn't... I don't know how to do that. And then, um... Yeah. Apply match to... Yeah, none of this is coming up.

---

Thanks for the screenshot — this clears it all up. You're in the right place: **Lumetri Color > Color Wheels & Match > Comparison View**, but you're missing **how to switch between reference and current clips** so you can use **Apply Match**.

Here’s exactly how to do it, **step-by-step**, using Premiere's **Comparison View** and **Apply Match** for color matching between two camera angles.

---

## ✅ GOAL:
Use one clip (e.g. FX3) as a **color reference**, and apply the match to another (e.g. FX30), using **Lumetri's automatic color match tool**.

---

## 🔧 STEP-BY-STEP: Use Apply Match Correctly

---

### ✅ 1. Enable Comparison View
You’ve already done this — you’re in:
```
Lumetri Color > Color Wheels & Match > Comparison View ✅
```

- The **left image** is your **reference**
- The **right image** is the **current clip**

---

### ✅ 2. Move the Playhead to the Reference Clip
- Move your **timeline playhead** to the **clip you want to use as the reference** (e.g., FX3)
- In **Comparison View**, click the left-side (reference) thumbnail to “lock” this as your comparison

---

### ✅ 3. Move the Playhead to the Target Clip (FX30)
- Now move the playhead **later in the timeline** (or earlier) to land on your **FX30 clip**
- The **right-side image** in the Comparison View updates automatically — this is the **clip that will receive the match**

---

### ✅ 4. Click “Apply Match”
- Make sure you're on the **clip you want to color correct**
- Then click the **“Apply Match”** button under the three color wheels

Premiere will:
- Analyze the **reference clip (left)**
- Adjust your **target clip (right)** to match it (especially **Midtones**, but also Shadows & Highlights)
- Apply those changes as keyframes in the **Lumetri Color > Color Wheels & Match** section

---

### 📌 Notes:
- If **Apply Match** is grayed out, make sure you’ve selected the clip in the timeline and are inside the Lumetri panel
- You can use the **“Timeline” mode** in Comparison View (instead of “Shot”) if you want to scrub for the best reference frame

---

### 🔁 Bonus: Manually Fine-Tune After Match
Once matched:
- Use **Curves** or **Basic Correction** to tweak exposure, white balance, gamma, etc.
- You can add additional **Lumetri instances** for modular control

---

## ✅ Summary Flow:
| Step | Action |
|------|--------|
| 1 | Enable **Comparison View** |
| 2 | Move playhead to **reference clip (FX3)** |
| 3 | Lock reference (left image) |
| 4 | Move playhead to **target clip (FX30)** |
| 5 | Click ✅ **Apply Match** |
| 6 | Fine-tune with sliders or scopes |

---

Want me to create a reusable color preset (Lumetri) for your FX3 → FX30 matching curve, or help you build a side-by-side grade comparison sequence with scopes aligned?

---

trying to match the output res for fx3 fx30 and obs 

---

Thanks — you're on the right track. You're in **OBS > Video settings**, looking at:

- **Base (Canvas) Resolution**
- **Output (Scaled) Resolution**
- **Common FPS Value**

Let’s make sure these match the **FX3**, **FX30**, and your editing pipeline so you get full-frame captures from both cameras with **zero resizing, scaling artifacts, or black borders.**

---

## ✅ TARGET SETTINGS for Matching FX3 / FX30 / OBS:

### ⚙️ FX3 & FX30 (Default Recording Settings)
- Resolution: `3840 × 2160` (4K UHD)
- Frame rate: `23.976` or `29.97` (depending on your settings)
- Color space: S-Log3, Rec.709, etc. (for grading)

---

## 🔧 OBS Settings You Should Use to Match FX3 / FX30

If you're trying to **record in 4K to match the camera files** (ideal for color work, crop-ins, multicam), change:

### OBS > Settings > **Video**:
| Setting                   | Suggested Value         |
|---------------------------|--------------------------|
| Base (Canvas) Resolution  | `3840 x 2160` ✅ (Match FX3/FX30) |
| Output (Scaled) Resolution | `3840 x 2160` ✅ |
| Downscale Filter          | Bicubic or Lanczos (if you scale later)
| Common FPS Values         | `30` or `29.97` ✅ (Match camera)

---

### OBS > Settings > **Output** > Recording:
| Setting              | Suggested Value          |
|----------------------|---------------------------|
| Recording Format     | `mov` ✅ |
| Encoder              | `Apple VT H.264` (or `ProRes` if available and drive space allows)
| Rate Control         | `CBR` or `VBR`
| Bitrate              | `> 50,000 Kbps` (for 4K)

---

### 🔁 Final Checklist:
| Device | Resolution | FPS | Matches OBS? |
|--------|------------|-----|---------------|
| FX3    | 3840x2160  | 30  | ✅             |
| FX30   | 3840x2160  | 30  | ✅             |
| OBS    | 3840x2160  | 30  | ✅             |

**If you're still seeing black bars** or scaling:
- Check the **Source Transform settings** (right-click the source → `Transform → Fit to Screen`)
- Make sure the **video feed from CamLink** or HDMI capture **isn't being scaled in Source Record**

---

## 🚀 Want Performance? Drop to 1080p
If your project is outputting **1080p**, and you only need 4K for cropping, you can keep:
- **OBS Base Resolution** = `3840x2160`
- **Output Resolution** = `1920x1080` ✅

But only **if** you're fine with losing native 4K detail in the OBS scene file.

---

Let me know:
- If your FX30 or FX3 are recording in **4K DCI (4096x2160)** instead
- If you're routing video via CamLink, HDMI → what resolution is it sending to OBS?
- If you'd like a custom OBS profile `.json` with pre-matched canvas + sources + Source Record filters and folders.