# OBS virtual camera setup



---



---



---

how do i use virtual cam (from obs) for facebook messenger. it keep defaulting to the camlink 4k when I want the feed from OBS virtual canera

---



---



---

Here’s how to get **OBS Virtual Camera** working with **Facebook Messenger** when it keeps defaulting to your **CamLink 4K**:

---

### 1. **Start the OBS Virtual Camera**
- Open OBS.
- Click **Start Virtual Camera** in the lower-right controls area.
- Make sure your CamLink feed (or other video sources) are visible in your OBS preview window—whatever you see there is what Messenger will receive.

---

### 2. **Select the Right Camera in Messenger**
Messenger runs in two main contexts, so check both if needed:

#### **A. On the Web (messenger.com or facebook.com/messages)**
1. Join or start a video call.
2. In the call window, click the **gear ⚙️ icon** (Settings) or **three dots (…)** menu.
3. Under **Camera**, select **OBS Virtual Camera** from the dropdown.
4. If it keeps defaulting to CamLink 4K:
   - Disconnect CamLink temporarily.
   - Refresh the browser (Ctrl + R or ⌘ + R).
   - Choose **OBS Virtual Camera** again.
   - Reconnect CamLink afterward.

> **Tip:** Browser permissions sometimes “lock” the first camera it detects. You can reset permissions:
   - In Chrome: go to `chrome://settings/content/camera`
   - Remove Facebook/Messenger from “Allowed”
   - Rejoin your call and re-select OBS Virtual Camera.

---

#### **B. In the Facebook Messenger Desktop App (Mac or Windows)**
1. Open **Settings > Audio/Video** (from the menu bar or profile icon).
2. Choose **OBS Virtual Camera** from the Camera dropdown.
3. If it doesn’t appear:
   - Quit Messenger.
   - Relaunch **OBS**, start the Virtual Camera first.
   - Then reopen Messenger.
   - macOS users may need to **grant OBS camera access**:  
     System Settings → Privacy & Security → Camera → Toggle on OBS.

---

### 3. **Confirm OBS Virtual Camera Is Active**
On macOS, open **FaceTime** or **Photo Booth** — if those apps show the OBS output when you select “OBS Virtual Camera,” the virtual device is working correctly.  
If not:
- Reinstall **OBS VirtualCam driver** (OBS > Tools > VirtualCam > Install).
- Restart your Mac/PC after reinstall.

---

### 4. **Troubleshooting**
- **Messenger uses the wrong camera after restart**: unplug CamLink or disable it in Device Manager (Windows) or System Settings (Mac) before opening Messenger.
- **OBS Virtual Camera not listed**: reinstall the plugin or update OBS to version > 27 (it’s built-in after that).
- **Black screen feed**: ensure there’s at least one active scene/source visible in OBS.

---

If you want to make OBS VirtualCam always appear *first* so Messenger picks it by default, I can walk you through changing the camera order in macOS or Windows—different methods exist for each system.