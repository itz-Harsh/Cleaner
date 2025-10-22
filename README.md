
# 🧹 Cleaner — Windows Temp & Junk Cleaner

Keep your Windows PC tidy with a tiny, focused cleaner script that removes common temporary files and empties the Recycle Bin.

This project provides a simple, single-file Python utility aimed at power users who want an easy way to reclaim disk space quickly.

## ✨ Highlights

- 🗑️ Cleans Windows Prefetch, system Temp, and the current user's %temp% directory
- ♻️ Empties the Recycle Bin
- ⚡ Zero-config: single-file script (`main.py`) and an optional `cleaner.bat` wrapper
- 🛡️ Notes and safety tips included — use with care

## 📦 Requirements

- 🐍 Python 3.x (recommended 3.8+)
- No additional packages required for the core script

Optional (only if you extend the project for GUI automation):

- 🤖 `pyautogui` (install with `pip install pyautogui`)

## 🚀 Quick start

1. (Optional) Create a virtual environment and activate it.

2. Run the script directly from PowerShell or Command Prompt (run as Administrator for best results):

```powershell
python main.py
```

Or use the bundled batch file:

```powershell
.\cleaner.bat
```

## 🧭 What the script does

- Deletes files in `C:\Windows\Prefetch`
- Clears the user Temp folder: `%USERPROFILE%\AppData\Local\Temp`
- Deletes files in `C:\Windows\Temp`
- Removes `C:\$Recycle.Bin` (empties Recycle Bin)

Each step includes a short pause so you can see progress if running interactively.

## ⚠️ Important safety notes

- This script permanently deletes files. There is no recycle/undo for the actions it performs.
- Only run on Windows systems you trust. Running as Administrator increases the scope of deletions.
- Review `main.py` before running if you're unsure what will be removed.

## 🔧 Extending or customizing

- Add logging before each deletion to review which files will be removed.
- Add a dry-run mode that lists files without deleting them.
- Wrap destructive commands in additional confirmation prompts.

## 🧪 Testing locally

- Test on a non-production or virtual machine first.
- Consider creating a backup or System Restore point before running.

## 📝 License & Disclaimer

Use at your own risk. The author is not responsible for data loss or system damage caused by running this script.

---

If you'd like, I can:

- add a dry-run mode to `main.py` that lists files before deleting them
- add a simple logging feature
- create a small PowerShell GUI front-end

Tell me which you'd prefer and I'll implement it.
