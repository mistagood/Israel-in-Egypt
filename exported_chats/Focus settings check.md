# Focus settings check



---



---

my focus settings . I'm not sure if its making face a priority. I just turned on s&q. It was just on the setting to the left (video). The focus was not following my face at all really. can you check these to see if it will work

---



---

I see your screenshot from the Sony FX3 remote panel — thanks, that helps. Let’s go through the focus settings you have active:

1. **Mode:**  
   - You’re in **S&Q Flexible Exp. Mode (Slow & Quick motion)**. This mode still allows AF, but sometimes face/eye AF tracking isn’t as sticky here as in normal movie mode.  
   - If you don’t *need* S&Q at that moment, switch back to the **video/movie mode icon** (the one just left of S&Q). That will give you the best and most predictable autofocus behavior for face/eye detection.

2. **Focus Area:**  
   - You currently have **Wide** selected. That means the camera tries to decide what to focus on across the whole frame. It may jump between you and the screens behind you.  
   - If you want it to prioritize your face, you should change this to **Face/Eye Priority in AF**. On the FX3, that’s usually under the *Focus → Face/Eye AF* setting. Once enabled, the focus box should lock onto your eyes when they are detected.  
   - If you want to force it even more, use **Zone** or **Flexible Spot** and place it over your face, with face/eye AF also enabled.

3. **AF-C vs AF-S:**  
   - You’re in **AF (Auto Focus)**, but check that it’s set to **AF-C (Continuous AF)** rather than AF-S. Continuous AF will track your face as you move; AF-S only grabs focus once and doesn’t follow.

4. **Eye/Face Priority Check:**  
   - On your screen, I don’t see the orange face box around your face. That means **Face/Eye AF is not turned on** right now. You’ll want to go into the **Focus menu → Face/Eye AF → On** and choose **Human Eye**.

---

✅ **What to do for reliable face focus:**  
- Switch from S&Q to **Movie mode** (unless you’re specifically doing slow/quick motion).  
- Set **Focus Area → Wide** *with* **Face/Eye AF Priority ON**.  
- Ensure **AF-C (Continuous AF)** is selected.  
- Double-check in the live view that the **orange box** tracks your eyes/face.  

Would you like me to give you the exact **menu path in the FX3 camera menu system** to turn on Face/Eye AF so it actually locks onto your face, not the background?

---

I did all this. I don't see the orange box either. How do I make sure that that is showing on my app, that it's actually showing those things? Should not be able to set that from the app, but it does seem to allow me.

---

Got it — thanks for clarifying. Yes, you’re right: with the **Sony Imaging Edge Remote app** (what you’re using on desktop), you should be able to both **turn on Face/Eye AF** and also **see the orange face/eye box** in live view when the camera detects you. If you don’t see it, that means either the feature isn’t enabled or the display of AF frames is turned off.

Here’s how to make sure it shows up:

---

### 1. Turn on Face/Eye AF (on camera or in app)
- In the **Remote panel**, look at the **Focus settings**.  
- Switch **AF-C** (continuous autofocus).  
- Then go into **Camera Settings 1 → AF/MF → Face/Eye AF → Face/Eye Priority in AF → ON**.  
- Under **Subject Detection → Human**.  
- For video: set **Eye Detection → Right/Left/Auto** (Auto is fine).  

⚡ On Imaging Edge Remote (your screenshot): there should be a toggle under **Focus → AF** for **Face/Eye Priority**. Sometimes it’s nested in the **AF Area / Face/Eye** sub-menu.

---

### 2. Make sure AF Frames are displayed
- On the FX3 body: **Menu → Setup (wrench) → Display Option → Display AF Frame → ON**.  
- If this is OFF, you won’t see the orange box even if Face AF is working.  

---

### 3. Verify it in Imaging Edge Remote
- In Live View, when Face/Eye AF is active, you should see **white boxes** searching and then **orange box around your face/eye** once locked.  
- If you don’t, try:
  - Toggle **Focus Area** from Wide → Flexible Spot → back to Wide (resets detection).  
  - Step closer to the camera or increase light — sometimes ISO noise reduces detection.  

---

### Quick test
1. Put the camera back to **Movie mode** (not S&Q).  
2. Set **AF-C + Wide + Face/Eye Priority = ON**.  
3. Look at the live view in the Remote app.  
   - If everything is working, you should see the orange box track your face.  
   - If you don’t, double-check **Display AF Frame** setting.  

