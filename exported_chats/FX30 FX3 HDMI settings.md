# FX30 FX3 HDMI settings



---



---



---

So in this picture the FX-30 is the one that has the camera settings going on it and the FX3 is the one that doesn't. Now what are the difference in the settings here because one seems to have a smaller picture but it has the settings on it as well. Can't both of these be coming out at the same size? How do I get it to match?

---



---



---

What you’re seeing is a mismatch in how each camera is outputting its HDMI signal. Here’s the breakdown:

### FX30 feed (top left, also in the bottom left preview)
- Has the overlay with shutter, iris, ISO, etc.
- The image area is smaller inside the frame, which means **it’s sending out a “Display Info On” HDMI feed** instead of a clean feed.
- That smaller picture-within-a-frame look is the **camera preview UI** being piped out, not the actual full-frame sensor image.

### FX3 feed (center right, “Scene 2” / “Program”)
- No camera settings cluttering the output.
- Clean HDMI feed, filling the frame properly.
- That’s why it looks larger and matches the monitor output without black bars or borders.

---

### Why they don’t match
- **The FX30 is set to output HDMI with overlays (Info Display ON)**.
- **The FX3 is set to output HDMI clean (Info Display OFF)**.
- That “smaller picture” effect is basically the camera GUI taking up part of the HDMI signal.

---

### How to fix it
On the FX30:
1. Go to **Menu → Setup (wrench icon) → HDMI Settings**.
2. Look for **HDMI Display Info** (sometimes called “HDMI Info. Display”).
3. Set it to **Off**.  
   This gives you a **clean feed** like the FX3.
   
Optional:  
Also check that **HDMI Resolution** and **Output Rec Control** are set the same as your FX3 (e.g., 4K 59.94p, Clean Feed).

---

Once you do that, **both the FX30 and FX3 will output full-size, clean HDMI feeds**. Right now, the FX30 is basically just vomiting its viewfinder UI onto your switcher.  

Want me to map out the exact HDMI menu differences between FX30 vs FX3 so you can make sure they stay in sync?

---

they look very different

---

Yeah, they look like two cameras that went to different schools. Let’s untangle what’s happening:

### Left side (Preview: Scene)
- Shutter: 1/80  
- Iris: f/2.8  
- ISO: 1000  
- **Exposure comp: +0.3**  
- WB: Auto (AWB)  
- Look: warmer, more natural skin tones  

### Right side (Program: Scene 2)
- Shutter: 1/80  
- Iris: f/2.8  
- ISO: 1000  
- **Exposure comp: 0.0**  
- WB: Auto (AWB)  
- Extra overlays: recording standby indicator (STBY), timecode, histogram, file name (C0883), battery info, etc.  
- Look: cooler, more bluish  

---

### Why they look different
1. **Exposure Compensation**
   - Left camera is at **+0.3** EV.  
   - Right camera is at **0.0** EV.  
   That’s already a brightness and tone shift.

2. **White Balance**
   - Both say AWB, but AWB isn’t identical across cameras. The FX30 and FX3 don’t always “agree” on neutral color under the same light. One can skew warmer, the other cooler.

3. **Gamma / Picture Profile**
   - The right camera (FX3) looks like it might be running a **different picture profile** (S-Log, Cine, or just a flatter gamma).  
   - The left camera (FX30) looks closer to a standard Rec.709 tone curve.  
   That alone explains why one looks flat and bluish while the other looks warmer and contrastier.

4. **HDMI Overlays**
   - FX3 is dumping *all* overlays, including histogram and timecode.  
   - FX30 is only showing basic overlays.  
   You can normalize this in each camera’s **HDMI Info Display** setting.

---

### How to match them
1. On both cameras, go into **Menu → Exposure → Exposure Compensation**. Match them (either both 0.0 or both +0.3).  
2. Set both to the **same Picture Profile (PP1, PP8, S-Log3, etc.)**. Don’t trust “AWB” to make them match—use the exact same PP.  
3. Lock the **same Kelvin WB** (not AWB). Pick something like 5600K for daylight, 3200K for tungsten, and disable Auto.  
4. In HDMI settings, turn **HDMI Info Display → Off** for clean feeds, unless you *want* those overlays.

---

So right now:
- FX30 = warmer, slightly boosted exposure, simpler HDMI overlay.  
- FX3 = flatter/cooler, no exposure boost, full HDMI overlay clutter.  

If you want them to match, the magic trio is: **exposure comp, WB lock, picture profile sync.**  

Do you want me to give you the exact Sony menu path for locking WB and picture profile on both so they stop looking like two cameras in a bad marriage?

