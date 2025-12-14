# Premiere Pro filing system



---



---

I need a filing system for my Premiere Pro projects, productions, and assets. What's the top down from this? I don't know if the production should be... Well, the project should be at the top and then the production under it. Help me get lined up on an organized filing system. Because I have a lot of videos and I want to work on them. But it's a little confusing with how the Premiere Pro setup brings up projects and assets and the browser and what's where. So it's really confusing for me. But I want to be able to have things organized to where I can find the assets I need easily. And know how to move through the projects or to start new projects specifically. And locate the old ones.

---



---

Got it — let’s untangle this. Adobe Premiere Pro (especially with **Productions**) can definitely be confusing until you settle on a **top-down folder system** that matches both Premiere’s logic and your own workflow. Here’s a clean, industry-style filing system you can adopt and scale:

---

## 🔝 Top-Down Structure

1. **Master "Projects" Folder (your drive root or media drive)**
   - Example:  
     ```
     /Video_Projects
     ```

2. **Production (a show, series, or larger body of work)**
   - Example:  
     ```
     /Video_Projects/Podcast_Series/
     /Video_Projects/YouTube_Channel/
     ```

   ➝ A **Production** in Premiere is a container for multiple projects. Use this for big/recurring work (series, clients, campaigns).

3. **Project (an individual video/episode/film inside a production)**
   - Example:  
     ```
     /Video_Projects/Podcast_Series/Episode_01/
     ```

   ➝ Inside a production, you’ll have **project files per episode** (or per video). Each of these links to assets but stays separate, so things don’t bloat.

4. **Assets / Media Folders (always separate from project files!)**
   - Example:
     ```
     /Video_Projects/Podcast_Series/Episode_01/Assets/
     /Video_Projects/Podcast_Series/Episode_01/Media/
     /Video_Projects/Podcast_Series/Episode_01/Exports/
     ```

---

## 🗂 Recommended Folder Template (per project)

Every project folder looks like this:

```
Episode_01/
├── 01_ProjectFiles/
│   └── Episode_01.prproj
├── 02_Media/
│   ├── Video/
│   ├── Audio/
│   ├── Graphics/
│   └── Stills/
├── 03_Assets/
│   ├── AE_Comps/
│   ├── Templates/
│   └── SFX/
├── 04_Exports/
│   ├── Master/
│   ├── Social/
│   └── Review/
└── 05_Documents/
    ├── Scripts/
    └── Notes/
```

✅ Numbered folders keep them sorted.  
✅ Media stays separate from project files — so if Premiere gets confused, relinking is fast.  
✅ Exports don’t clutter your working directories.  

---

## 🔄 Inside Premiere: How it Maps

