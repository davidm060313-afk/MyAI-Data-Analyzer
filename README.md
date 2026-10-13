# MyAI Data Analyzer

A beginner-friendly Flask web app for Linux Mint and Windows. It uploads files, extracts available text, asks an AI service to analyze the extracted content, and saves item metadata and analysis in SQLite (local) or PostgreSQL (cloud).

## Supported files
- Text/notes/posts: TXT, Markdown, JSON
- Documents: PDF, DOCX
- Data: CSV, XLSX (Excel)
- Images: PNG, JPG/JPEG, WEBP, BMP (OCR is optional)
- Audio/video: MP3, WAV, M4A, OGG, MP4, MOV, WEBM, MKV (speech transcription is optional)

## Important limits
- This starter does not automatically log in to or scrape social networks. Export your own posts or paste them into a TXT/CSV file and upload that.
- AI analyzes extracted text. For video/audio, install the optional Whisper and FFmpeg components. For images, install Tesseract OCR. It does not magically understand a video if transcription/frame extraction is unavailable.
- The included local file storage works on your computer. For Render, the included `render.yaml` uses a persistent disk for uploaded files; add a PostgreSQL database and set `DATABASE_URL`. Render disks and PostgreSQL may have paid-plan requirements. A persistent disk attaches to one service/region and is not shared between replicas.
- Add login/authentication before making this internet-facing. This starter is not a multi-user secured product yet; do not upload private or sensitive files to a public deployment.
- Never put API keys in source code or commit `.env` to Git.

## Linux Mint setup
1. Install Python and venv:
   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip
   ```
2. Unzip the project, open Terminal in its folder, and run:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   cp .env.example .env
   ```
3. Edit `.env` in a text editor. Set `MYAI_API_URL` to your actual MyAI JSON API endpoint, or set `GEMINI_API_KEY`. Keep keys private.
4. Start the app:
   ```bash
   python app.py
   ```
5. Open `http://127.0.0.1:5000` in your browser. To stop it, press Ctrl+C in Terminal.

### Optional image OCR on Linux Mint
```bash
sudo apt install tesseract-ocr ffmpeg
source .venv/bin/activate
pip install pytesseract openai-whisper
```
Whisper can require substantial disk space and processing time. Try a small audio clip first.

## Windows setup
1. Install Python 3.12 or newer from https://www.python.org/downloads/ and enable “Add Python to PATH”.
2. Extract the ZIP. Open PowerShell in the extracted folder:
   ```powershell
   py -3 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   Copy-Item .env.example .env
   ```
3. Edit `.env` in Notepad and set `MYAI_API_URL` or `GEMINI_API_KEY`.
4. Run:
   ```powershell
   python app.py
   ```
5. Open `http://127.0.0.1:5000`.

## Connecting to your existing MyAI
Set `MYAI_API_URL` to the exact URL of the JSON endpoint. The code sends a POST JSON body containing both `message` and `prompt`. It tries to read a JSON response field named `response`, `answer`, `reply`, `text`, or `content`.

Your existing MySpace `/api/ai` route may require a logged-in session cookie or CSRF token. If so, this app cannot connect with only a URL; use the direct Gemini API key as the simplest initial connection, or add a dedicated authenticated API token endpoint to MySpace. Do not put your personal website login password into this app.

## Cloud deployment overview (Render)
1. Put the extracted project in a new GitHub repository.
2. Create a PostgreSQL database in Render and copy its **internal** connection URL.
3. Create a web service from the repository. The `render.yaml` can help configure it.
4. Add environment variables `DATABASE_URL`, `MYAI_API_URL`, and either `GEMINI_API_KEY` or the MyAI endpoint credentials.
5. The included disk config stores uploads at `/var/data`. Confirm your Render plan supports persistent disks before deploying.
6. Add login, per-user ownership checks, rate limiting, and file-scanning before allowing other people to use it.

## Database migration note
The first version creates its table automatically. If changing `DATABASE_URL` after using the app, existing local items will not automatically be copied to the cloud database.

## Troubleshooting
- `AI is not connected yet`: set a valid AI endpoint or Gemini API key in `.env`, then restart.
- `401/403` from MyAI: its endpoint likely requires a login session or token; use Gemini key or add a proper API token endpoint.
- Excel error: ensure `openpyxl` installed.
- PDF with no extracted text: it may be a scanned image; OCR is needed.
- Audio/video transcription errors: install FFmpeg and `openai-whisper`. Whisper may not install on every Python/hardware setup; skip it if installation is difficult.
- Cloud says file missing: ensure persistent disk is mounted at the same `DATA_DIR` and database rows point to that storage.