---

yes. lol how do I lock the WB

---

Finally, someone asks the question that every Sony menu designer secretly hopes you’ll never figure out. Here’s how you lock WB so your cameras stop gaslighting each other with different blues and oranges:

---

### On FX30 & FX3 (same basic menus)
1. **Hit Menu**  
   Go to the **Camera Settings (the little camera icon)**.

2. **Navigate to White Balance**
   - FX3: *Camera Settings 1 → Page 10/14 → White Balance*  
   - FX30: *Camera Settings → Exposure/Color → White Balance*

3. **Choose a Preset or Kelvin**
   - **Presets:** Daylight, Incandescent, Shade, etc.  
   - **Custom:** Point the camera at a neutral white/grey card, hit *Set*, it locks WB to that exact light.  
   - **Kelvin:** Scroll down to “Color Temp” and dial in a number (e.g., 5600K for daylight).  

4. **Lock It**
   - Once you’ve set WB, it **stays locked** until you manually change it.  
   - Avoid “AWB” (Auto WB) like the plague—Sony’s “auto” loves to randomly shift during recording, especially if someone walks in wearing a blue shirt.

---

### Recommended for Multi-cam Matching
- **Use Kelvin WB:**  
  - Daylight? Set both cams to **5600K**.  
  - Indoors tungsten? **3200K**.  
- Or, use a **grey card** under your actual lights and do a custom WB on both cameras.  

---

So: **Menu → Camera Settings → WB → Set to Kelvin (e.g., 5600K) or Custom WB with a grey card.**  
That locks it, no more wandering colors.

Want me to also give you the exact Picture Profile settings so the FX30 and FX3 *really* look identical, not just close?

---

its not letting me change the exposure compensation

---

That’s Sony for you—ten thousand menu options and half of them greyed out depending on what mode you’re in. Exposure compensation is one of those tricky ones. Here’s why you can’t change it right now:

---

### Why Exposure Comp might be locked
1. **Manual mode (M):**  
   In full manual, exposure compensation does nothing—because you’re already directly controlling shutter, aperture, and ISO. The camera assumes *you* are the brain.

2. **ISO set to Manual:**  
   Even in Aperture or Shutter priority, if ISO is locked, exposure comp may grey out.

3. **Log / Picture Profiles:**  
   If you’re in S-Log or a flat cine profile, some exposure options get restricted. Sony forces you to expose via ISO/shutter/aperture instead.

4. **Exposure Compensation Dial Setting:**  
   On some configs, the dial or wheel has to be assigned to “Exposure Comp.” If it’s not mapped, you’ll just see it frozen.

---

### How to actually adjust exposure between cameras
Since you’re in **manual video shooting**, the way to “match exposure” is not exposure comp but:
- **Shutter speed** (keep consistent—both are at 1/80, fine).
- **Aperture** (both f/2.8, fine).
- **ISO** (both at 1000, fine).
- **Picture Profile black levels / gamma curve.** ← sneaky culprit.

So in your case:  
The FX30 was at +0.3 EV earlier because you had it in a semi-auto mode. Now that you’re in full manual, **exposure comp is meaningless**. To brighten/darken one camera to match the other, you’ll either:
- Adjust ISO slightly (e.g., ISO 1250 vs 1000).  
- Or tweak the **Picture Profile black/gamma settings** so they render similarly.

---

### Quick fix
1. **Match ISO** manually (don’t expect exp comp to help).  
2. **Disable AWB, lock WB** (like we covered earlier).  
3. **Sync Picture Profiles** (PP1 = Rec709, PP8 = S-Log3, etc.)—make sure both are the same.

---

Want me to write out the **exact menu path to set both cams to a simple, identical Rec.709 profile** so you stop chasing exposure comp around like it owes you money?

---

	Picture Profile black levels / gamma curve

---

Exactly—the *real* reason your two cameras don’t look the same has less to do with exposure comp and more to do with the **picture profile (PP)** they’re set to. Sony hides a whole second world of color and contrast under “Picture Profile.” Here’s the rundown:

---

### What Picture Profile Does
- **Gamma curve**: how shadows/midtones/highlights roll off (Rec.709 vs S-Log3 vs Cine4, etc.).  
- **Black Level**: whether shadows sit true black or lifted.  
- **Color Mode**: Rec.709, S-Gamut, Pro, Movie, etc.  
- **Detail**: sharpness baked into the image.  

If one camera is in PP Off (default Rec.709 look) and the other is in S-Log3 (super flat and blue), they’ll look like two completely different worlds.

---

