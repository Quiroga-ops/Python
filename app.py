import tkinter as tk
from tkinter import messagebox

def mostrar_popup():
    messagebox.showinfo("Título del Popup", "Sapa!🐸.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación Principal")
ventana.geometry("300x200")

# Botón para mostrar el popup
boton_popup = tk.Button(ventana, text="Presione aquí 😊", command=mostrar_popup)
boton_popup.pack(pady=20)

# Ejecutar la aplicación
ventana.mainloop()
