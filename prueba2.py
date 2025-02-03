import tkinter as tk
import yt_dlp
import subprocess
import threading


def convertir_a_argumentos(ydl_opts):
    argumentos = []
    
    # Recorremos las opciones y las convertimos a argumentos de línea de comandos
    if 'format' in ydl_opts:
        argumentos.extend(['-f', ydl_opts['format']])
    
    if 'outtmpl' in ydl_opts:
        argumentos.extend(['-o', ydl_opts['outtmpl']])
    
    if 'merge_output_format' in ydl_opts:
        argumentos.extend(['--merge-output-format', ydl_opts['merge_output_format']])
    
    if 'ignoreerrors' in ydl_opts:
        if ydl_opts['ignoreerrors']:
            argumentos.append('--ignore-errors')
    
    if 'noplaylist' in ydl_opts:
        if ydl_opts['noplaylist']:
            argumentos.append('--no-playlist')
    
    # Para los postprocesadores (si existen)
    if 'postprocessors' in ydl_opts:
        for postprocessor in ydl_opts['postprocessors']:
            if 'key' in postprocessor and postprocessor['key'] == 'FFmpegExtractAudio':
                argumentos.append('--extract-audio')
                if 'preferredcodec' in postprocessor:
                    argumentos.extend(['--audio-quality', postprocessor['preferredquality']])
                if 'preferredcodec' in postprocessor:
                    argumentos.extend(['--audio-format', postprocessor['preferredcodec']])
    
    return argumentos

def ejecutar():
    boton = radio_var.get()
    if boton == "1":
        funcion1()
    elif boton == "2":
        funcion2()

def funcion1():
    playlist_url = entrada.get()
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

def funcion2():
    playlist_url = entrada.get()
    print("boton2")
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

def redirigir_a_texto(text_widget, mensaje):
    text_widget.insert(tk.END, mensaje)
    text_widget.yview(tk.END)  # Desplazar hacia abajo

def ejecutar_descarga():
    playlist_url = entrada.get()
    # Opciones para descargar videos en la mejor calidad disponible
    boton = radio_var.get()
    if boton == "1":
        ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Video y audio en la mejor calidad
        'outtmpl': 'descargas/%(playlist)s/%(title)s.%(ext)s',  # Guarda en carpeta con nombre de la playlist
        'merge_output_format': 'mp4',  # Fuerza MP4 para mejor compatibilidad
        'ignoreerrors': True,  # Ignorar errores y continuar con la descarga
        'noplaylist': False,  # Asegurar que descargue toda la playlist
    }

    elif boton == "2":
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
    
    
        
    
    args = ['yt-dlp', playlist_url] + convertir_a_argumentos(ydl_opts)

    # Ejecutar el comando yt-dlp con los argumentos generados
    proceso = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Leer la salida línea por línea y actualizar la caja de texto
    for linea in iter(proceso.stdout.readline, ''):
        redirigir_a_texto(text_box, linea)
        root.update_idletasks()  # Actualizar la interfaz gráfica

    # Esperar a que el proceso termine
    proceso.stdout.close()
    proceso.wait()

# Crear la ventana principal
root = tk.Tk()
root.title("youtube download tool")  # Título de la ventana
root.geometry("600x400")  # Tamaño de la ventana (ancho x alto)

# Aquí agregarás widgets (botones, etiquetas, etc.)
label = tk.Label(root, text="youtube download tool")
label.pack()  # Agrega la etiqueta a la ventana

label = tk.Label(root, text="¿quiere descargar el video o solo el audio?")
label.pack()

radio_var = tk.StringVar(value="1")

radio1 = tk.Radiobutton(root, text="video", variable=radio_var, value="1")
radio1.pack()

radio2 = tk.Radiobutton(root, text="audio", variable=radio_var, value="2")
radio2.pack()

label = tk.Label(root, text="introduzca el link de la playlist")
label.pack()  # Agrega la etiqueta a la ventana

entrada = tk.Entry(root, width=30)
entrada.pack()

button = tk.Button(root, text="Obtener descarga", command=lambda: threading.Thread(target=ejecutar_descarga, daemon=True).start())
button.pack()

# Crear la caja de texto con desplazamiento
text_box = tk.Text(root, height=50, width=500)
text_box.pack(padx=10, pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()