### How to Match
1. **Menu → Color/Tone → Picture Profile → ON**  
   - FX30: Camera → Exposure/Color → Picture Profile.  
   - FX3: Camera Settings 1 → Page 12 → Picture Profile.

2. **Pick the Same PP Number**  
   - For easy matching, start with **PP1 (Movie, Rec.709)** on both.  
   - If you want cinematic but still matchable: **PP6 (Cine2)** or **PP8 (S-Log3)** on both.

3. **Black Level**  
   - Inside PP menu, you’ll see **Black Level**.  
   - Default is 0, but if one cam is set to -2 (crushed shadows) and the other +2 (milky shadows), they’ll never match.  
   - Set both to the same (usually 0).

4. **Gamma Curve**  
   - PP1: Movie (Rec.709)  
   - PP8: S-Log3  
   - Both must be identical—mixing PP1 and PP8 will look like one’s “ready to edit” and the other’s “flat and lifeless.”

5. **Color Mode**  
   - Keep identical: Movie, ITU709, S-Gamut3.Cine, etc.  

---

### Shortcut if You Just Want Them to Match Quickly
- Set **Picture Profile = OFF** on both.  
   → This forces a standard Rec.709 look, no weird gamma curve differences.  
- Or pick **PP1 on both** and don’t touch it.

---

So the “black levels / gamma” thing = inside the **Picture Profile** menu. That’s where one of your cameras is quietly betraying you.  

Do you want me to lay out a **step-by-step for setting both FX3 and FX30 to Rec.709 (no log, no surprises)** so they look nearly identical straight out of HDMI?

---



---

Now you’re getting somewhere—both feeds finally look like they’re in the same ballpark. The differences are smaller, but I can still see the gap:

- **Preview (left)**: warmer, more yellow in the skin and room.  
- **Program (right)**: slightly cooler, flatter contrast, shadows look a bit deeper.  

That’s the **picture profile gamma/black level** difference still peeking through. The good news is you can kill it at the root.

---

### Step-by-Step: Set Both to Rec.709 (Standard Look)
On **both FX30 & FX3**:

1. **Menu → Camera Settings → Exposure/Color → Picture Profile**  
   (FX3 path: Camera Settings 1 → Page 12 → Picture Profile)

2. **Turn Picture Profile = ON**.  
   Choose **PP1** (this is “Movie” gamma, Rec.709 color).  
   - Gamma = Movie  
   - Color Mode = Movie  
   - Black Level = 0 (reset if it’s been tweaked)  

3. **Double-check sub-settings**:  
   - **Black Gamma**: Middle, 0  
   - **Knee**: Auto  
   - **Saturation**: 0  
   - **Detail**: 0  

4. **Do this on both cameras** so they’re literally identical.

---

### If you want to go even cleaner
- Skip Picture Profiles entirely: **Set Picture Profile = OFF** on both.  
   This gives you Sony’s default Rec.709 baked-in look, which is fine for streaming and multi-cam switchers.  
   → The downside is less flexibility in post.  

---

### Why this works
- Right now, one of your cams is almost certainly on **PP8 (S-Log3)** or a Cine gamma, while the other is on Rec.709 or PP Off.  
- That explains why one looks more neutral/flat while the other looks warmer and “video-ready.”  

---

Lock WB (both at same Kelvin), set **PP1 or OFF** on both, and the feeds will stop fighting you.  

Want me to give you the **exact tweaks if you’d prefer to run S-Log3 (PP8)** on both instead, so you have maximum grading flexibility later? Or do you just want the easy Rec.709 match for switching?

---

theyre on the same

---

Got it—if both cameras are on the same **Picture Profile**, yet they’re still showing slight differences like in your screenshot, here are the usual suspects:

---

### 1. **White Balance**
- Even if both say *AWB* or both are set to *Kelvin 5600K*, small mismatches creep in.  
- AWB especially will drift between bodies.  
✅ Solution: set a **custom white balance** on both with the same grey/white card under your actual lights.

---

### 2. **Black Level / Black Gamma**
- Inside the PP menu, check if **Black Level** or **Black Gamma** got nudged.  
- Even a ±1 difference will make shadows look warmer or cooler.  
✅ Solution: reset both to 0.

---

### 3. **Color Mode Sub-settings**
- Both cameras can say “Movie” or “ITU709” but still have slightly different saturation or phase adjustments.  
✅ Solution: go into **Color Mode → Reset** on both.

---

### 4. **ISO Calibration**
- Even if both say ISO 1000, Sony sensors don’t line up perfectly. One body might be effectively ISO 950, the other 1050.  
✅ Solution: open the waveform monitor in your switcher/OBS, and adjust one cam’s ISO or aperture by 1/3 stop until skin levels match.

