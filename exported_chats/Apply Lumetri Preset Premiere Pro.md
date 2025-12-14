# Apply Lumetri Preset Premiere Pro



---



---

How do I apply a preset in Premiere Pro? It's Adobe Premiere Pro 25 that I'm using. But I saved the preset of a Lumetri color and now I'm trying to apply that on another clip and I can't see anywhere that lets you or how do you get to the presets.

---



---



---

To apply a **Lumetri Color preset** in **Adobe Premiere Pro 2025**, follow these steps:

---

### 🟩 Step 1: Locate Your Saved Preset
Your saved Lumetri preset should be in the **Effects** panel:

1. Go to the **Effects** panel.
   - If it’s not visible, enable it via `Window > Effects`.

2. In the **Effects** panel, open the **Presets** folder.
   - Your saved Lumetri preset should be listed by the name you gave it.

---

### 🟦 Step 2: Apply the Preset to a New Clip

You have **two main ways** to apply it:

#### 🔹 Drag-and-Drop Method
1. **Drag the preset** from the *Effects > Presets* panel.
2. **Drop it** onto the clip in the **Timeline** or **Program Monitor**.

#### 🔹 Apply via the Effect Controls Panel
1. Select your **new clip** in the timeline.
2. Go to the **Effects** panel.
3. Drag the preset onto the **clip** (as above).
4. Then open the **Effect Controls** panel to tweak the Lumetri settings if needed.

---

### 🟨 Step 3: Confirm It Worked

- Go to the **Effect Controls** panel with the clip selected.
- You should see a **Lumetri Color** effect listed.
- Expand it to see your preset settings already applied.

---

### 📝 Notes

- If your preset doesn’t appear, confirm that it was saved correctly:
  - You can save a Lumetri preset by right-clicking the **Lumetri Color** effect in the **Effect Controls panel** and selecting **Save Preset**.
  - Give it a name and description.

- Presets are stored in your user folder, so if you changed machines or cleared cache, it may not appear unless exported and re-imported.

---

Would you like help organizing a set of custom looks across a project, or exporting presets to share?

---

How do I create a new text layer? I want to copy in some text from the Bible and have it scroll up the screen because it's going to be too much for one screen. But I want to have it scrolling up the screen so that I can call out parts of it as I go.

---



---

To create a **scrolling text layer** in **Adobe Premiere Pro 2025**, here's a step-by-step method to paste in Bible text and make it **scroll upward smoothly**, perfect for teaching or callouts.

---

## 🟫 STEP 1: Create the Text Layer

1. **Select the Type Tool (T)**  
   - Or go to `Graphics > New Layer > Text`.

2. **Click in the Program Monitor** to create the text layer.
3. In the **Essential Graphics Panel**, paste in your Bible passage.

   - If the panel isn’t visible, go to `Window > Essential Graphics`.
   - You can **copy-paste directly** from your source text (e.g., BibleGateway, BlueLetterBible, or your own doc).

---

## 🟨 STEP 2: Style Your Text

- Adjust **font**, **size**, **line spacing**, **color**, and **alignment**.
- For long passages, make the text box tall/narrow to simulate a scroll look.

⚠️ Important: 
- Don’t worry if the text goes off-screen — that’s expected. You’ll animate it next.

---

## 🟥 STEP 3: Animate the Scroll

### 🧭 Option A: Keyframe Position (Recommended for smooth control)

1. Go to the **Effect Controls** panel.
2. Under the **Text layer**, find **"Position"**.

3. Move the playhead to the **start** of the clip.
   - Click the **stopwatch** next to Position to set your **first keyframe**.
   - Drag the **text below the frame** (Y value increased).

4. Move the playhead to the **end** of the clip.
   - Drag the text **up above the top edge** of the frame (Y value decreased).
   - This sets your **second keyframe**.

5. Play it back to see the **scrolling effect**.

💡 You can adjust speed by:
- Making the clip longer = slower scroll
- Shorter = faster scroll

---

### 🟦 Option B: Use a Graphic Roll (Optional Method)

1. Instead of text, go to `File > New > Legacy Title`.
2. In the Legacy Title window:
   - Click the **Roll/Crawl Options** (bottom toolbar).
   - Choose **"Roll"** (starts at bottom, scrolls up).
   - Paste your text into the title.
   - Save and exit.

3. Place the legacy title on the timeline like a clip.

⚠️ *Legacy Title is older and not as flexible as the Essential Graphics method, but it's good for quick scripture rolls.*

---

## 🟩 STEP 4: Call Out Parts While It Scrolls

As it scrolls, you can:

- **Pause the scroll** by adding **hold keyframes** in Effect Controls.
- **Add markers** on the timeline for where to speak or zoom.
- **Zoom in** on sections using **Scale/Position** or add graphics to highlight.

---

Let me know if you'd like a template with example Bible scrolling text, or if you want to animate highlights (e.g., underline or glow certain verses as it scrolls).

---

Okay, so how do I make the text fit into the width of the box that I want it to, because I've copied it in, but it won't reflow the text to the next line. It just makes the font smaller or bigger and spreads it out, and I need it to reflow into a certain width.

---

To make the text **reflow properly within a specific width** in **Premiere Pro 2025**, you need to convert your text into a **paragraph text box** — not point text.

Here’s how to fix the issue and get clean line-wrapped text that scrolls vertically:

---

## 🟥 Problem Recap:
You're pasting in Bible text, but it acts like a **single-line point text**, which:
- Doesn’t wrap automatically
- Stretches/resizes instead of flowing within a box

---

## ✅ Solution: Create a Paragraph Text Box

### Option A: Create Paragraph Text From Scratch

1. **Select the Type Tool (T)**.
2. **Click-and-drag** in the **Program Monitor** to draw a **text box** — **this is the key**.
   - A bounding box appears.
   - Now you’re in **paragraph mode**, not point mode.

3. **Paste in your text** (Ctrl+V / Cmd+V).
   - It will **reflow** and wrap inside the box.
   - You can **resize the box** (not the font) to adjust line width.

> 🔄 You can always resize the width by dragging the **handles** of the box. The text inside will wrap automatically.

---

### Option B: Convert Existing Text to Paragraph Mode

If you already created text and it’s acting like point text:

1. Select the text layer.
2. Go to **Essential Graphics Panel**.
3. Right-click the text → choose **"Convert to Paragraph Text"**.

   - Or click the **Paragraph icon** (a square with horizontal lines).
   - Now the text will reflow into the bounding box.

4. Resize the **text box**, not the font, to control the wrapping.

---

## 🟩 Bonus Tips

- Use **Left Alignment** in Essential Graphics > Edit tab for clean scripture flow.
- Adjust **Line Spacing (Leading)** to avoid crowding.
- You can **center the text box on screen** using Align & Transform tools.

---

Let me know if you want the text to scroll with pauses between verses, or to add highlights for callouts as you read. I can walk you through that too.