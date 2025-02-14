# youtube_download

## Descripción
Este programa permite descargar playlists de YouTube en formato de audio (MP3) o video (MP4) utilizando la biblioteca `yt_dlp`.

Cuenta con una interfaz de consola que solicita al usuario la URL de la playlist y su preferencia de descarga (audio o video). Los archivos descargados se guardan en la carpeta `descargas/` dentro de una subcarpeta con el nombre de la playlist.

## Dependencias
Para ejecutar este programa, es necesario instalar las siguientes dependencias:

- `yt-dlp` (para descargar videos y audios desde YouTube)
- `ffmpeg` (para la conversión de audio a MP3)

### Instalación de dependencias
Ejecute los siguientes comandos para instalar las dependencias necesarias:

```sh
pip install yt-dlp
```

Además, asegúrese de que `ffmpeg` esté instalado en su sistema. Puede instalarlo con:

- En Windows: [Descargar FFmpeg](https://ffmpeg.org/download.html)
- En Linux (Debian/Ubuntu):
  ```sh
  sudo apt install ffmpeg
  ```
- En macOS:
  ```sh
  brew install ffmpeg
  ```

## Uso

1. Ejecute el script en la terminal:
   ```sh
   python youtube_download.py
   ```
2. Seleccione si desea descargar solo el audio o el video.
3. Introduzca la URL de la playlist cuando se le solicite.
4. Espere a que la descarga se complete.

## Características
- Descarga de listas de reproducción completas.
- Opción para descargar solo audio en formato MP3 con calidad de 192 kbps.
- Opción para descargar videos en la mejor calidad disponible y convertirlos a MP4.
- Manejo de errores para evitar interrupciones durante la descarga.

## Versión con Interfaz Gráfica (GUI)
Actualmente, se encuentra en desarrollo una versión con interfaz gráfica en fase alfa. Esta versión permitirá una experiencia más amigable para los usuarios que prefieran una interacción visual en lugar de la línea de comandos.

## Información del Autor
- **Autor:** Majora2004
- **Nombre del proyecto:** youtube_download
- **Versión:** 1.1

