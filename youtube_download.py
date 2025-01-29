import yt_dlp

def download_playlist_audio(playlist_url):
    # Opciones para descargar solo el audio en MP3
    ydl_opts = {
        'format': 'bestaudio/best',  # Mejor calidad de audio disponible
        'outtmpl': 'descargas/%(playlist)s/%(title)s.%(ext)s',  # Guarda en carpeta con nombre de la playlist
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extrae el audio del video
            'preferredcodec': 'mp3',  # Convierte a MP3
            'preferredquality': '192',  # Calidad de 192 kbps
        }],
        'ignoreerrors': True,  # Ignorar errores y seguir con la descarga
        'noplaylist': False,  # Permitir la descarga de listas de reproducción
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

    print("¡Descarga de la playlist completada!")

def download_playlist_videos(playlist_url):
    # Opciones para descargar videos en la mejor calidad disponible
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Video y audio en la mejor calidad
        'outtmpl': 'descargas/%(playlist)s/%(title)s.%(ext)s',  # Guarda en carpeta con nombre de la playlist
        'merge_output_format': 'mp4',  # Fuerza MP4 para mejor compatibilidad
        'ignoreerrors': True,  # Ignorar errores y continuar con la descarga
        'noplaylist': False,  # Asegurar que descargue toda la playlist
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

    print("¡Descarga de la playlist completada!")



print("quiere descargar el video o solo el audio: SI/NO")
vid= input()
if vid=="no":
    print("Escribe la URL de la playlist:")
    playlist_url = input().strip()
    download_playlist_audio(playlist_url)
elif vid=="si":
    print("Escribe la URL de la playlist:")
    playlist_url = input().strip()
    download_playlist_videos(playlist_url)


    
    

