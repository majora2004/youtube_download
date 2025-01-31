import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Mi Primera App")  # Título de la ventana
root.geometry("400x300")      # Tamaño de la ventana (ancho x alto)

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

def get_radio():
    print("Opción seleccionada:", radio_var.get())

button = tk.Button(root, text="Obtener descarga", command=get_radio)
button.pack()
# Iniciar el bucle principal de la aplicación

label=tk.Label(root, text="introduzca el link de la plylist")
label.pack()  # Agrega la etiqueta a la ventana
root.mainloop()