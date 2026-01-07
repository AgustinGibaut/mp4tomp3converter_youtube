import os
import sys
import subprocess
from pathlib import Path
from typing import Optional

class AudioDownloader:
    
    def __init__(self, output_dir: str = "audios"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.output_template = str(self.output_dir / "%(title)s.%(ext)s")

    def _get_yt_dlp_command(self, url: str) -> list[str]:
        return [
            sys.executable, "-m", "yt_dlp",
            url,
            "--extract-audio",
            "--audio-format", "mp3",
            "--no-playlist",
            "--quiet",
            "--no-warnings",
            "--ignore-errors",
            "-o", self.output_template
        ]

    def download(self, url: str) -> bool:
        print(f"\n [Iniciando] Procesando: {url}")
        
        try:
            process = subprocess.Popen(
                self._get_yt_dlp_command(url),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            process.communicate()

            return any(self.output_dir.iterdir())

        except Exception as e:
            print(f"DEBUG: Error interno: {e}")
            return False

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("="*40)
    print("      YOUTUBE TO MP3 CONVERTER")
    print("="*40)

    url = input("\n Ingrese la URL: ").strip()
    
    if not url:
        print("  Error: La URL no puede estar vacía.")
        return

    downloader = AudioDownloader()
    
    if downloader.download(url):
        print(f"\n Finalizado: Audio disponible en '{downloader.output_dir}'")
    else:
        print("\n Error: No se pudo procesar la descarga.")

if __name__ == "__main__":
    main()