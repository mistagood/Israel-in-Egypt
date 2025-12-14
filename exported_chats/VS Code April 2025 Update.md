# VS Code April 2025 Update



---

April 2025 (version 1.100)

Show release notes after an update

Release date: May 8, 2025

Update: Enable Next Edit Suggestions (NES) by default in VS Code Stable (more...).

Update 1.100.1: The update addresses these security issues.

Update 1.100.2: The update addresses these issues.

Welcome to the April 2025 release of Visual Studio Code. There are many updates in this version that we hope you'll like, some of the key highlights include:

Chat

Custom instructions and reusable prompts (more...).
Smarter results with tools for GitHub, extensions, and notebooks (more...).
Image and Streamable HTTP support for MCP (more...).
Chat performance

Faster responses on repeat chat requests (more...).
Faster edits in agent mode (more...).
Editor experience

Improved multi-window support for chat and editors (more...).
Staged changes now easier to identify (more...).
If you'd like to read these release notes online, go to Updates on code.visualstudio.com. Insiders: Want to try new features as soon as possible? You can download the nightly Insiders build and try the latest updates as soon as they are available.

Chat
Prompt and instructions files
You can tailor your AI experience in VS Code to your specific coding practices and technology stack by using Markdown-based instructions and prompt files. We've aligned the implementation and usage of these two related concepts, however they each have distinct purposes.

Instructions files
Setting:   chat.instructionsFilesLocations

Instructions files (also known as custom instructions or rules) provide a way to describe common guidelines and context for the AI model in a Markdown file, such as code style rules, or which frameworks to use. Instructions files are not standalone chat requests, but rather provide context that you can apply to a chat request.

Instructions files use the .instructions.md file suffix. They can be located in your user data folder or in the workspace. The   chat.instructionsFilesLocations setting lists the folders that contain instruction files.

You can manually attach instructions to a specific chat request, or they can be automatically added:

To add them manually, use the Add Context button in the Chat view, and then select Instructions.... Alternatively use the Chat: Attach Instructions... command from the Command Palette. This brings up a picker that lets you select existing instructions files or create a new one to attach.

To automatically add instructions to a prompt, add the applyTo Front Matter header to the instructions file to indicate which files the instructions apply to. If a chat request contains a file that matches the given glob pattern, the instructions file is automatically attached.

The following example provides instructions for TypeScript files (applyTo: '**/*.ts'):

---
applyTo: '**/*.ts'
---
Place curly braces on separate lines for multi-line blocks:
if (condition)
{
  doSomething();
}
else
{
  doSomethingElse();
}

You can create instruction files with the Chat: New Instructions File... command. Moreover, the files created in the user data folder can be automatically synchronized across multiple user machines through the Settings Sync service. Make sure to check the Prompts and Instructions option in the Backup and Sync Settings... dialog.

Learn more about instruction files in our documentation.

Prompt files
Setting:   chat.promptFilesLocations

Prompt files describe a standalone, complete chat request, including the prompt text, chat mode, and tools to use. Prompt files are useful for creating reusable chat requests for common tasks. For example, you can add a prompt file for creating a front-end component, or to perform a security review.

Prompt files use the .prompt.md file suffix. They can be located in your user data folder or in the workspace. The   chat.promptFilesLocations setting lists the folder where prompt files are looked for.

There are several ways to run a prompt file:

Type / in the chat input field, followed by the prompt file name. Screenshot that shows running a prompt in the Chat view with a slash command.

Open the prompt file in an editor and press the 'Play' button in the editor tool bar. This enables you to quickly iterate on the prompt and run it without having to switch back to the Chat view. Screenshot that shows running a prompt by using the play button in the editor.

Use the Chat: Run Prompt File... command from the Command Palette.

Prompt files can have the following Front Matter metadata headers to indicate how they should be run:

mode: the chat mode to use when invoking the prompt (ask, edit, or agent mode).
tools: if the mode is agent, the list of tools that are available for the prompt.
The following example shows a prompt file for generating release notes, that runs in agent mode, and can use a set of tools:

---
mode: 'agent'
tools: ['getCurrentMilestone', 'getReleaseFeatures', 'file_search', 'semantic_search', 'read_file', 'insert_edit_into_file', 'create_file', 'replace_string_in_file', 'fetch_webpage', 'vscode_search_extensions_internal']
---
Generate release notes for the features I worked in the current release and update them in the release notes file. Use [release notes writing instructions file](.github/instructions/release-notes-writing.instructions.md) as a guide.

