import tkinter as tk
from tkinter import messagebox
import requests
import socket

# ======== VERSIÓN LOCAL ========
LOCAL_VERSION = "2.0.0"
GITHUB_VERSION_URL = "https://raw.githubusercontent.com/PieroZavalaAyala/actualizadoralpha/main/version.txt"
ACTUALIZACION_URL = "https://github.com/PieroZavalaAyala/actualizadoralpha.git"  # Cambia esto por el enlace a tu repo

# ======== FUNCIONES DE CÁLCULO ========
def sumar():
    try:
        resultado = float(entry1.get()) + float(entry2.get())
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa solo números")

def restar():
    try:
        resultado = float(entry1.get()) - float(entry2.get())
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa solo números")

def multiplicar():
    try:
        resultado = float(entry1.get()) * float(entry2.get())
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa solo números")

def dividir():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Error", "No se puede dividir entre cero.")
        else:
            resultado = num1 / num2
            label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa solo números")

def limpiar():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    label_resultado.config(text="Resultado:")

# ======== FUNCIÓN PARA VERIFICAR CONEXIÓN A INTERNET ========
def verificar_conexion():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

# ======== FUNCIÓN PARA BUSCAR ACTUALIZACIONES ========
def buscar_actualizaciones():
    if not verificar_conexion():
        messagebox.showerror("Error", "No hay conexión a internet.")
        return

    try:
        response = requests.get(GITHUB_VERSION_URL)
        if response.status_code == 200:
            version_online = response.text.strip()
            if version_online > LOCAL_VERSION:
                mensaje = f"¡Hay una nueva versión disponible! ({version_online})\n\nPuedes descargarla desde:\n{ACTUALIZACION_URL}"
                messagebox.showinfo("Actualización disponible", mensaje)
            else:
                messagebox.showinfo("Sin actualizaciones", "Ya tienes la última versión.")
        else:
            messagebox.showerror("Error", "No se pudo verificar la actualización.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar al servidor.\n{e}")

# ======== UI PRINCIPAL ========
root = tk.Tk()
root.title("Calculadora Básica")

tk.Label(root, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

btn_sumar = tk.Button(root, text="Sumar", command=sumar)
btn_sumar.grid(row=2, column=0, padx=5, pady=5)

btn_restar = tk.Button(root, text="Restar", command=restar)
btn_restar.grid(row=2, column=1, padx=5, pady=5)

btn_multiplicar = tk.Button(root, text="Multiplicar", command=multiplicar)
btn_multiplicar.grid(row=3, column=0, padx=5, pady=5)

btn_dividir = tk.Button(root, text="Dividir", command=dividir)
btn_dividir.grid(row=3, column=1, padx=5, pady=5)

btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar, bg="#f0ad4e", fg="white")
btn_limpiar.grid(row=4, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(root, text="Resultado:")
label_resultado.grid(row=5, column=0, columnspan=2)

btn_actualizar = tk.Button(root, text="Buscar actualizaciones", command=buscar_actualizaciones, bg="#007acc", fg="white")
btn_actualizar.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
