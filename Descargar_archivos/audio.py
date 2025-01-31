import yt_dlp
import os

def download_audio(link):
    # Obtener la ruta de la carpeta de Descargas del usuario
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

    ydl_opts = {
        "format": "bestaudio/best",  # Descargar la mejor calidad de audio disponible
        "outtmpl": os.path.join(downloads_path, "%(title)s.%(ext)s"),  # Guardar en la carpeta Descargas
        "extract_flat": True, # Extraer solo el audio
        "noplaylist": True,  # Evitar descargar listas de reproducción si se proporciona un enlace de lista
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Descarga completa")

    except Exception as e:
        print(f"Hubo un error al descargar el audio: {e}")

link = str(input("Pega el link de la canción a descargar:  ")).strip()
download_audio(link)