# iPhone 15 mic issue



---



---

iPhone 15 is not picking up the rode 2 wireless as a microphone. How do I get it to read this device?

---



---



---

If your iPhone 15 is not recognizing the **RØDE Wireless GO II** as a microphone, try the following step-by-step troubleshooting guide:

---

### ✅ 1. **Check the Connection Type**
The iPhone 15 has a **USB-C port**, not Lightning. So make sure:

- You are using the **RØDE SC15** (Lightning to USB-C) **or** the **RØDE SC21** (USB-C to USB-C), depending on your system.
- If using the **Wireless GO II**, make sure the **receiver** (RX unit) is connected via:
  - **USB-C to USB-C cable** directly to your iPhone 15 (use RØDE's supplied cable or a verified data-capable USB-C cable).
  - Avoid 3.5mm TRS unless you are using a certified adapter like the **RØDE AI-Micro**.

---

### ✅ 2. **Enable USB Audio on the Receiver**
Sometimes the receiver does not default to USB audio. To fix this:

- Connect the receiver to your computer.
- Open **RØDE Central**.
- Make sure **USB Audio is enabled**.
- You may also enable “Merged” mode to combine both transmitters into one audio stream (if using both).

---

### ✅ 3. **Check iPhone Settings**
iPhones do not have manual audio input settings. Instead:

- Open the **Camera app** or **Voice Memos**.
- Plug in the receiver.
- Start a video or audio recording.
- Speak into the lav mic.
- Playback the recording—**if the mic was detected**, you’ll hear clean lav audio (not iPhone mic).

If it still uses the internal mic, the receiver is **not being recognized as a USB audio input**.

---

### ✅ 4. **Try a Compatible App**
Some apps do not recognize external mics well. Use apps that **do** support external audio:

- **RØDE Reporter** app
- **Filmic Pro**
- **Voice Record Pro**
- **LumaFusion** (for video editing and capture)
  
These apps let you **select the input device** and monitor signal.

---

### ✅ 5. **Firmware Update**
Use **RØDE Central** (Mac/PC) to update:

- The receiver
- The transmitters

Outdated firmware can prevent correct handshake with newer devices like the iPhone 15.

---

### ✅ 6. **Try Another USB-C Cable**
Some cables only charge, not transfer audio/data. Make sure:

- The cable is **USB 2.0 or higher with data support**.
- Preferably use the **original cable that came with the Wireless GO II**, or the **RØDE SC21**.

---

### ✅ 7. **Power & Battery Check**
If the receiver isn’t powering up when connected to iPhone:

- Charge the receiver fully.
- Try powering it on **before** connecting.
- Avoid using low-power modes on your iPhone.

---

### ✅ Final Tip: Reset Your iPhone (if nothing works)
- Restart your iPhone.
- Try another recording app.
- Plug in the receiver **after** the app is open.

---

If you've tried all the above and it's still not working, let me know what exact setup (e.g., cable used, app, mic mode) you're using and I can help debug further.

---

I'm not using it USB, I'm using it through 3.5 adapter to the iPhone. I asked how do I make it read this device

---

Thanks — that’s key. Since you're using the **RØDE Wireless GO II** via **3.5mm** into an iPhone 15 (which uses **USB-C**), here’s the core issue:

> **The iPhone does not recognize analog microphones through most 3.5mm-to-USB-C adapters.**

### 🔧 The Problem:
iPhone 15 **does not have a dedicated analog mic input** like older iPhones with headphone jacks or even Lightning ports. Most USB-C to 3.5mm adapters (including Apple’s own) **only support audio output**, not microphone input — unless the adapter has **TRRS mic support with ADC (analog-to-digital conversion)**.

---

### ✅ The Fix: Use a TRRS-Compatible Interface

To get your **RØDE Wireless GO II (via 3.5mm)** working with iPhone 15, you need **one of the following**:

#### **Option 1: Use the RØDE AI-Micro**
- The [**RØDE AI-Micro**](https://www.rode.com/interfaces/aimicro) is a **dedicated mobile interface** that supports **TRS/3.5mm mic input**, and converts it to digital USB-C for iPhones.
- Just plug the Wireless GO II receiver’s **3.5mm TRS cable** into one of AI-Micro's inputs, then plug AI-Micro into your iPhone with the supplied **USB-C cable**.
- ✅ **Guaranteed to work with iPhone 15.**
- 🎧 Also supports **monitoring with headphones**.

#### **Option 2: Use RØDE SC4 + SC15/SC21 (not reliable on iPhone 15)**
- SC4 converts TRS (mic) to TRRS (iPhone).
- But iPhone 15 doesn't have a TRRS analog input anymore — so this combo **only works** with some **powered Lightning ports**, not USB-C.

🛑 **In short:** your analog 3.5mm cable won’t work directly with USB-C unless you're using a **proper mic interface like AI-Micro**.

---

### 🚫 What Doesn’t Work
- ❌ Generic 3.5mm to USB-C adapters (they’re often output-only)
- ❌ Apple USB-C to 3.5mm adapter (only supports headphone audio)
- ❌ Dongles that lack ADC (analog-to-digital conversion)

---

### Summary
You need to **convert the analog mic signal** into **USB-C digital audio** that iPhone 15 can understand. Use:

- ✅ **RØDE AI-Micro** (best option)
- OR
- ✅ Go direct with a **USB-C cable from the Wireless GO II receiver to iPhone** (bypasses 3.5mm entirely)

Would you like links or wiring diagrams for either method?

---

My bad, it's iPhone 14 Pro Max. iPhone 14 Pro Max.

---

Ah—thank you! That changes everything. The **iPhone 14 Pro Max uses a Lightning port**, not USB-C.

So if you're connecting the **RØDE Wireless GO II** receiver via **3.5mm analog**, here's how to **make it work as a microphone input**:

---

## ✅ How to Get iPhone 14 Pro Max to Read the RØDE Wireless GO II via 3.5mm

### 🔌 Required Equipment:

1. **Apple Lightning to 3.5mm Headphone Jack Adapter**  
   - [This one](https://www.apple.com/shop/product/MMX62AM/A/lightning-to-35-mm-headphone-jack-adapter)
   - ⚠️ *Must be the genuine Apple adapter* — many third-party versions do **not** pass mic input.

2. **RØDE SC7 Cable** (TRS to TRRS)  
   - Converts your RØDE receiver’s **TRS (3.5mm)** output to **TRRS**, which the iPhone adapter expects for mic input.  
   - [SC7](https://www.rode.com/cables/sc7) has **black plug (TRS)** on one end and **gray plug (TRRS)** on the other.  
   - Plug the **black end into the RØDE receiver**, and the **gray end into the Lightning adapter**.

---

## 🎤 Step-by-Step Setup:

1. **Connect the SC7 cable**:
   - Black plug → Wireless GO II receiver’s **3.5mm out**  
   - Gray plug → Apple Lightning to 3.5mm adapter

2. **Connect the Lightning adapter to your iPhone**

3. **Open a recording app** (Camera, Voice Memos, etc.)

4. **Test recording**:
   - Speak into the Wireless GO II transmitter
   - Playback your video or audio — if it sounds clean and close, the iPhone **read the mic input** successfully

---

## 🔎 How to Verify It’s Working

- In **Camera app** (Video mode), start recording.
- Speak only into the Wireless GO mic.
- Playback the video:
  - If it sounds distant, it used the iPhone mic.
  - If it sounds clean and close, it's using the RØDE system.

📌 *There’s no visual confirmation in iOS, but apps like “Voice Record Pro” or “Filmic Pro” may show input level meters.*

---

## ❗ Common Issues to Avoid

| Problem | Cause | Fix |
|--------|--------|-----|
| 🎤 iPhone uses internal mic | Wrong cable type (TRS instead of TRRS) | Use **SC7** |
| 🔇 No sound at all | Faulty or non-Apple adapter | Use **genuine Apple Lightning adapter** |
| 🎧 Echo or feedback | Trying to monitor without split | Use a **splitter** if you want headphones too |

---

## ✅ Optional Monitoring Setup

If you want to **monitor** audio while recording:
- Use a **Lightning splitter** (Mic + Headphone)
- Or use **RØDE AI-Micro**, which supports both mic input and monitoring

---

## Summary

To use the **RØDE Wireless GO II** with iPhone 14 Pro Max via 3.5mm:

- ✅ Use **RØDE SC7 cable** (TRS to TRRS)
- ✅ Use **Apple Lightning to 3.5mm adapter**
- ✅ Plug into camera or recording app and test

Let me know if you'd like a diagram, Amazon/Apple Store links, or recommendations for apps that show input meters.

---



---



---

Thank you — the photos are **very helpful**.

You're almost there, but there's **one small issue** with the current setup that's likely preventing the iPhone 14 Pro Max from detecting your **RØDE Wireless GO II** mic.

---

### 📸 What I See in Your Setup:
- You're using a **RØDE red cable** — that's the standard **TRS-to-TRS cable** (both ends have **2 black rings**) — this is meant for **cameras**, **not phones**.
- You're plugging that into a **Lightning to 3.5mm adapter** (appears to be the official Apple one — good).
  
---

### 🚫 Why It’s Not Working:
iPhones require a **TRRS** microphone input (3 black rings) for analog audio through the Lightning port.

> But the red RØDE cable (TRS-to-TRS) **cannot carry mic input** into the iPhone Lightning adapter — it's missing the correct wiring format.

---

### ✅ What You Need to Do Instead:

Replace that red cable with the **RØDE SC7 cable**:

| ✅ Correct Cable | ❌ Your Current Cable |
|------------------|------------------------|
| **RØDE SC7** – TRS to TRRS | RØDE Red TRS to TRS |
| One black plug (TRS) → receiver | Both plugs are black (TRS to TRS) |
| One gray plug (TRRS) → iPhone Lightning adapter | Won’t work for mic input |

---

### 🔌 Correct Setup:
1. Plug **black end of SC7** into the **RØDE Wireless GO II receiver**.
2. Plug **gray end of SC7** into the **Apple Lightning to 3.5mm adapter**.
3. Plug the **Lightning adapter into your iPhone 14 Pro Max**.
4. Open the **Camera app (video)** or **Voice Memos** and test.

---

### 🎧 Bonus Tip (Testing Mic Input):
- Record a test video.
- Scratch the mic on the Wireless GO II and see if the sound is loud/close.
- If it sounds far away, it's still using the internal iPhone mic.

---

### ✅ Where to Get the SC7 Cable:
- [Amazon - RØDE SC7](https://www.amazon.com/dp/B00L6C8PNU)
- [RØDE official site](https://www.rode.com/cables/sc7)

This should solve your issue completely. Let me know if you'd like a visual wiring diagram for confirmation.

---

That link doesn't even have the right kinds of adapters on it. How am I supposed to use that? I'm using a real wireless Go 2. It doesn't have a cord.

---

Got it — thank you for the clarification. You're using the **RØDE Wireless GO II** system, **wirelessly** from the transmitter, but trying to connect the **receiver** into the iPhone 14 Pro Max through 3.5mm analog.

And yes — you're absolutely right: the **receiver has no cord** permanently attached — you connect a 3.5mm TRS cable **from the receiver's output jack** into your phone via adapters.

Let me now give you the **exact, correct solution** based on your setup.

---

## 🔧 The Problem with Your Current Setup:
From your photo and setup, you're using the **red TRS–TRS cable** that came with the RØDE Wireless GO II. That's the **wrong cable for smartphones**.

Here’s why:

| TRS (2 rings) | TRRS (3 rings) |
|--------------|----------------|
| 🎥 For cameras | 📱 For phones |
| No mic input on phones | Mic input recognized by iPhone |
| Your red cable | You need SC7 (gray+black ends) |

The **Apple Lightning to 3.5mm adapter** requires **TRRS**, not TRS.

---

## ✅ What You Need

You just need **one specific cable** to fix this:

### 🎯 **RØDE SC7 – TRS to TRRS Patch Cable**
- **Black plug** (TRS) → goes into the **Wireless GO II receiver**
- **Gray plug** (TRRS) → goes into the **Apple Lightning to 3.5mm adapter**
- Then plug that into your iPhone.

🔗 Here is the correct link:
👉 [RØDE SC7 Official Product Page](https://www.rode.com/cables/sc7)  
👉 [RØDE SC7 on Amazon (correct one)](https://www.amazon.com/dp/B00L6C8PNU)

![Rode SC7](https://cdn.rode.com/cables/sc7/sc7-product.jpg)

---

## 🔁 Summary Setup Chain

1. 🎤 **Wireless GO II Receiver**
2. 🔌 **Black end of SC7 cable** → into 3.5mm jack on receiver
3. 🔌 **Gray end of SC7 cable** → into **Apple Lightning-to-3.5mm adapter**
4. 🔌 **Apple adapter** → into iPhone Lightning port

That’s it. Once this is connected:

- The iPhone **will detect the mic**
- You can record in **Camera**, **Voice Memos**, or any app that uses external audio
- You don’t need to “select” it — iOS auto-switches to external mic if wiring is correct

---

Let me know if you want me to confirm which cable you're currently using from a photo — happy to double-check.

---

can it use the lightning

---



---

Yes — the **RØDE Wireless GO II** can absolutely connect **directly via Lightning** to your **iPhone 14 Pro Max**, **bypassing the 3.5mm cable completely**. This is actually the **cleanest, most reliable method**.

---

## ✅ OPTION: Direct Lightning Connection (Digital Audio)

### What You Need:
1. **RØDE SC15** cable  
   🔗 [RØDE SC15 product page](https://www.rode.com/cables/sc15)  
   - USB-C (goes into the receiver) → Lightning (goes into iPhone)  
   - **MFi-certified**, made specifically for iPhone/iPad Lightning ports  
   - Transfers **digital audio**, not analog (cleaner signal)

---

### 🎯 Setup Instructions:

1. Plug the **USB-C end** of the **SC15** into the **Wireless GO II receiver**.
2. Plug the **Lightning end** into your **iPhone 14 Pro Max**.
3. That’s it — iOS will automatically switch to digital external mic.

> 🎥 Works perfectly in:
> - Camera app (Video mode)
> - Voice Memos
> - Filmic Pro / LumaFusion / Voice Record Pro

---

## 🔍 How to Tell It’s Working:

- Do a test video in the Camera app.
- Scratch or tap the RØDE transmitter mic.
- Playback the video — if it sounds clean and close, it worked.
- You won’t see a mic icon, but the system uses the digital mic when detected.

---

## ⚠️ Important Notes:

- The **SC15** only works with **Lightning iPhones** (like yours)  
- The **Wireless GO II receiver must be updated via RØDE Central** to latest firmware for full compatibility  
- It draws power from the iPhone — no battery needed on receiver

---

## ✅ Why This Is Better Than 3.5mm

| Feature              | 3.5mm Analog | SC15 Lightning |
|----------------------|---------------|----------------|
| Plug-and-play        | ❌ Needs TRRS | ✅ Yes |
| Audio quality        | Analog signal | **Digital (clean)** |
| Adapter needed       | Yes (Apple + SC7) | **No** |
| Works with Lightning | ⚠️ Only with proper adapters | ✅ Native |
| App compatibility    | Varies        | **Universal** |

---

## 🔗 Buy SC15:
- [RØDE SC15 on Amazon](https://www.amazon.com/dp/B08V8MWVJZ)
- [B&H Photo](https://www.bhphotovideo.com/c/product/1611796-REG/rode_sc15_usb_c_to_lightning.html)

---

Let me know if you want to see a visual of the SC15 cable in use or compare it to your current adapter. This is the **best way** to use the Wireless GO II with iPhone 14 Pro Max — no adapters, no analog confusion.

---

Will beats usbc to lightning cable work

---



---



---

No — a **Beats USB-C to Lightning cable will NOT work** to connect your **RØDE Wireless GO II** receiver to your **iPhone 14 Pro Max** for microphone input.

---

### ❌ Why the Beats Cable Won’t Work

1. **It’s a charging/audio cable for Beats products only**  
   - It's designed to **charge** Beats headphones or transmit **audio output**, **not microphone input**.

2. **It does NOT support USB audio from external microphones**  
   - The RØDE Wireless GO II sends **digital audio** over USB-C.
   - The Beats cable is **not MFi-certified for mic data transfer**, and **iOS will not recognize the RØDE receiver through it**.

3. **Apple devices require a specific MFi-certified cable** for digital microphone input through Lightning.  
   - The **SC15** is designed by RØDE **specifically for this**.

---

### ✅ What You Actually Need:
You need the **RØDE SC15**, which is:
- ✅ USB-C (male) → Lightning (male)
- ✅ MFi-certified (Made for iPhone)
- ✅ Carries **digital audio** into iPhone
- ✅ Designed specifically for use with **RØDE Wireless GO II receiver**

🔗 [RØDE SC15 official page](https://www.rode.com/cables/sc15)

---

### ⚠️ Bottom Line:

| Cable Type                  | Works with Wireless GO II + iPhone? |
|----------------------------|--------------------------------------|
| **RØDE SC15 (Lightning)**  | ✅ YES (official and supported)       |
| Beats USB-C to Lightning   | ❌ NO (charging/audio only)          |
| Generic USB-C to Lightning | ❌ NO (not MFi mic-compatible)        |

---

Let me know if you want help confirming you’re ordering the right cable. I can match it to your gear.

---

What are alternative cables 

---

Here are the **only proper alternatives** to the **RØDE SC15** for connecting your **RØDE Wireless GO II** receiver to your **iPhone 14 Pro Max** (Lightning port) — all support **digital microphone input**, not just charging or audio output.

---

## ✅ 1. **RØDE SC15 (Official Cable)**  
- **USB-C (receiver)** → **Lightning (iPhone)**  
- **MFi-certified** (Made for iPhone)
- Direct, plug-and-play, **no adapters needed**
- ✔️ Best and most stable option  
- 🔗 [SC15 on RØDE.com](https://www.rode.com/cables/sc15)

---

## ✅ 2. **RØDE SC19**
- **Longer version** of the SC15 (1.5 meters)
- Same function: **USB-C to Lightning**
- MFi-certified, works identically
- Great if you need extra reach

---

## ✅ 3. **Apple Lightning to USB 3 Camera Adapter** + **USB-C to A female adapter**
- This is a more **modular but clunky setup**, and more prone to power issues
- Parts:
  - Apple **Lightning to USB 3 Camera Adapter** (w/ charging passthrough)
  - USB-A to USB-C adapter (to plug in your Wireless GO II receiver)
- Plug Lightning adapter into iPhone  
- Plug Wireless GO II into USB port using USB-C to USB-A adapter

> ⚠️ This setup **requires external power** (plug into the Lightning port on the adapter), or iPhone may **not supply enough power** to the RØDE receiver.

🔗 [Apple Lightning to USB 3 Camera Adapter](https://www.apple.com/shop/product/MK0W2AM/A/lightning-to-usb-3-camera-adapter)

---

## ❌ What **Won’t Work** as Alternatives:

| Cable Type                          | Works? | Reason |
|------------------------------------|--------|--------|
| Beats USB-C to Lightning           | ❌     | Not for mic input |
| Generic USB-C to Lightning         | ❌     | No MFi mic support |
| USB-C charging cables              | ❌     | Power only, no audio |
| Lightning to headphone adapters    | ❌     | Analog only, not USB digital |

---

## 🔄 Summary of Working Alternatives:

| Cable/Adapter                 | Connection Type                | Notes                            |
|------------------------------|-------------------------------|----------------------------------|
| **SC15**                     | USB-C to Lightning             | Best direct solution             |
| **SC19**                     | USB-C to Lightning (longer)    | Same as SC15, just longer        |
| **Apple USB 3 Camera Adapter** + USB-C adapter | Lightning to USB-A + USB-C         | Requires external power          |

---

Let me know what you're trying to accomplish (video, podcast, mobile rig), and I can tell you which is best for your workflow.

---

does the rode receiver have audio out jack

---



---



---



---

Yes — the **RØDE Wireless GO II receiver** does indeed have a **3.5mm audio output jack**, located on the **top edge** of the unit. Here's how it works and what you can do with it:

---

## 🎧 RØDE Wireless GO II – Audio Out Jack (3.5mm)

### 🔌 Port Details:
- The jack is labeled with a **headphone icon** or sometimes just “OUT”.
- It is a **3.5mm TRS analog output** (standard for cameras and recorders).
- It outputs a **mixed mono** or **stereo signal** depending on settings.
- This jack is **not a headphone jack** — it’s a **line-out**, meant to go into:
  - DSLR/mirrorless cameras
  - Audio recorders
  - Computers (with mic-in)
  - Smartphones (with proper adapters)

---

### 🔧 Use Cases for the Audio Out Jack

| Device           | Cable Needed                           | Notes |
|------------------|-----------------------------------------|-------|
| DSLR/Camera      | Red TRS–TRS cable (included)            | ✅ Plug and go |
| Smartphone (Lightning) | RØDE SC7 (TRS to TRRS) + Apple Lightning adapter | ✅ Allows mic input |
| iPhone (Digital) | Skip analog — use RØDE SC15 (USB-C → Lightning) | ✅ Cleaner, direct digital |
| Audio Recorder   | TRS–TRS or TRS–XLR depending on input   | ✅ Use manual gain |
| Computer (analog) | TRS to TRS or TRRS adapter if combo jack | ✅ Mic input |

---

### ⚙️ Output Settings via RØDE Central
You can configure the output behavior using **RØDE Central** app:

- **Merged mode**: Combines both transmitters into one mono channel
- **Split mode**: Sends each transmitter to Left and Right channels
- **Pad output**: Lowers signal level if needed (to avoid clipping)

---

### 🔍 Summary:

- ✅ Yes, the **receiver has a 3.5mm audio out jack**
- 🛠️ It requires the **correct cable** for the device you're sending it to
- 🔄 For iPhones: use **SC7 (analog)** or **SC15 (digital via Lightning)**

Let me know which cable or function you're planning to use the output for — I can tell you exactly what cable to grab based on your setup.

---

going to the apollo x

---

Great — if you’re connecting the **RØDE Wireless GO II receiver** to your **Apollo Twin X** (or any **Apollo X interface**) to record directly into your DAW or route via Console, here’s how to do it properly:

---

## 🎧 Goal: Feed RØDE Wireless GO II into Apollo Twin X

You’ll be using the **3.5mm audio out jack** on the **Wireless GO II receiver** to feed audio into your Apollo — which accepts **¼" TRS or XLR** inputs.

---

### ✅ Option 1: Use 3.5mm TRS to Dual ¼” TS Y-Cable (Recommended for Line Input)

| Cable Needed | Example Product |
|--------------|------------------|
| **3.5mm TRS (male) → Dual ¼" TS (male)** | [Hosa CMP-159](https://www.hosatech.com/products/analog-audio/stereo-breakouts/cmp-159/) (3.5mm to dual ¼”) |

#### Setup:
- Plug **3.5mm TRS** end into **RØDE receiver output**
- Plug **Left and Right ¼” TS** plugs into **Apollo's line inputs (1 & 2)**
- On Apollo Console, set those channels to **LINE** (not mic or Hi-Z)
- Pan the two channels hard left/right if using split mode (or center both for merged)

> 🎚️ **Gain Tip**: The Wireless GO II outputs a hot signal — start with Apollo line gain low and adjust.

---

### ✅ Option 2: Use 3.5mm TRS to Single ¼" TRS Cable (For Mono/Merged Mode)

| Cable Needed | Example |
|--------------|--------|
| **3.5mm TRS → ¼” TRS** (male to male) | Hosa HMR-003Y or similar |

- Use this only if you are in **Merged Mode** on the RØDE (both mics into one signal)
- Plug into **Channel 1 Line In** on the Apollo
- Set input to **LINE**, not Mic or Hi-Z
- Monitor signal via Apollo Console

---

### ⚠️ Important Notes:

| Setting | Tip |
|--------|-----|
| **Merged Mode** | Combines both mics to one channel — ideal for single ¼" input |
| **Split Mode** | Sends TX1 to Left, TX2 to Right — use stereo cable or Y-cable |
| **Pad Output** | Enable -6dB pad in RØDE Central if input is too hot |
| **Phantom Power** | **DO NOT enable** phantom power on Apollo inputs — it's not needed and may cause issues |
| **Monitoring** | Use Apollo Console to route to headphones or DAW as needed |

---

### 🎚️ Optional Enhancements:
- Use **RØDE Central** on your Mac to:
  - Set **merged vs split** audio
  - Apply **pad**
  - Enable **safety track** (dual gain recording, if needed for cameras)
- Save your settings before unplugging USB

---

## ✅ Summary Wiring Diagram

```
[RØDE Wireless GO II Receiver]
         │
     3.5mm TRS
         │
     (Y-split)
         ├── ¼" TS → Apollo Line Input 1 (L)
         └── ¼" TS → Apollo Line Input 2 (R)
```

**OR**

```
[RØDE Wireless GO II Receiver]
         │
     3.5mm TRS
         │
    → ¼" TRS (mono)
         ↓
  Apollo Line Input 1
```

---

Let me know which cable type you already have or if you want recommendations from B&H, Amazon, or Sweetwater. I can match you with a high-quality cable that’ll fit your studio exactly.