---

### 5. **Sensor Variation**
- FX30 (APS-C) vs FX3 (full-frame) = different sensor designs. Even with the same PP, they don’t render 100% identical.  
- The FX3 tends to look flatter and slightly cooler; FX30 has a touch more baked-in warmth.  
✅ Solution: accept they won’t *perfectly* match out of the box. You’ll always need a slight correction in your switcher or post.

---

### Quick Practical Fix
1. Lock **Kelvin WB** (not AWB) on both.  
2. Reset **Black Level/Black Gamma** to 0.  
3. Use your switcher’s **color correction** (lift/gamma/gain or tint wheels) to fine-tune them live.  

---

So: if they’re on the same PP, it’s **not settings mismatch—it’s body difference.** You’ll never get them 100% identical in-camera. You can get them *close*, and then polish inside your switcher.

Do you want me to give you the **step-by-step for doing the fine color match inside OBS/ATEM**, so you don’t waste more time digging through Sony menus that will never fully sync?

---



---

This shot really shows the story: same PP, same exposure, but the FX30 (Preview/Scene) and FX3 (Program/Scene 2) are still rendering a little differently.  

- **Preview/Scene (likely FX30)** → warmer skin, slightly more red in the midtones.  
- **Program/Scene 2 (likely FX3)** → cooler, flatter, shadows look denser, and overall less red.  

That’s *textbook sensor/processing difference*. Even with identical settings, the FX30 (APS-C) and FX3 (full frame) won’t spit out identical Rec.709 color. Sony doesn’t bother to tune them perfectly because they’re aimed at different users (cinema vs hybrid).  

---

### The practical way to match them now
Since the menus are already the same:

1. **Lock WB** to the same Kelvin (don’t use AWB). If your lights are daylight, pick **5600K** on both.  
2. **Check PP sub-settings**:
   - Black Level = 0  
   - Black Gamma = 0  
   - Color Mode = Movie or ITU709  
   - Detail = 0  
   - Reset them if you’ve been tinkering.  
3. **Waveform Match** in your switcher/OBS:
   - Look at skin tones on both cameras.  
   - Nudge **ISO** by 1/3 stop on the darker cam to equalize brightness.  
   - Use your ATEM/OBS color correction wheels: warm up the cooler camera slightly (add a tick of red/orange in midtones).  
4. **Save It** as presets in your switcher, so you don’t have to fight this every time.

---

### Key takeaway
You’ve done everything right in-camera. At this point, what you’re seeing isn’t user error—it’s **FX30 vs FX3 color science**. The fix isn’t deeper menus, it’s finishing the match in your switcher.

Do you want me to lay out the **exact ATEM/OBS correction settings (lift, gamma, gain tweaks)** that people usually use to close the gap between FX30 and FX3? That way you can just dial them in once and save.

---



---

Perfect—you’ve reached the stage where the real fix happens: **matching in OBS with filters**.  

Looking at your shot:  

- **Preview (left / FX30)** → warmer, more magenta/red in the mids.  
- **Program (right / FX3)** → cooler, flatter, shadows a touch denser.  
- OBS filter panel is open, so you’re already tweaking Contrast / Brightness / Saturation. That’s the right move.

---

### How to Match Them in OBS
In OBS, for the “cooler” camera (FX3):
1. **Filters → Apply Color Correction**
   - **Contrast**: +0.05 to +0.10 (makes mids pop, closer to FX30 look).  
   - **Brightness**: leave at 0 unless it’s clearly under by more than ⅓ stop.  
   - **Gamma**: +0.05 to +0.10 (lifts midtones without blowing highlights).  
   - **Saturation**: +0.05 to +0.10 (skin looks more alive).  
   - **Hue Shift**: +2 to +3° toward red/orange if the image looks too cyan.  

2. **Check skin tones** – don’t obsess over the background, match your skin to look consistent across both cams.

3. **Save the filter preset** so every time that cam comes in, the correction is auto-applied.

---

### Pro Tip
- Always balance in-camera first (WB locked, same PP).  
- Then do **tiny corrections in OBS**. Treat this like color grading live.  
- Don’t push saturation too high—it’ll look fake fast. Small nudges work better than big swings.

---

So in short: you’re not crazy. Same PP doesn’t equal same color between FX3 and FX30. The only way to close the last 10% is **OBS filters or ATEM correction wheels**.  

Do you want me to give you a **ready-to-use OBS filter preset file** (JSON) that you can import and apply instantly to the cooler cam? That way you don’t have to eyeball all the sliders every session.