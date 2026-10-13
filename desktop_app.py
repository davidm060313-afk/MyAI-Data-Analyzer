import os, sys, threading, time, webbrowser
from pathlib import Path
from werkzeug.serving import make_server

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DATA_DIR", str(ROOT / "data"))

from app import app

class ServerThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.server = make_server("127.0.0.1", int(os.getenv("PORT", "5177")), app)
        self.ctx = app.app_context()
        self.ctx.push()
    def run(self):
        self.server.serve_forever()
    def stop(self):
        self.server.shutdown()

def main():
    server = ServerThread()
    server.start()
    url = f"http://127.0.0.1:{os.getenv('PORT', '5177')}"
    time.sleep(0.5)
    try:
        import webview
        window = webview.create_window("MyAI Data Analyzer", url, width=1180, height=820, min_size=(760, 560))
        webview.start()
    except ImportError:
        print("pywebview is not installed; opening the app in your default browser.")
        webbrowser.open(url)
        print("Leave this terminal open while using the app. Press Ctrl+C to stop.")
        try:
            while True: time.sleep(1)
        except KeyboardInterrupt:
            pass
    finally:
        server.stop()

if __name__ == "__main__":
    main()