- **Production** = `/Podcast_Series/` folder  
- **Project** = `Episode_01.prproj` inside `/01_ProjectFiles/`  
- **Bins inside Premiere** should mirror your **02_Media/** and **03_Assets/** folders.  
   - Example bin setup:  
     ```
     Media
       ├── Video
       ├── Audio
       ├── Stills
     Assets
       ├── AE_Comps
       ├── Templates
       └── SFX
     Sequences
     ```

---

## 🔑 Workflow Tips

- Always create **one Premiere project file per video** inside a production (don’t cram a whole series into one project).  
- Keep **media referenced, not duplicated** — don’t drag files from random downloads folders. Put them into `/Media/` first.  
- Use **Productions** if you want multiple editors or multiple episodes in one ecosystem. Otherwise, stick to separate project files.  
- Add **Export subfolders by version/date** (`V1`, `V2`, etc.) so you don’t overwrite finals.  

---

👉 Question for you:  
Do you see yourself using **Productions** (big multi-episode system) or would you rather keep it simple with **individual projects per video**? That determines whether “Production” sits above “Project” in your hierarchy.

---

I think project based. I definitely need to figure out how to set this up and get The assets, media, exports, you know, and all the different stills, graphics, all the things that you said, like all these things, I really need to figure out how do I get media from being in a video that I take in either OBS or with my camera, but just a movie file and then turn that into a project with being able to have all the assets in one place and the media and, you know, I think I created a library at one point, but I can't really understand how different libraries and things are accessed at work, so I just really need help getting those basics and the intricacies.

---

Perfect, thanks for showing me your Finder view — I can see exactly what’s happening: all your video clips, PDFs, images, exports, and screen grabs are just **floating in Recents or Downloads**. That’s why Premiere feels messy: it’s not pulling from a stable “home” where everything lives. Let’s set up a **repeatable system** so every new project has the same structure and you always know where things go.  

---

## 🎬 Step 1: Create a **Master Folder**
On your main drive (or external SSD/HDD), make a **single top-level folder** for all video work:

```
/Video_Projects/
```

---

## 📂 Step 2: Use a Template Project Folder
Inside `/Video_Projects/`, make a **template folder** like this (you’ll copy this for each new project):

```
_ProjectTemplate/
├── 01_ProjectFiles/
│   └── project_name.prproj
├── 02_Media/
│   ├── Video/
│   ├── Audio/
│   ├── Stills/
│   └── Graphics/
├── 03_Assets/
│   ├── AE_Comps/
│   ├── Templates/
│   └── SFX/
├── 04_Exports/
│   ├── Master/
│   ├── Social/
│   └── Review/
└── 05_Documents/
    ├── Scripts/
    └── Notes/
```

Whenever you start a new project, duplicate `_ProjectTemplate` and rename it:  
```
/Video_Projects/Interview_Jacob/
/Video_Projects/YouTube_Tutorial01/
/Video_Projects/Podcast_Ep5/
```

---

## 📥 Step 3: Bring in New Media the Right Way
- **OBS recording** → Save directly into `02_Media/Video/` for that project.  
- **Camera footage** → Copy card contents into `02_Media/Video/`.  
- **Screen captures** → Move them into `02_Media/Stills/` (instead of leaving them in “Recents”).  
- **Downloaded graphics/music** → Drop into `02_Media/Graphics/` or `Audio/`.  

🔑 The rule: **Never import from Downloads/Recents.** Always drag files into the right folder first, then import into Premiere.

---

## 🎛 Step 4: Premiere Setup
- Open Premiere → New Project → Save inside `01_ProjectFiles/`.  
- Inside Premiere’s **Project Panel**, create bins that mirror your folder structure:  
  ```
  Media
    ├── Video
    ├── Audio
    ├── Stills
    └── Graphics
  Assets
    ├── AE_Comps
    ├── Templates
    └── SFX
  Sequences
  ```

This way, if you drop a file into `02_Media/Video/`, you know exactly where to import it and store it inside Premiere.

---

## 📤 Step 5: Exports
When you render, always point to `04_Exports/`.  
- Master copies → `/Master/`  
- Instagram/TikTok cuts → `/Social/`  
- Client review versions → `/Review/`  

---

## 🧩 Libraries vs Projects
- **Premiere Libraries (Creative Cloud Libraries):** these are more like “collections” of reusable things (logos, graphics, stock assets) across multiple projects. You don’t *have* to use them if you keep things in `/Assets/`.  
- **Premiere Project:** the `.prproj` file is the brain. Always lives in `01_ProjectFiles/`.  
- **Premiere Production:** not necessary unless you’re managing a *series* or team. Stick to single projects for now.  

---

✅ Once you adopt this, you’ll always know:
- **Where the raw files are** → `02_Media/`  
- **Where Premiere brain lives** → `01_ProjectFiles/`  
- **Where finished videos go** → `04_Exports/`

---

Would you like me to make you a **command-line script** (Mac) that automatically creates this folder template whenever you start a new project? That way, instead of dragging folders around, you just type:  
```bash
newproj "Interview_Jacob"
```  
…and it spits out the full structure instantly.

---

that sounds good. 

---



---



---

# Create a ready-to-use project template and an installable `newproj` script, then zip them for download.
import os, zipfile, textwrap, stat, json, pathlib

base_dir = "/mnt/data/Premiere_Project_Starter"
template_root = os.path.join(base_dir, "_ProjectTemplate")
script_dir = os.path.join(base_dir, "scripts")
readme_path = os.path.join(base_dir, "README.md")
script_path = os.path.join(script_dir, "newproj")

# Desired folder structure for the template
structure = [
    "01_ProjectFiles",
    "02_Media/Video",
    "02_Media/Audio",
    "02_Media/Stills",
    "02_Media/Graphics",
    "03_Assets/AE_Comps",
    "03_Assets/Templates",
    "03_Assets/SFX",
    "04_Exports/Master",
    "04_Exports/Social",
    "04_Exports/Review",
    "05_Documents/Scripts",
    "05_Documents/Notes",
]

# Ensure base directories
os.makedirs(template_root, exist_ok=True)
os.makedirs(script_dir, exist_ok=True)

# Build folder tree with .gitkeep placeholders
for rel in structure:
    d = os.path.join(template_root, rel)
    os.makedirs(d, exist_ok=True)
    keep = os.path.join(d, ".gitkeep")
    open(keep, "w").close()

# Add a placeholder Premiere project filename suggestion
placeholder = os.path.join(template_root, "01_ProjectFiles", "project_name.prproj.txt")
with open(placeholder, "w") as f:
    f.write("Create your Premiere project here and save as <project_name>.prproj")

# README content
readme = textwrap.dedent("""
# Premiere Pro Project Starter

This package gives you:
1) A reusable folder **_ProjectTemplate** with a clean, numbered structure.
2) A **newproj** command-line tool to quickly generate new projects.

## Folder Template
```
_ProjectTemplate/
├── 01_ProjectFiles/
├── 02_Media/
│   ├── Video/
│   ├── Audio/
│   ├── Stills/
│   └── Graphics/
├── 03_Assets/
│   ├── AE_Comps/
│   ├── Templates/
│   └── SFX/
├── 04_Exports/
│   ├── Master/
│   ├── Social/
│   └── Review/
└── 05_Documents/
    ├── Scripts/
    └── Notes/
```

## Install `newproj` (macOS / zsh)
1. Open Terminal and run:
```
mkdir -p ~/bin
cp scripts/newproj ~/bin/newproj
chmod +x ~/bin/newproj
echo '\n# add user bin to PATH\nexport PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
2. Move the template where you keep projects (recommended: `~/Video_Projects/`):
```
mkdir -p ~/Video_Projects
cp -R _ProjectTemplate ~/Video_Projects/
```

## Usage
Create a new project called "Interview_Jacob" under `~/Video_Projects`:
```
newproj "Interview_Jacob"
```
Or choose a base directory:
```
newproj -b "/Volumes/MediaSSD/Video_Projects" "YouTube_Tutorial01"
```
The command will create:
```
/<base>/YouTube_Tutorial01/
  ├── 01_ProjectFiles/
  ├── 02_Media/{Video,Audio,Stills,Graphics}
  ├── 03_Assets/{AE_Comps,Templates,SFX}
  ├── 04_Exports/{Master,Social,Review}
  └── 05_Documents/{Scripts,Notes}
```

> Tip: In Premiere, mirror these as bins. Always copy OBS/camera files into `02_Media/Video` first, then import.
""")
with open(readme_path, "w") as f:
    f.write(readme)

# newproj script content
script = textwrap.dedent("""
#!/usr/bin/env zsh
#
# newproj: create a Premiere Pro folder scaffold for a project
# Usage:
#   newproj [-b BASE_DIR] [-t TEMPLATE_DIR] [-q] PROJECT_NAME
#
# Defaults:
#   BASE_DIR: ~/Video_Projects
#   TEMPLATE_DIR: <BASE_DIR>/_ProjectTemplate  (falls back to internal layout)
#
set -euo pipefail

BASE_DIR="${HOME}/Video_Projects"
TEMPLATE_DIR=""        # optional; auto-resolves if empty
QUIET=0

print_usage() {
  cat <<'USAGE'
newproj [-b BASE_DIR] [-t TEMPLATE_DIR] [-q] PROJECT_NAME

Options:
  -b BASE_DIR      Where to create the project (default: ~/Video_Projects)
  -t TEMPLATE_DIR  Folder tree to copy (default: <BASE_DIR>/_ProjectTemplate)
  -q               Quiet (no output)

Examples:
  newproj "Interview_Jacob"
  newproj -b "/Volumes/MediaSSD/Video_Projects" "YouTube_Tutorial01"
USAGE
}

while getopts ":b:t:qh" opt; do
  case "$opt" in
    b) BASE_DIR="$OPTARG" ;;
    t) TEMPLATE_DIR="$OPTARG" ;;
    q) QUIET=1 ;;
    h) print_usage; exit 0 ;;
    \?) echo "Unknown option -$OPTARG" >&2; print_usage; exit 1 ;;
    :)  echo "Option -$OPTARG requires an argument." >&2; print_usage; exit 1 ;;
  esac
done
shift $((OPTIND-1))

if [ $# -lt 1 ]; then
  echo "Error: PROJECT_NAME required." >&2
  print_usage
  exit 1
fi

PROJECT_NAME="$1"
DEST="${BASE_DIR}/${PROJECT_NAME}"

# Resolve default template if not provided
if [ -z "${TEMPLATE_DIR}" ]; then
  TEMPLATE_DIR="${BASE_DIR}/_ProjectTemplate"
fi

# Create base dir if missing
mkdir -p "${BASE_DIR}"

# If template exists, copy it; else build folders from scratch
if [ -d "${TEMPLATE_DIR}" ]; then
  cp -R "${TEMPLATE_DIR}" "${DEST}"
  # If copied folder is literally named _ProjectTemplate, rename to project
  if [ -d "${DEST}/_ProjectTemplate" ]; then
    mv "${DEST}/_ProjectTemplate" "${DEST}.tmp"
    rm -rf "${DEST}"
    mv "${DEST}.tmp" "${DEST}"
  fi
else
  mkdir -p "${DEST}/01_ProjectFiles"
  mkdir -p "${DEST}/02_Media/Video" "${DEST}/02_Media/Audio" "${DEST}/02_Media/Stills" "${DEST}/02_Media/Graphics"
  mkdir -p "${DEST}/03_Assets/AE_Comps" "${DEST}/03_Assets/Templates" "${DEST}/03_Assets/SFX"
  mkdir -p "${DEST}/04_Exports/Master" "${DEST}/04_Exports/Social" "${DEST}/04_Exports/Review"
  mkdir -p "${DEST}/05_Documents/Scripts" "${DEST}/05_Documents/Notes"
fi

# Optional: drop a README and a suggested .prproj name
cat > "${DEST}/README.txt" <<EOF
Project: ${PROJECT_NAME}

Save your Premiere file here:
  ${DEST}/01_ProjectFiles/${PROJECT_NAME}.prproj

Media goes here:
  ${DEST}/02_Media/{Video,Audio,Stills,Graphics}

After Effects comps and templates:
  ${DEST}/03_Assets/{AE_Comps,Templates,SFX}

Exports:
  ${DEST}/04_Exports/{Master,Social,Review}
EOF

if [ ${QUIET} -eq 0 ]; then
  echo "✔ Created project scaffold at: ${DEST}"
  echo "→ Open Premiere and save your project as:"
  echo "  ${DEST}/01_ProjectFiles/${PROJECT_NAME}.prproj"
fi
""")

with open(script_path, "w") as f:
    f.write(script)
os.chmod(script_path, os.stat(script_path).st_mode | stat.S_IEXEC)

# Zip everything
zip_path = "/mnt/data/Premiere_Project_Starter.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(base_dir):
        for name in files:
            full = os.path.join(root, name)
            rel = os.path.relpath(full, base_dir)
            z.write(full, arcname=rel)

zip_path

---

Awesome—let’s make this turnkey. I built you a ready-to-use **project template + a `newproj` command** so you can spin up clean Premiere folders in seconds.

[Download the Premiere Project Starter (ZIP)](sandbox:/mnt/data/Premiere_Project_Starter.zip)

What’s inside:
- `_ProjectTemplate/` — the full numbered folder tree (Media, Assets, Exports, etc.).
- `scripts/newproj` — a macOS zsh command that creates a fresh project scaffold anywhere you want.
- `README.md` — quick reference.

## 1) Install `newproj` (one-time)
Open Terminal and run:
```bash
mkdir -p ~/bin
cp ~/Downloads/Premiere_Project_Starter/scripts/newproj ~/bin/newproj
chmod +x ~/bin/newproj
echo '\n# add user bin to PATH\nexport PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

## 2) Place the template
```bash
mkdir -p ~/Video_Projects
cp -R ~/Downloads/Premiere_Project_Starter/_ProjectTemplate ~/Video_Projects/
```

## 3) Create a new Premiere project folder
```bash
newproj "Interview_Jacob"
# or to a specific drive:
newproj -b "/Volumes/MediaSSD/Video_Projects" "YouTube_Tutorial01"
```

That creates:
```
/<base>/<ProjectName>/
├── 01_ProjectFiles/
├── 02_Media/{Video,Audio,Stills,Graphics}
├── 03_Assets/{AE_Comps,Templates,SFX}
├── 04_Exports/{Master,Social,Review}
└── 05_Documents/{Scripts,Notes}
```

## 4) Premiere workflow (simple + bulletproof)
- **Save the .prproj here**: `01_ProjectFiles/<ProjectName>.prproj`
- **Put camera/OBS clips here**: `02_Media/Video/` (then import into Premiere)
- **Put music/VO here**: `02_Media/Audio/`
- **Put logos/lower-thirds here**: `02_Media/Graphics/` (or `03_Assets/Templates` if reusable)
- **Put stills/screens**: `02_Media/Stills/`
- **Exports only**: `04_Exports/` (Master, Social, Review)

Inside Premiere, mirror this with bins:
```
Media
  ├── Video
  ├── Audio
  ├── Stills
  └── Graphics
Assets
  ├── AE_Comps
  ├── Templates
  └── SFX
Sequences
```

## Notes on Libraries (optional)
- **Creative Cloud Libraries** are global/reusable assets. You don’t need them to stay organized—your `/03_Assets` folder covers most needs. Use Libraries later if you want cloud-synced logos or MOGRTs across many projects.

If you want, I can also add an **Automator Quick Action** so you can right-click in Finder ➝ “New Premiere Project Folder…” and it’ll run `newproj` for you.

---



---

can you use terminal to execute this for me now

---



---

I can’t run commands directly in your Terminal — but I can give you the **exact commands** you can paste in your Terminal window right now to set everything up. Here’s what to do step-by-step:

---

### 1. Unzip the package you downloaded
If you downloaded `Premiere_Project_Starter.zip` into your `Downloads` folder, run:
```bash
cd ~/Downloads
unzip Premiere_Project_Starter.zip -d Premiere_Project_Starter
```

---

### 2. Install the `newproj` script
This puts the command into `~/bin` and makes it executable:

```bash
mkdir -p ~/bin
cp Premiere_Project_Starter/scripts/newproj ~/bin/newproj
chmod +x ~/bin/newproj
```

Then add it to your PATH (so you can call `newproj` from anywhere):
```bash
echo '\n# add user bin to PATH\nexport PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

---

### 3. Move the project template into place
Recommended to keep in `~/Video_Projects`:

```bash
mkdir -p ~/Video_Projects
cp -R Premiere_Project_Starter/_ProjectTemplate ~/Video_Projects/
```

---

### 4. Test it
Now try creating a new project scaffold:
```bash
newproj "Interview_Jacob"
```

You should see:
```
✔ Created project scaffold at: /Users/you/Video_Projects/Interview_Jacob
→ Open Premiere and save your project as:
/Users/you/Video_Projects/Interview_Jacob/01_ProjectFiles/Interview_Jacob.prproj
```

---

Do you want me to also write you a **one-liner setup script** so you can just copy-paste once and have all of this done automatically (install + template + path update)?

---

yes but I liked what you said about a quick action

---

Perfect 👍 — let’s do both:  

1. A **one-liner setup script** (so you just paste once in Terminal to install `newproj`).  
2. A **Quick Action (Automator Service)** so you can right-click in Finder → “New Premiere Project…” and it’ll build the full folder tree.  

---

## 1) One-liner setup script
Copy & paste this into Terminal:

```bash
cd ~/Downloads && unzip -o Premiere_Project_Starter.zip -d Premiere_Project_Starter && \
mkdir -p ~/bin ~/Video_Projects && \
cp Premiere_Project_Starter/scripts/newproj ~/bin/newproj && chmod +x ~/bin/newproj && \
cp -R Premiere_Project_Starter/_ProjectTemplate ~/Video_Projects/ && \
echo '\n# add user bin to PATH\nexport PATH="$HOME/bin:$PATH"' >> ~/.zshrc && \
source ~/.zshrc && \
echo "✅ newproj installed. Try: newproj \"Test_Project\""
```

That sets up everything in one shot.

---

## 2) Finder Quick Action (Right-Click Menu)

Here’s how to create it:

1. **Open Automator** (⌘+Space → search *Automator*).  
2. Choose **Quick Action** (aka “Service”).  
3. At the top:  
   - Workflow receives → `no input`  
   - In → `Finder.app`  

4. From the left library, drag in **Run Shell Script**.  
   - Set Shell to `/bin/zsh`.  
   - Paste this script:

   ```zsh
   # Ask for project name
   PROJECT_NAME=$(osascript -e 'Tell application "System Events" to display dialog "Enter project name:" default answer ""' -e 'text returned of result')

   if [ -z "$PROJECT_NAME" ]; then
     exit 0
   fi

   # Base directory (adjust if you keep projects elsewhere)
   BASE_DIR="$HOME/Video_Projects"

   # Call your newproj tool
   ~/bin/newproj "$PROJECT_NAME"

   # Reveal in Finder
   open "$BASE_DIR/$PROJECT_NAME"
   ```

5. Save as **New Premiere Project**.

Now, in Finder you can **Right-Click → Quick Actions → New Premiere Project…** → it will ask for a name → boom, folder tree created and opened.

---

⚡ Question:  
Do you want the Quick Action to always use `~/Video_Projects`, or should it instead **ask you which folder** to create the project in (like picking an external SSD vs local drive)?

---



---

I see exactly what happened 👍 — the error says:  

```
unzip:  cannot find or open Premiere_Project_Starter.zip
```

That just means the ZIP file isn’t in your `~/Downloads` folder (where the command is looking).  

### ✅ Fix
1. First check what’s actually in Downloads:
```bash
ls ~/Downloads
```

2. If the file is there but has a slightly different name (e.g. `Premiere_Project_Starter (1).zip`), just adjust the command. Example:
```bash
cd ~/Downloads
unzip -o "Premiere_Project_Starter (1).zip" -d Premiere_Project_Starter
```

3. Then re-run the rest of the install (without the unzip part, since it’s already extracted):
```bash
mkdir -p ~/bin ~/Video_Projects
cp Premiere_Project_Starter/scripts/newproj ~/bin/newproj
chmod +x ~/bin/newproj
cp -R Premiere_Project_Starter/_ProjectTemplate ~/Video_Projects/
echo '\n# add user bin to PATH\nexport PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

---

👉 Can you run `ls ~/Downloads` and tell me exactly how the ZIP file is named? That way I can give you the exact command with the right filename.

---

Does this allow me to choose a video and then create the project based on that video? Or is that another step that I'll have to do?

---

Great question 👍  

Right now the tool we set up (`newproj`) **only creates the folder structure + placeholder project file**. It doesn’t yet take a video file and automatically drop it into `02_Media/Video/`. That part is still a manual step:  

1. Run `newproj "MyVideoProject"`  
   → gives you the full folder tree.  
2. Copy or move your chosen `.mov` / `.mp4` file into:  
   ```
   ~/Video_Projects/MyVideoProject/02_Media/Video/
   ```  
3. Open Premiere and **import from that folder**.  

---

### 🔄 If you want to automate step 2
We can extend the `newproj` script so it works like this:  
```bash
newproj -f /path/to/video.mov "MyVideoProject"
```

That would:  
- Build the project folder.  
- Copy (or move) `video.mov` into `02_Media/Video/`.  
- Optionally rename it to match the project name (e.g. `MyVideoProject.mov`).  

---

⚡ So: the current version = **folders only**.  
If you want, I can patch `newproj` to support `-f` (file input) so you can right-click a video, send it into Finder Quick Action → it builds the project + drops the video in immediately.  

👉 Do you want me to patch it so it both **creates the folder tree** *and* **ingests a video file into `02_Media/Video/` automatically**?

---

yes! the more simple the better!

---



---



---

Love it. I’ll upgrade your tool so it can **create the project AND ingest your video(s)** in one shot.

## A) Install the upgraded `newproj` (supports `-f`)
Paste this whole block in Terminal:

```bash
cat > ~/bin/newproj <<'ZSH'
#!/usr/bin/env zsh
# newproj — create a Premiere folder scaffold (and optionally ingest media)
# Usage:
#   newproj [-b BASE_DIR] [-t TEMPLATE_DIR] [-m] [-r] [-o] [-q] [-f FILE ...] PROJECT_NAME
# Options:
#   -b BASE_DIR      Base directory (default: ~/Video_Projects)
#   -t TEMPLATE_DIR  Template (default: <BASE_DIR>/_ProjectTemplate; if missing, build folders)
#   -f FILE          Media file(s) to ingest into 02_Media/Video (repeatable)
#   -m               Move (mv) instead of copy (cp)
#   -r               If exactly one file, rename it to <PROJECT_NAME><orig_ext>
#   -o               Open the project folder in Finder when done
#   -q               Quiet
set -euo pipefail

BASE_DIR="${HOME}/Video_Projects"
TEMPLATE_DIR=""
QUIET=0
MOVE=0
RENAME_SINGLE=0
OPENF=0
FILES=()

print_usage() {
  cat <<'USAGE'
newproj [-b BASE_DIR] [-t TEMPLATE_DIR] [-m] [-r] [-o] [-q] [-f FILE ...] PROJECT_NAME

Examples:
  newproj "Interview_Jacob"
  newproj -f ~/Desktop/clip.mov "Tutorial_01"
  newproj -m -r -f "/Volumes/Card/DCIM/100MSDCF/DSC_0001.MP4" "Trip_Vlog"
  newproj -b "/Volumes/MediaSSD/Video_Projects" -f a.mov -f b.mov -o "MultiCam_Test"
USAGE
}

# parse args
while getopts ":b:t:f:mrqo h" opt; do
  case "$opt" in
    b) BASE_DIR="$OPTARG" ;;
    t) TEMPLATE_DIR="$OPTARG" ;;
    f) FILES+=("$OPTARG") ;;
    m) MOVE=1 ;;
    r) RENAME_SINGLE=1 ;;
    q) QUIET=1 ;;
    o) OPENF=1 ;;
    h) print_usage; exit 0 ;;
    \?) echo "Unknown option -$OPTARG" >&2; print_usage; exit 1 ;;
    :)  echo "Option -$OPTARG requires an argument." >&2; print_usage; exit 1 ;;
  esac
done
shift $((OPTIND-1))

if [ $# -lt 1 ]; then
  echo "Error: PROJECT_NAME required." >&2
  print_usage
  exit 1
fi

PROJECT_NAME="$1"
DEST="${BASE_DIR}/${PROJECT_NAME}"

# Defaults
if [ -z "${TEMPLATE_DIR}" ]; then
  TEMPLATE_DIR="${BASE_DIR}/_ProjectTemplate"
fi

# Build base
mkdir -p "${BASE_DIR}"

# Copy template or synthesize structure
if [ -d "${TEMPLATE_DIR}" ]; then
  cp -R "${TEMPLATE_DIR}" "${DEST}"
  if [ -d "${DEST}/_ProjectTemplate" ]; then
    mv "${DEST}/_ProjectTemplate" "${DEST}.tmp"
    rm -rf "${DEST}"
    mv "${DEST}.tmp" "${DEST}"
  fi
else
  mkdir -p "${DEST}/01_ProjectFiles"
  mkdir -p "${DEST}/02_Media/Video" "${DEST}/02_Media/Audio" "${DEST}/02_Media/Stills" "${DEST}/02_Media/Graphics"
  mkdir -p "${DEST}/03_Assets/AE_Comps" "${DEST}/03_Assets/Templates" "${DEST}/03_Assets/SFX"
  mkdir -p "${DEST}/04_Exports/Master" "${DEST}/04_Exports/Social" "${DEST}/04_Exports/Review"
  mkdir -p "${DEST}/05_Documents/Scripts" "${DEST}/05_Documents/Notes"
fi

# Drop a short README
cat > "${DEST}/README.txt" <<EOF
Project: ${PROJECT_NAME}

Save your Premiere file here:
  ${DEST}/01_ProjectFiles/${PROJECT_NAME}.prproj

Media goes here:
  ${DEST}/02_Media/{Video,Audio,Stills,Graphics}

After Effects / Templates:
  ${DEST}/03_Assets/{AE_Comps,Templates,SFX}

Exports:
  ${DEST}/04_Exports/{Master,Social,Review}
EOF

# Ingest files (to 02_Media/Video)
if [ ${#FILES[@]} -gt 0 ]; then
  VIDDIR="${DEST}/02_Media/Video"
  mkdir -p "${VIDDIR}"

  if [ ${#FILES[@]} -eq 1 ] && [ ${RENAME_SINGLE} -eq 1 ]; then
    src="${FILES[1]}"
    ext="${src##*.}"
    target="${VIDDIR}/${PROJECT_NAME}.${ext}"
    if [ ${MOVE} -eq 1 ]; then
      mv "$src" "$target"
    else
      cp "$src" "$target"
    fi
  else
    for src in "${FILES[@]}"; do
      if [ ${MOVE} -eq 1 ]; then
        mv "$src" "${VIDDIR}/"
      else
        cp "$src" "${VIDDIR}/"
      fi
    done
  fi
fi

if [ ${QUIET} -eq 0 ]; then
  echo "✔ Created project at: ${DEST}"
  echo "→ Save Premiere project as: ${DEST}/01_ProjectFiles/${PROJECT_NAME}.prproj"
  if [ ${#FILES[@]} -gt 0 ]; then
    echo "→ Ingested ${#FILES[@]} file(s) into: ${DEST}/02_Media/Video"
  fi
fi

[ ${OPENF} -eq 1 ] && open "${DEST}"
ZSH
chmod +x ~/bin/newproj
```

**How to use it now:**
- Single file (copy):
  ```bash
  newproj -f ~/Desktop/clip.mov "MyProject"
  ```
- Single file (move & rename to project name):
  ```bash
  newproj -m -r -f ~/Desktop/clip.mov -o "MyProject"
  ```
- Multiple files:
  ```bash
  newproj -f a.mov -f b.mov -f c.mov -o "MultiCam_Test"
  ```

---

## B) (Nice-to-have) Right-click in Finder → **New Project from Selected Video…**
This Quick Action will take whatever file(s) you select in Finder, ask for a project name (pre-filled from the first file), and call `newproj` with `-f` so your media lands in `02_Media/Video/`.

**Create it once:**
1. Open **Automator** → **Quick Action**.
2. Top bar:
   - *Workflow receives*: **files or folders**
   - *in*: **Finder**
3. Add **Run Shell Script**.
   - Shell: `/bin/zsh`
   - Pass input: **as arguments**
4. Paste:

```zsh
#!/bin/zsh
set -e

# Default base; change if you prefer an external drive
BASE_DIR="$HOME/Video_Projects"

if [ "$#" -lt 1 ]; then
  exit 0
fi

# Use first selected file to suggest a project name
first="$1"
suggest="$(basename "$first")"
suggest="${suggest%.*}"

proj=$(osascript -e 'Tell application "System Events" to display dialog "Enter project name:" default answer "'"$suggest"'"' -e 'text returned of result') || exit 0

# Build -f args for all selected items
args=()
for f in "$@"; do
  args+=(-f "$f")
done

# Create project, ingest files, open the folder
"$HOME/bin/newproj" -b "$BASE_DIR" "${args[@]}" -o "$proj"
```

5. Save as **New Project from Selected Video…**

**Use it:**
- In Finder, select one or more clips → Right-click → **Quick Actions** → **New Project from Selected Video…** → confirm the name → done.

---

### That’s it
You can now go from **clip → organized project + media ingested** in one command or one right-click.

---



---



---



---

Perfect — you’re already in the **Quick Actions** menu. We just need to add a new one that hooks into your `newproj` script. Here’s how you can get “**New Project from Selected Video…**” to show up right there:  

---

## 🚀 Create the Finder Quick Action
1. Open **Automator** (⌘+Space → type *Automator*).  
2. Choose **New Document → Quick Action**.  
3. At the top of the workflow:  
   - “Workflow receives” → **files or folders**  
   - “in” → **Finder.app**  
4. Drag in **Run Shell Script** from the left panel.  
   - Shell: `/bin/zsh`  
   - Pass input: **as arguments**  

5. Paste this script:

   ```zsh
   #!/bin/zsh
   set -e

   BASE_DIR="$HOME/Video_Projects"

   if [ "$#" -lt 1 ]; then
     exit 0
   fi

   # Use first file name as suggested project name
   first="$1"
   suggest="$(basename "$first")"
   suggest="${suggest%.*}"

   # Ask user for project name
   proj=$(osascript -e 'Tell application "System Events" to display dialog "Enter project name:" default answer "'"$suggest"'"' -e 'text returned of result') || exit 0

   # Build -f args for all selected items
   args=()
   for f in "$@"; do
     args+=(-f "$f")
   done

   # Run newproj with selected files
   "$HOME/bin/newproj" -b "$BASE_DIR" "${args[@]}" -o "$proj"
   ```

6. Save it as **New Project from Selected Video…**  

---

## 🖱 How to use
- Right-click on one or more video files in Finder.  
- Choose **Quick Actions → New Project from Selected Video…**  
- A dialog pops up asking for the project name (pre-filled with the filename).  
- When you confirm, it:  
  - Creates the full Premiere folder structure under `~/Video_Projects`  
  - Copies your video(s) into `02_Media/Video/`  
  - Opens the new project folder in Finder.  

---

👉 Do you want me to make it so the Quick Action can also **ask which base folder** (e.g. external SSD vs `~/Video_Projects`) every time you run it? Or do you prefer it always defaulting to `~/Video_Projects`?

---



---

🔥 That’s it working exactly as intended!  

From your screenshot I can see:  
- `02_Media/Video/` already has your `.mov` file inside (auto-ingested ✅).  
- `01_ProjectFiles/` is waiting for you to save your Premiere project.  
- `03_Assets/`, `04_Exports/`, `05_Documents/` are all scaffolded correctly.  
- `README.txt` gives you the quick reference.  

So now your workflow is:  

1. **Right-click any video → Quick Actions → New Project from Selected Video…**  
   → Instantly get the full project structure.  

2. Open Premiere and **Save As** directly into `01_ProjectFiles/YourProjectName.prproj`.  

3. Your raw video is already in `02_Media/Video/`.  
   Drag it in Premiere from that folder and edit.  

---

✨ Optional Next Upgrade  
Want me to tweak it so:  
- The video is **renamed to match the project name** automatically (instead of keeping the camera filename like `2025-08-30 14-59-14.mov`)?  

That way you’d have:  
```
02_Media/Video/
   Interview_Jacob.mov
```  

Would make things super tidy inside Premiere bins too. Want me to patch that in?

---

How? When it creates this before it asks me for a name for the project, it didn't actually create a project file. It's still waiting for me to, I guess, do that.

---

Exactly 👍 — what you’re seeing is normal Premiere behavior.  

Here’s why:  
- Our `newproj` script creates the **folder structure** and ingests your media.  
- But the `.prproj` file (the actual Premiere project database) can *only* be created by Premiere itself when you do **File → New Project → Save**.  

That’s why you see a placeholder file called `project_name.prproj.txt` — it’s just a reminder. Premiere won’t understand that as a real project file.  

---

## 🎬 Your workflow from here
1. Use Quick Action → creates the folder + ingests media.  
   (You’ve already got this working perfectly!)  

2. Open Premiere Pro → New Project.  
   - Name it the **same as your project folder**.  
   - Save it inside:  
     ```
     01_ProjectFiles/YourProjectName.prproj
     ```

3. In Premiere’s **Project Panel**, import your media from:  
   ```
   02_Media/Video/
   ```
   (your clip is already there).  

---

✅ That’s it — from now on, every project will have:  
- A real `.prproj` inside `01_ProjectFiles/` (your editing brain).  
- Media organized under `02_Media/`.  
- Exports under `04_Exports/`.  

---

⚡ If you want, I can go one step further and give you a **Premiere Project template file** (an actual `.prproj`) that you save once with empty bins already set up (`Video`, `Audio`, `Stills`, `Graphics`, `Sequences`). Then the script can auto-copy that into `01_ProjectFiles/` so you don’t even have to create a new project inside Premiere — you’d just double-click and start editing.  

👉 Do you want me to build that `.prproj` starter template for you, so every new project already has bins ready and you don’t have to set them up each time?

---

yessss

---



---



---

Yes! We can make it so each new job **already has a real `.prproj`** inside `01_ProjectFiles`, ready to open—no extra clicks.

Because a Premiere project file is proprietary, the right move is:
1) **You create a “starter” .prproj once** (with bins/sequences set how you like).
2) The script will **auto-copy & rename** that file into each new project folder.

Below are the exact steps + an upgraded script that does it all (including optional media rename).

---

# 1) Make your Premiere template *once*
In Premiere Pro:
1. File → **New Project** → name it `ProjectTemplate`.
2. In the Project panel, create your standard bins:
   ```
   Media
     ├── Video
     ├── Audio
     ├── Stills
     └── Graphics
   Assets
     ├── AE_Comps
     ├── Templates
     └── SFX
   Sequences
   ```
3. (Optional) Create a default sequence that matches your usual footage
   (e.g., **3840x2160, 23.976**, your preferred audio layout), and place it in **Sequences**.
4. Save it to:
   ```
   ~/Video_Projects/_ProjectTemplate/01_ProjectFiles/ProjectTemplate.prproj
   ```

> You can tweak this template later (add LUTs, color bins, custom metadata columns, etc.). The script will always copy the latest version.

---

# 2) Install the upgraded `newproj` (auto-copies the template .prproj)

Paste this in Terminal (it overwrites your current `newproj` with the smarter one):

```bash
cat > ~/bin/newproj <<'ZSH'
#!/usr/bin/env zsh
# newproj — create a Premiere folder scaffold, ingest media, and copy a .prproj template
# Usage:
#   newproj [-b BASE_DIR] [-t TEMPLATE_DIR] [-p PRPROJ_TEMPLATE] [-m] [-r] [-o] [-q] [-f FILE ...] PROJECT_NAME
#
# Options:
#   -b BASE_DIR         Base directory (default: ~/Video_Projects)
#   -t TEMPLATE_DIR     Folder tree template (default: <BASE_DIR>/_ProjectTemplate; if missing, build folders)
#   -p PRPROJ_TEMPLATE  Path to a .prproj file to copy (default: first .prproj found under TEMPLATE_DIR/01_ProjectFiles)
#   -f FILE             Media file(s) to ingest into 02_Media/Video (repeatable)
#   -m                  Move (mv) instead of copy (cp)
#   -r                  If exactly one file via -f, rename it to <PROJECT_NAME><ext>
#   -o                  Open the project folder in Finder when done
#   -q                  Quiet
set -euo pipefail

BASE_DIR="${HOME}/Video_Projects"
TEMPLATE_DIR=""
QUIET=0
MOVE=0
RENAME_SINGLE=0
OPENF=0
PRPROJ_TEMPLATE=""
FILES=()

print_usage() {
  cat <<'USAGE'
newproj [-b BASE_DIR] [-t TEMPLATE_DIR] [-p PRPROJ_TEMPLATE] [-m] [-r] [-o] [-q] [-f FILE ...] PROJECT_NAME

Examples:
  newproj "Interview_Jacob"
  newproj -f ~/Desktop/clip.mov "Tutorial_01"
  newproj -m -r -f "/Volumes/Card/DCIM/100MSDCF/DSC_0001.MP4" "Trip_Vlog"
  newproj -b "/Volumes/MediaSSD/Video_Projects" -p ~/Video_Projects/_ProjectTemplate/01_ProjectFiles/ProjectTemplate.prproj -f a.mov -f b.mov -o "MultiCam_Test"
USAGE
}

while getopts ":b:t:p:f:mrqo h" opt; do
  case "$opt" in
    b) BASE_DIR="$OPTARG" ;;
    t) TEMPLATE_DIR="$OPTARG" ;;
    p) PRPROJ_TEMPLATE="$OPTARG" ;;
    f) FILES+=("$OPTARG") ;;
    m) MOVE=1 ;;
    r) RENAME_SINGLE=1 ;;
    q) QUIET=1 ;;
    o) OPENF=1 ;;
    h) print_usage; exit 0 ;;
    \?) echo "Unknown option -$OPTARG" >&2; print_usage; exit 1 ;;
    :)  echo "Option -$OPTARG requires an argument." >&2; print_usage; exit 1 ;;
  esac
done
shift $((OPTIND-1))

if [ $# -lt 1 ]; then
  echo "Error: PROJECT_NAME required." >&2
  print_usage
  exit 1
fi

PROJECT_NAME="$1"
DEST="${BASE_DIR}/${PROJECT_NAME}"

# Defaults
if [ -z "${TEMPLATE_DIR}" ]; then
  TEMPLATE_DIR="${BASE_DIR}/_ProjectTemplate"
fi

mkdir -p "${BASE_DIR}"

# Copy the folder template or synthesize if missing
if [ -d "${TEMPLATE_DIR}" ]; then
  cp -R "${TEMPLATE_DIR}" "${DEST}"
  if [ -d "${DEST}/_ProjectTemplate" ]; then
    mv "${DEST}/_ProjectTemplate" "${DEST}.tmp"
    rm -rf "${DEST}"
    mv "${DEST}.tmp" "${DEST}"
  fi
else
  mkdir -p "${DEST}/01_ProjectFiles"
  mkdir -p "${DEST}/02_Media/Video" "${DEST}/02_Media/Audio" "${DEST}/02_Media/Stills" "${DEST}/02_Media/Graphics"
  mkdir -p "${DEST}/03_Assets/AE_Comps" "${DEST}/03_Assets/Templates" "${DEST}/03_Assets/SFX"
  mkdir -p "${DEST}/04_Exports/Master" "${DEST}/04_Exports/Social" "${DEST}/04_Exports/Review"
  mkdir -p "${DEST}/05_Documents/Scripts" "${DEST}/05_Documents/Notes"
fi

# If no explicit PRPROJ template passed, try to find one under TEMPLATE_DIR
if [ -z "${PRPROJ_TEMPLATE}" ]; then
  if [ -d "${TEMPLATE_DIR}/01_ProjectFiles" ]; then
    # pick the first .prproj if present
    set +e
    PRPROJ_TEMPLATE=$(ls "${TEMPLATE_DIR}/01_ProjectFiles/"*.prproj 2>/dev/null | head -n 1)
    set -e || true
  fi
fi

# Copy .prproj if we found/received one
DEST_PRPROJ="${DEST}/01_ProjectFiles/${PROJECT_NAME}.prproj"
if [ -n "${PRPROJ_TEMPLATE}" ] && [ -f "${PRPROJ_TEMPLATE}" ]; then
  mkdir -p "${DEST}/01_ProjectFiles"
  cp "${PRPROJ_TEMPLATE}" "${DEST_PRPROJ}"
else
  # Write a small reminder if no template was found
  cat > "${DEST}/01_ProjectFiles/READ_ME_FIRST.txt" <<EOF
No .prproj template found.
Create a new Premiere project and save as:
  ${DEST_PRPROJ}
EOF
fi

# Write top-level README
cat > "${DEST}/README.txt" <<EOF
Project: ${PROJECT_NAME}

Premiere project file:
  ${DEST_PRPROJ}

Media:
  ${DEST}/02_Media/{Video,Audio,Stills,Graphics}

Assets:
  ${DEST}/03_Assets/{AE_Comps,Templates,SFX}

Exports:
  ${DEST}/04_Exports/{Master,Social,Review}
EOF

# Ingest media
if [ ${#FILES[@]} -gt 0 ]; then
  VIDDIR="${DEST}/02_Media/Video"
  mkdir -p "${VIDDIR}"

  if [ ${#FILES[@]} -eq 1 ] && [ ${RENAME_SINGLE} -eq 1 ]; then
    src="${FILES[1]}"
    ext="${src##*.}"
    target="${VIDDIR}/${PROJECT_NAME}.${ext}"
    if [ ${MOVE} -eq 1 ]; then
      mv "$src" "$target"
    else
      cp "$src" "$target"
    fi
  else
    for src in "${FILES[@]}"; do
      if [ ${MOVE} -eq 1 ]; then
        mv "$src" "${VIDDIR}/"
      else
        cp "$src" "${VIDDIR}/"
      fi
    done
  fi
fi

if [ ${QUIET} -eq 0 ]; then
  echo "✔ Created project at: ${DEST}"
  if [ -f "${DEST_PRPROJ}" ]; then
    echo "→ Premiere project created: ${DEST_PRPROJ}"
  else
    echo "→ No .prproj template found; create: ${DEST_PRPROJ}"
  fi
  if [ ${#FILES[@]} -gt 0 ]; then
    echo "→ Ingested ${#FILES[@]} file(s) into: ${DEST}/02_Media/Video"
  fi
fi

[ ${OPENF} -eq 1 ] && open "${DEST}"
ZSH
chmod +x ~/bin/newproj
```

Now, if you’ve saved `ProjectTemplate.prproj` where we said, every run will drop a **real** project file named after your project into `01_ProjectFiles`.

**Examples**
```bash
# Use your saved template automatically:
newproj -f ~/Desktop/clip.mov -r -o "MyProject"

# If your .prproj lives elsewhere:
newproj -p "/Volumes/MediaSSD/Templates/ProjectTemplate.prproj" -f ~/Desktop/clip.mov -o "Client_Video_01"
```

---

# 3) (Optional) Update the Quick Action to use the template & rename
If you want the right-click to also rename the first ingested clip to the project name and ensure the .prproj is created:

Open **Automator → Quick Action** you made earlier → **Run Shell Script**, replace with:

```zsh
#!/bin/zsh
set -e

BASE_DIR="$HOME/Video_Projects"
PRPROJ_TEMPLATE="$HOME/Video_Projects/_ProjectTemplate/01_ProjectFiles/ProjectTemplate.prproj"

if [ "$#" -lt 1 ]; then
  exit 0
fi

first="$1"
suggest="$(basename "$first")"
suggest="${suggest%.*}"

proj=$(osascript -e 'Tell application "System Events" to display dialog "Enter project name:" default answer "'"$suggest"'"' -e 'text returned of result') || exit 0

args=()
for f in "$@"; do
  args+=(-f "$f")
done

# -r = rename single file to project name if exactly one was selected
"$HOME/bin/newproj" -b "$BASE_DIR" -p "$PRPROJ_TEMPLATE" -r "${args[@]}" -o "$proj"
```

Save. Now the Quick Action will:
- Create the folder tree
- **Copy your `ProjectTemplate.prproj`** into `01_ProjectFiles/<Project>.prproj`
- **Ingest the selected file(s)**
- If you selected **one** file, it will rename it to match the project name (tidy!)
- Open the folder

---

You’re set. Next time you right-click a clip → **New Project from Selected Video…** → you’ll have a *real* Premiere project file already in place, bins prebuilt, sequence ready (if you put one in the template), and media ingested.

---



---

Media
  ├── Video
  ├── Audio
  ├── Stills
  └── Graphics
Assets
  ├── AE_Comps
  ├── Templates
  └── SFX
Sequences

are these 2 bins with the respective bins inside, total 10? 

---



---

Yes — you’ve got the right count.  

What you’ve written is **2 top-level bins** with their own children:  

- **Media** (4 sub-bins)  
  - Video  
  - Audio  
  - Stills  
  - Graphics  

- **Assets** (3 sub-bins)  
  - AE_Comps  
  - Templates  
  - SFX  

And then **Sequences** as its own top-level bin.  

So in total:  
- 3 top-level bins (**Media**, **Assets**, **Sequences**)  
- 7 sub-bins inside the first two  

👉 That makes **10 bins total** (3 + 7).  

Would you like me to update the `.prproj` template instructions so that when you make it, those 10 bins are already created and in place?

---

Can I pre-build the template to have any assets I want already in it, like logos and maybe some parts already gone, like some effects and things like that, that's already in there?

---



---



---

Short answer: **yes**—you can pre-build a Premiere **project template** that already contains your brand assets, logos, lower-thirds, MOGRTs, LUT look, adjustment layers, audio buses/effects, and even a ready-to-go master sequence. Then every new job will start with all that in place.

Here’s the clean, reliable way to do it:

# How to build a rock-solid `.prproj` template

1) **Put your brand assets inside the template tree**
Place these inside `_ProjectTemplate` so paths stay consistent across copies:
```
_ProjectTemplate/
├─ 01_ProjectFiles/ProjectTemplate.prproj
├─ 02_Media/
│  ├─ Video/      (empty)
│  ├─ Audio/      (place your theme music if you always use it)
│  ├─ Stills/     (brand photos if needed)
│  └─ Graphics/   (PNG/SVG logos you’ll actually reference in sequences)
└─ 03_Assets/
   ├─ Brand/      (original logo packs, lockups, color refs)
   ├─ MOGRTs/     (installable Motion Graphics templates)
   ├─ LUTs/       (*.cube for Lumetri “Browse”)
   ├─ AE_Comps/   (optional: an AE template project to dynamic-link)
   ├─ SFX/        (button taps, whooshes you always use)
   └─ Templates/  (caption styles, bars & tone, 2-pop, slates)
```

2) **Create bins & import assets into the template**
Open `ProjectTemplate.prproj` and set bins exactly how you want:
```
Media
  ├─ Video
  ├─ Audio
  ├─ Stills
  └─ Graphics
Assets
  ├─ AE_Comps
  ├─ Templates
  └─ SFX
Sequences
```
Then **import from the folders above** (02_Media/* and 03_Assets/*). This bakes your logos/SFX into the project so they’re instantly available on each new job.

3) **Pre-build your sequences & effects**
- Create a **Master_Sequence** (e.g., 3840×2160 23.976) with:
  - **Adjustment Layer stack** on top (Lumetri, sharpening, grain, etc).
  - **Lumetri**: click the “Input LUT” or Creative slot → **Browse** to a `.cube` in `03_Assets/LUTs/` (this keeps it portable; avoid installing system LUTs).
  - **Intro/Outro** clips, bumpers, slates, countdown/2-pop if you use them.
  - **Track layout** (A1 Dialogue, A2 Music, A3 SFX …).
  - **Submixes** DLG/MUS/SFX and a **Master** with Limiter (e.g., -1.0 dB ceiling) and Loudness Radar if you like to QC inside Premiere.
- Add a **Title/Lower-Third** graphic layer pre-styled. If you use MOGRTs:
  - Install them via Essential Graphics **into the project** (point to `03_Assets/MOGRTs`).
- Save the project. You now have a reusable `.prproj` that opens ready to edit.

4) **Dynamic Link (optional)**
If you want pre-built AE elements:
- Create `03_Assets/AE_Comps/BrandGraphics.aep`
- In Premiere, **Import** (not “Replace with AE Comp”) so the comp lives in **Assets/AE_Comps**. Save.
- When the template is copied by our script, the AEP comes along; Premiere will relink with a single click if needed.

5) **Presets**
- Effect/Export presets are user-level. Export your custom presets to files and keep them in `03_Assets/Templates/`:
  - **Export Presets** (`.epr`)
  - **Effect Presets** (`.prfpset`)
  - **Caption styles** (save to the project if you always use them)

> Tip: On a new machine, you just import these once. Your project still opens even without importing; you just won’t see the preset names until you import them.

# Important notes about linking
- Premiere prefers absolute paths, but if the **same folder names** exist inside the new project and files keep the **same names**, Premiere usually **auto-finds** or needs a quick one-time Relink (and then it relinks everything in that folder tree).
- Using **Lumetri → Browse to a .cube inside 03_Assets/LUTs** avoids the “install LUTs into system folders” trap.

# Make the template “first-class” in the script
You’ve already got the upgraded `newproj`. Just save your template here:
```
~/Video_Projects/_ProjectTemplate/01_ProjectFiles/ProjectTemplate.prproj
```
Now every time you run:
```bash
newproj -f /path/to/clip.mov -r -o "MyProject"
```
…it will copy `ProjectTemplate.prproj` to:
```
01_ProjectFiles/MyProject.prproj
```
with your bins, sequences, effects, and brand assets ready.

# (Optional) Add a few extra folders to the scaffold
If you want the template structure to include more slots by default (e.g., proxies & brand):

```bash
mkdir -p ~/Video_Projects/_ProjectTemplate/02_Media/Proxies
mkdir -p ~/Video_Projects/_ProjectTemplate/03_Assets/{Brand,MOGRTs,LUTs}
```

# If you want me to pre-wire it further
I can also patch the script to:
- **Add missing subfolders** (`Proxies`, `LUTs`, `MOGRTs`, `Brand`) on creation if your template doesn’t have them yet.
- Optionally **rename** the first ingested clip to match the project (you already have `-r`).
- Write a tiny **readme** pointing you straight to the `.prproj` file and your Master_Sequence.

If that sounds good, say the word and I’ll give you a tiny paste-in update that adds those folders automatically on each `newproj`.

---



---

okay

---



---

Perfect ✅ — here’s how you lock this in so every new project you spin up has your **pre-built Premiere template** (bins, sequences, effects, brand assets) and your `newproj` script keeps it tidy.

---

## 1. Build your template once
1. Open Premiere → File → **New Project**.  
2. Create the **bins** you want:  
   ```
   Media
     ├─ Video
     ├─ Audio
     ├─ Stills
     └─ Graphics
   Assets
     ├─ AE_Comps
     ├─ Templates
     └─ SFX
   Sequences
   ```
3. Import your **logos, SFX, LUTs, music beds, MOGRTs** into the right bins.  
4. Create a **Master_Sequence** with your effects stack (color LUT, limiter, audio submixes, adjustment layer, etc.).  
5. Save as:  
   ```
   ~/Video_Projects/_ProjectTemplate/01_ProjectFiles/ProjectTemplate.prproj
   ```

---

## 2. Put static assets in the scaffold
In Finder/Terminal, make folders for things you always want available:

```bash
mkdir -p ~/Video_Projects/_ProjectTemplate/02_Media/Proxies
mkdir -p ~/Video_Projects/_ProjectTemplate/03_Assets/{Brand,LUTs,MOGRTs}
```

Drop in:
- **Brand/** → original logo packs, colors  
- **LUTs/** → .cube files for Lumetri  
- **MOGRTs/** → Motion Graphics Templates  
- **SFX/** → whooshes, hits you always use  

---

## 3. Use `newproj` to spin up real projects
Now every time you run:

```bash
newproj -f ~/Desktop/clip.mov -r -o "Client_Video01"
```

It will:
- Copy the entire template folder.  
- Copy & rename `ProjectTemplate.prproj` to:  
  ```
  01_ProjectFiles/Client_Video01.prproj
  ```
- Ingest your selected video(s) into `02_Media/Video/`.  
- Rename the first video if you use `-r`.  
- Open the project folder in Finder (`-o`).  

---

## 4. Quick Action right-click workflow
With the Automator Quick Action we built earlier, you can:  
- Right-click on a clip in Finder → **Quick Actions → New Project from Selected Video…**  
- Enter a project name (pre-filled from the file).  
- Script auto-creates the structure + drops in your `.prproj` with bins/sequences already waiting.  

---

⚡ From now on you don’t have to touch Downloads or make bins manually.  
Every project you open in Premiere will *already* have:  
- Correct folder structure  
- Brand assets/logos  
- Pre-built Master Sequence with LUT/effects  
- Audio/SFX loaded  
- Media imported where it belongs  

---

👉 Do you want me to tweak your Quick Action so it also **always copies your logo(s) into 02_Media/Graphics** automatically, so you don’t even need to import them each time?

---

I thought it was supposed to copy everything in the template and in the bins. I thought that was what we were doing here.

---



---



---

Totally fair—here’s the key distinction:

- **Our script** copies the entire `_ProjectTemplate` folder **and** drops a **copy of your `.prproj` template** into `01_ProjectFiles/<ProjectName>.prproj`.  
- **Premiere bins + items** only show up if they’re already **inside that `.prproj` template**. Copying folders/files on disk doesn’t auto-import them into bins.

So if you open a freshly created project and the bins are empty, it means the **template project file** didn’t have those assets imported before you saved it.

# Fix it once (then it works forever)
1) Open your template project:
```
~/Video_Projects/_ProjectTemplate/01_ProjectFiles/ProjectTemplate.prproj
```
2) In Premiere, build the bins you want:
```
Media (Video, Audio, Stills, Graphics)
Assets (AE_Comps, Templates, SFX, Brand, LUTs, MOGRTs) ← if you want these too
Sequences
```
3) **Import the actual files** (logos, SFX, music beds, mogrts, LUTs-as-footage if you reference them, etc.) from your template folder paths, e.g.:
```
~/Video_Projects/_ProjectTemplate/02_Media/Audio/...
~/Video_Projects/_ProjectTemplate/02_Media/Graphics/...
~/Video_Projects/_ProjectTemplate/03_Assets/Brand/...
~/Video_Projects/_ProjectTemplate/03_Assets/SFX/...
```
4) (Optional) Create a **Master_Sequence** with your adjustment layer + effects, audio submixes, etc.  
5) **Save** the template project.

Now when you run `newproj …`, it will:
- Copy the whole `_ProjectTemplate` folder (so all those logo/SFX files exist in the new project’s 02/03 folders), **and**
- Copy `ProjectTemplate.prproj` → `01_ProjectFiles/<ProjectName>.prproj` **with your bins already populated**.

# Quick checklist to verify
- In Terminal, the script echoed:  
  `→ Premiere project created: /.../01_ProjectFiles/<ProjectName>.prproj`  
  (Open **that** file.)
- After opening, if anything is “Media Offline,” use **Link Media**, check **“Relink others automatically”**, and point to the new project’s `02_Media` / `03_Assets` folders. After first relink, everything should resolve.

# Why copying folders doesn’t fill bins
Premiere’s bins live **inside the .prproj**. The OS can copy files/folders, but only **Premiere** can “know” they belong in bins. That’s why we bake them into the template project once.

If you want, I can give you a super-short “template audit” list (what to import, how to set LUTs, audio submixes, MOGRTs) to ensure the template is perfect and portable.

---



---

no video was imported for the project when it was created

---



---

Got it — I see what’s happening from your screenshot. The bins and `Master_Sequence` **did come through correctly** from your template (✅), but the `.mov` you ingested with `newproj` is sitting in the folder on disk (`02_Media/Video/`) and not showing up inside Premiere yet.  

That’s because of how Premiere works:  
- **Bins + sequences live inside the `.prproj` file** (which we copied).  
- **Files on disk** don’t automatically appear in bins unless they were already imported *when you saved the template*.  

Right now, the script successfully copied your `.mov` into `02_Media/Video/`, but Premiere has no idea it should “see” that clip until you import it (File → Import, or drag from Finder).

---

## ✅ Two ways forward

### Option A: Keep it manual (simplest, most reliable)
1. Right after running `newproj`, open the `.prproj`.  
2. In Premiere, just **drag from `02_Media/Video/` into your “Video” bin**.  
   - Because the script always drops new files into the same folder path, this takes 2 seconds.

---

### Option B: Automate import (experimental)
Premiere doesn’t have a command-line way to auto-import clips, but there are two approaches:
- **Production/Team Project Templates** (Adobe’s built-in way to set up a template project with “watched folders”).  
- **ExtendScript / UXP panel** (small Premiere script/plugin that auto-imports all files found in `02_Media/Video/` on project open).

That would mean:  
- Every time you open a new project, Premiere would scan `02_Media/Video/` and import what it finds automatically.

---

👉 So right now, everything *is* working with your template. The only missing link is that Premiere won’t “auto-import” newly copied media.  

Would you like me to:  
1. Keep it simple and give you a **drag-and-drop workflow tip** (Option A), or  
2. Write you a tiny **Premiere ExtendScript** that auto-imports everything in `02_Media/Video/` on project open (Option B — more technical, but closer to your dream of “drop video → ready to edit”)?