---

👉 Do you want me to write you the **step-by-step Imaging Edge Remote clicks** (with the exact panel names in the desktop app) so you can confirm Face/Eye Priority is actually on from there, instead of only relying on the camera body?

---

I did all that, checked everything, but it still doesn't display. Neither the white squares or the orange ones display on the imaging edge remote program. Does the imaging edge allow for this to display? You have to check the specifications.

---



---

You're absolutely right to question whether Imaging Edge Remote supports displaying face/eye AF frames—which is critical to troubleshooting your focus issues. Here's what the official specifications say, especially regarding the Sony FX3:

---

###  Does Imaging Edge Desktop (Remote) show AF frames?

From Sony’s official documentation:
- The **AF area frame** in Live View *only* appears in Imaging Edge Remote when using **Flexible Spot** (or Expand Flexible Spot), and *only* if that option is supported by your camera. If you're using **Wide** focus area, the focusing frame doesn't appear at all in the remote interface—even though it works on the camera itself citeturn0search0.

So, if you rely on Wide AF in Remote mode, you won't see any AF frame—even if Face/Eye AF is enabled and working.

---

###  What about Face/Eye detection frames?

On the FX3 itself, you can control the display of face/eye detection frames via this menu:
> MENU → (Focus) → **Face/Eye AF** → **Face/Eye Frame Disp.** → **On** or **Off** citeturn0search5.

- **On**: detection frames appear when the camera detects a face or eye.
- **Off**: frames are suppressed—even if detection is working.

Important note: This setting only affects the camera's **built-in monitor / EVF**, not the remote view in Imaging Edge.

---

###  Summary Table

| Feature                         | Camera Display | Imaging Edge Remote |
|----------------------------------|----------------|----------------------|
| AF frames (Flexible Spot)        | Yes            | Yes                  |
| AF frames (Wide AF)              | Yes            | **No**               |
| Face/Eye detection frames        | Yes (if enabled) | **No**             |

---

###  What this means for you:

- If you're using **Wide AF** (even with Face/Eye Priority), the remote app will **not** show any detection frames—white or orange.
- The **face/eye detection frame** setting on the camera applies only to the camera's display, not to Imaging Edge.

---

###  What you can do:

1. **Enable AF area Flexible Spot** while using Remote mode—this will at least show a focusing frame you can reposition.
2. **Use the camera’s monitor** to visually confirm that Face/Eye AF is actually tracking (look for the white/gray/white-to-orange frames).
3. **Rest assured**, even if the remote preview doesn't show it, Face/Eye AF can still be active and tracking.

---

### TL;DR:
The Imaging Edge Desktop remote interface **does not display face or eye detection frames** when using Wide AF. That behavior is by design—not a bug. You're not missing any hidden setting!

Would you like a quick suggestion on how to best test Face/Eye AF using Flexible Spot in Remote to at least get something visible?

---

this little square is all imm getting. it doesnt track the eyes. 

---

Thanks for showing me the second screenshot — that clears it up.  

What you’re seeing (the **orange square**) is the **Expand Spot AF frame**. That is the only type of AF box Imaging Edge Remote will actually display. It does **not** show face or eye detection frames (white/orange boxes around your eyes) even when Face/Eye AF is working on the FX3 body.  

So:  

- ✅ **This is expected behavior.** Imaging Edge Remote will only show **spot/zone AF frames**.  
- ❌ It does **not** overlay the face/eye detection boxes on the desktop app. That’s why you’re not seeing the orange eye-tracking box.  

---

### Why you only see the small square
- In your screenshot you’ve selected **Focus Area: Expand Spot**.  
- That box is simply the focus target area you can move manually.  
- The app cannot display the face/eye AF overlays — those only appear on the camera’s LCD/HDMI output.  

---

### Bottom line
- **On the app:** you’ll only ever see the spot/zone AF box (what you’re seeing now).  
- **On the camera monitor/HDMI out:** you’ll see the face/eye detection boxes if Face/Eye AF is enabled.  

So if you want to visually confirm face/eye AF tracking, you’ll need to check the **camera’s built-in screen or an HDMI monitor**, not Imaging Edge Remote.  

---

👉 Do you want me to show you how to keep Imaging Edge Remote running *and at the same time* monitor the FX3’s HDMI out (so you can see the face/eye AF box live while controlling from the app)? That’s the usual workaround.