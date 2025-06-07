import yt_dlp
import os

def download_video(link):
    # Obtener la ruta de la carpeta de Descargas del usuario
    downloads_path = os.path.join(os.path.expanduser("~"), "Descargas")  

    ydl_opts = {
        "format": "bestvideo[height>=1080]+bestaudio/best[height>=1080]/best",  # Descargar video en 1080p o superior si está disponible
        "outtmpl": os.path.join(downloads_path, "%(title)s.%(ext)s"),  # Guardar en la carpeta Descargas
        "merge_output_format": "mp4",  # Unir audio y video en formato MP4
        "noplaylist": True,  # Evitar descargar listas de reproducción si se proporciona un enlace de lista
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Descarga completa")

    except Exception as e:
        print(f"Hubo un error al descargar el video: {e}")

# No debe haber ninguna llamada a download_video aquí
