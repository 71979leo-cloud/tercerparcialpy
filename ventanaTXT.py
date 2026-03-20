import tkinter as tk
from tkinter import messagebox

# --- FUNCIONES ---

def guardar_archivo():
    nombre = entrada_nombre.get()
    # Obtenemos el texto desde la línea 1, carácter 0 hasta el final
    contenido = cuadro_texto.get("1.0", tk.END)

    try:
        with open(nombre, "w") as archivo:
            archivo.write(contenido)
        messagebox.showinfo("Éxito", "Archivo guardado correctamente")
    except Exception:
        messagebox.showerror("Error", "No se pudo guardar el archivo")

def abrir_archivo():
    nombre = entrada_nombre.get()
    try:
        with open(nombre, "r") as archivo:
            contenido = archivo.read()
            cuadro_texto.delete("1.0", tk.END)
            cuadro_texto.insert(tk.END, contenido)
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo no existe")
    except Exception:
        messagebox.showerror("Error", "No se pudo abrir el archivo")

def agregar_texto():
    nombre = entrada_nombre.get()
    contenido = cuadro_texto.get("1.0", tk.END)
    try:
        with open(nombre, "a") as archivo:
            archivo.write(contenido)
        messagebox.showinfo("Éxito", "Texto agregado correctamente")
    except Exception:
        messagebox.showerror("Error", "No se pudo agregar el texto")

def limpiar_texto():
    cuadro_texto.delete("1.0", tk.END)


# --- INTERFAZ GRÁFICA (Lo que aparece en las fotos) ---

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Archivos de Texto")
ventana.geometry("500x400")

# Etiqueta nombre archivo
tk.Label(ventana, text="Nombre del archivo:").grid(row=0, column=0, padx=10, pady=10)

# Entrada del nombre
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.grid(row=0, column=1, padx=10, pady=10)

# Cuadro de texto
# El columnspan=3 es para que el cuadro ocupe el ancho de las columnas de abajo
cuadro_texto = tk.Text(ventana, width=60, height=15)
cuadro_texto.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# --- BOTONES ---

# Botón Guardar
btn_guardar = tk.Button(ventana, text="Guardar", width=12, command=guardar_archivo)
btn_guardar.grid(row=2, column=0, pady=10)

# Botón Abrir
btn_abrir = tk.Button(ventana, text="Abrir", width=12, command=abrir_archivo)
btn_abrir.grid(row=2, column=1)

# Botón Agregar
btn_agregar = tk.Button(ventana, text="Agregar", width=12, command=agregar_texto)
btn_agregar.grid(row=3, column=0)

# Botón Limpiar
btn_limpiar = tk.Button(ventana, text="Limpiar", width=12, command=limpiar_texto)
btn_limpiar.grid(row=3, column=1)

# Ejecutar aplicación
ventana.mainloop()