import yt_dlp
import os

def download_video(link):
    downloads_path = os.path.join(os.path.expanduser("~"), "Descargas")

    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": os.path.join(downloads_path, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",  # Convierte el video a mp4 si es necesario
            }
        ],
        "noplaylist": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("✅ Descarga completa")
    except Exception as e:
        print(f"❌ Hubo un error al descargar el video: {e}")
