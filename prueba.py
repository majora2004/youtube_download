import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Mi Primera App")  # Título de la ventana
root.geometry("400x300")      # Tamaño de la ventana (ancho x alto)

# Aquí agregarás widgets (botones, etiquetas, etc.)
label=tk.Label(root, text="hola caracola")
label.pack()  # Agrega la etiqueta a la ventana


def on_button_click():
    print("arriba españa")

# Iniciar el bucle principal de la aplicación
root.mainloop()