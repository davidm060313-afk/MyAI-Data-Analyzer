@echo off
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe py -3 -m venv .venv
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements-desktop.txt
if not exist .env copy .env.example .env
python desktop_app.py
pause
