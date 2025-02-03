import tkinter as tk
import yt_dlp

# Crear la ventana principal
root = tk.Tk()
root.title("youtube download tool")  # Título de la ventana
root.geometry("400x300")      # Tamaño de la ventana (ancho x alto)

#las funciones del programa aqui
def ejecutar():
    boton=radio_var.get()
    if boton == "1" :
        funcion1()
    elif boton== "2":
        funcion2()

def funcion1():
    playlist_url  = entrada.get()
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


# Aquí agregarás widgets (botones, etiquetas, etc.)
label=tk.Label(root, text="youtube download tool")
label.pack()  # Agrega la etiqueta a la ventana

label=tk.Label(root, text="¿quiere decargar el video o solo el audio?")
label.pack()

radio_var = tk.StringVar(value="1")

radio1 = tk.Radiobutton(root, text="video", variable=radio_var, value="1")
radio1.pack()

radio2= tk.Radiobutton(root, text="audio", variable=radio_var, value="2")
radio2.pack()



label=tk.Label(root, text="introduzca el link de la plylist")
label.pack()  # Agrega la etiqueta a la ventana

entrada = tk.Entry(root, width=30)
entrada.pack()

button = tk.Button(root, text="Obtener descarga", command=ejecutar)
button.pack()
# Iniciar el bucle principal de la aplicación
text_box = tk.Text(root, height=10, width=50)
text_box.pack(padx=10, pady=10)


root.mainloop()