To create a prompt file, use the Chat: New Prompt File... command from the Command Palette.

Learn more about prompt files in our documentation.

Improvements and notes
Instructions and prompt files now have their own language IDs, configurable in the language mode dialog for any file open document ("Prompt" and "Instructions" respectively). This allows, for instance, using untitled documents as temporary prompt files before saving them as files to disk.
We renamed the Chat: Use Prompt command to Chat: Run Prompt. Furthermore, the command now runs the selected prompt immediately, as opposed to attaching it as chat context as it did before.
Both file types now also support the description metadata in their headers, providing a common place for short and user-friendly prompt summaries. In the future, this header is planned to be used along with the applyTo header as the rule that determines if the file needs to be auto-included with chat requests (for example, description: 'Code style rules for front-end components written in TypeScript.')
Faster agent mode edits


so what can I do with this?

---



---

The April 2025 update to Visual Studio Code (version 1.100) introduces powerful new features specifically designed to **streamline your AI coding workflows** using **custom instructions** and **reusable prompt files**.

Here’s what you can do with these features — and **why they’re a game-changer** if you're building or automating with AI:

---

## ✅ **1. Set AI Guidelines with `.instructions.md` Files**
You can **create reusable AI behavior rules** in Markdown format, known as **Instructions Files**.

### ✨ Example Use Cases:
- Define your **code style guide** (e.g., brace placement, naming conventions).
- Set **framework-specific rules** (e.g., use `Next.js` for frontends, or enforce `async/await`).
- Tailor behavior for **different file types** (TypeScript, Python, etc).

### 🔧 How it works:
- Create `.instructions.md` files.
- Add an `applyTo` header to specify when they apply (e.g., `applyTo: "**/*.ts"`).
- VS Code **automatically adds them to chat sessions** involving those file types.

---

## ✅ **2. Build Reusable Chat Prompts with `.prompt.md` Files**
Prompt files are **ready-to-run chat requests** that can include:
- Prompt text
- Chat mode (`ask`, `edit`, or `agent`)
- Tools to invoke (file search, semantic search, etc.)

### ✨ Example Use Cases:
- A prompt that always performs a **security audit**.
- One that helps you **create a new component** with your chosen stack.
- A prompt that **summarizes a file** using AI.

### ⚙️ How to use:
- Save `.prompt.md` files in the configured folders.
- Run them via:
  - `/filename` in the chat input
  - "Play" button inside the editor
  - `Chat: Run Prompt File...` in Command Palette

---

## ✅ **3. Sync Across Machines**
If you enable **Settings Sync**, you can:
- Sync both prompts and instructions across multiple devices.
- Stay consistent with your team or across projects.

---

## ✅ **4. Supercharged Agent Mode with Tool Access**
When using **Agent Mode**:
- Prompts can access internal tools like:
  - `semantic_search`
  - `insert_edit_into_file`
  - `file_search`
  - `vscode_search_extensions_internal`

### 🔧 Example Prompt:
```markdown
---
mode: 'agent'
tools: ['file_search', 'read_file', 'insert_edit_into_file']
---
Summarize all TODO comments in the current workspace and create a checklist in `tasks.md`.
```

---

## 🧠 **Why this Matters (especially for power users, devs, and researchers):**
You can now **automate workflows** like:
- Setting AI coding standards for your team.
- Embedding custom knowledge into AI tools.
- Creating "smart buttons" for repeat coding tasks.
- Auto-attach instructions to AI chats for specific file types.
- Maintain consistent documentation, release notes, or coding styles with AI support.

---

## 🔨 Getting Started
1. Use **`Chat: New Instructions File...`** to create coding rules.
2. Use **`Chat: New Prompt File...`** to build AI task automations.
3. Run a prompt by typing `/yourPromptName` in the Chat input or pressing **Play** in the editor.

---

If you're doing **AI-assisted coding**, **documentation generation**, or building **custom workflows**, this update gives you the power to **train your tools to act more like your team**.

Let me know what specific tasks you're working on, and I can help you draft instructions or prompts that fit your workflow.