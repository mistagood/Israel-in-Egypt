# FX3 MacBook pairing steps



---



---

Right now I'm synced up to my iPhone, and I'm trying to get the monitor synced up to my camera through my MacBook. And so, how do I go to that setting in the FX3 to turn on pairing or remote use of the FX3 with the MacBook? I'm currently using it on the monitor control app on my iPhone, but I want to do the monitoring from my computer.

---



---



---

Got it — you’re trying to connect your **Sony FX3** to your MacBook for remote monitoring (instead of just using the iPhone monitor app). Right now, the “Remote” desktop app isn’t detecting the camera. That means the FX3 hasn’t been set to allow PC Remote / pairing. Here’s how to get to that setting on the FX3:

---

### Steps on the Sony FX3
1. **Turn on the Camera** and press the **Menu** button.  
2. Go to:  
   **Setup (wrench icon) → USB → USB Connection**  
   - Set this to **PC Remote** (not Mass Storage or MTP).  
3. In the same menu, also check:  
   **Setup → USB → PC Remote Settings**  
   - Make sure **Still Img. Ctrl / Movie Ctrl** is enabled.  
   - Leave connection method as **USB** if you’re going wired.  
4. If you want to use **Wi-Fi instead of USB**:  
   - Go to **Network → Wi-Fi → Access Point Set.**  
   - Turn **Control w/ Smartphone** ON (this is the same pairing your iPhone is using).  
   - For Mac, you’d need the **Imaging Edge Desktop** app (IEDT) to pair the same way.  

---

### On the MacBook
1. Make sure you’re running the latest version of **Imaging Edge Desktop**.  
2. Connect the FX3 via **USB-C to USB-C** or **USB-C to USB-A** (depending on your MacBook port).  
   - Avoid hubs if possible, plug directly into the Mac.  
3. Open **Imaging Edge Desktop → Remote**.  
   - Your FX3 should appear in the device list once “PC Remote” is enabled on the camera.  
4. If using Wi-Fi instead:  
   - The FX3 will generate a **QR code** in the Network → Smartphone Connect menu.  
   - You’ll need to pair your Mac with it in Imaging Edge Desktop → Remote.  

---

### Quick Troubleshooting
- If USB still doesn’t connect:  
  - Try a different cable (must be a **data-capable USB-C cable**, not a charge-only cable).  
  - Try switching **USB Power Supply → Off** in Setup, so it doesn’t conflict with powering.  
  - Restart both the camera and the Imaging Edge app.  

---

⚡ Question for you: Do you want to run the FX3 monitoring over **USB (wired, faster/stable)** or **Wi-Fi (wireless, same way your iPhone is doing it now)**? That’ll determine which exact pairing path you should follow.

---

Okay, so obviously I already have Control with Smartphone on, I guess because I'm using it on my phone. I just said that. And I want to use it Wi-Fi with the Imaging Edge Desktop Remote. How do I get the QR code? Because I need to pair these. Because that's what I asked you, how do I pair it in the beginning and why isn't it showing up in the list? That's the M's that I sent you and it's not showing up in the list.

---

Got it — thanks for clarifying. Since you’re already using **Control w/ Smartphone** on the FX3, what you now need is the **QR code (or SSID/password)** that allows **Imaging Edge Desktop (IEDT) on your Mac** to pair the same way your phone did. Here’s the step-by-step path on the **FX3**:

---

### On the FX3 (to get QR code / network info)
1. **Menu → Network → Wi-Fi → Connect to Smartphone.**
   - Select **Connect via QR Code**.  
   - The camera will display a **QR code** on the LCD screen.  

2. Normally this QR code is for pairing to the Sony **Imaging Edge Mobile app** (iOS/Android), but with **Imaging Edge Desktop** you’ll instead use the same **SSID and password** shown in the **Access Point Set.** or **Network Info.** screens.

3. If you don’t see the QR option, try:  
   **Menu → Network → Wi-Fi → Access Point Set. → Display SSID/Password.**

   - This will show the camera’s Wi-Fi hotspot name (SSID) and password.  
   - Your Mac must join that Wi-Fi network in order for IEDT Remote to see the camera.

---

### On your MacBook
1. Join the FX3’s Wi-Fi network (SSID/password from above).  
   - Go to **System Settings → Wi-Fi** and select the FX3 SSID.  
2. Open **Imaging Edge Desktop → Remote**.  
   - Click **Refresh**. The FX3 should now appear in the list.  
   - Double-click it to pair.  

---

✅ Why it’s not showing up in your screenshot:  
Right now, your MacBook is not on the **same Wi-Fi network** as the camera. That’s why Remote shows nothing. The iPhone app works because it already paired via QR and switched to that Wi-Fi connection. The Mac needs the same step.

---

Would you like me to give you the **exact FX3 menu path for “SSID/Password display”** so you can try connecting your Mac right away?