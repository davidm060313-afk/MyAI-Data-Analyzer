# MyAI Data Analyzer — Desktop App edition

This edition opens as a desktop window on Linux Mint and Windows using pywebview. If pywebview's desktop engine is unavailable, it falls back to your browser. It still stores data locally by default.

## Linux Mint
1. Extract this folder.
2. Open Terminal inside the extracted folder.
3. Run:
   ```bash
   sudo apt update
   sudo apt install python3-venv python3-pip python3-tk
   ./run_linux.sh
   ```
4. First launch installs Python dependencies. It will create `.env` if missing.
5. Edit `.env` and add `MYAI_API_URL` or `GEMINI_API_KEY`, then launch again.

If the native window cannot start, install WebKitGTK:
```bash
sudo apt install gir1.2-webkit2-4.1
```
If that package is unavailable on your Mint version, use the browser fallback or consult pywebview Linux dependencies.

## Windows
1. Install Python 3.12+ from https://www.python.org/downloads/ (enable Add Python to PATH).
2. Double-click `run_windows.bat`.
3. On first run, dependencies install automatically and `.env` is created.
4. Edit `.env` with your AI connection, then double-click the launcher again.

## Notes
- This is a desktop window around the included web application, not a fully native Windows/Linux widget interface.
- Files remain local unless you separately configure a cloud database/storage service.
- Don't deploy the current starter publicly before adding login and per-user access controls.
