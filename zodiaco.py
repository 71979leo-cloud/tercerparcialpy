import tkinter as tk
from PIL import Image, ImageTk 

def obtener_signo():
    nombre = entry_nombre.get().lower()
    apellido_paterno = entry_apellido_paterno.get().lower()
    apellido_materno = entry_apellido_materno.get().lower()
    

    dia_nac = int(entry_dia.get())
    mes_nac = int(entry_mes.get())
    año_nac = int(entry_año.get())

    dia_actual = 10
    mes_actual = 4
    año_actual = 2026

    edad = año_actual - año_nac


    if (mes_actual < mes_nac) or (mes_actual == mes_nac and dia_actual < dia_nac):
        edad = edad - 1

    residuo = (año_nac - 1900) % 12
    
    if residuo == 0: animal = "rata"; archivo_foto = "rata.png"
    if residuo == 1: animal = "buey"; archivo_foto = "buey.png"
    if residuo == 2: animal = "tigre"; archivo_foto = "tigre.png"
    if residuo == 3: animal = "conejo"; archivo_foto = "conejo.png"
    if residuo == 4: animal = "dragón"; archivo_foto = "dragon.png"
    if residuo == 5: animal = "serpiente"; archivo_foto = "serpiente.png"
    if residuo == 6: animal = "caballo"; archivo_foto = "caballo.png"
    if residuo == 7: animal = "cabra"; archivo_foto = "cabra.png"
    if residuo == 8: animal = "mono"; archivo_foto = "mono.png"
    if residuo == 9: animal = "gallo"; archivo_foto = "gallo.png"
    if residuo == 10: animal = "perro"; archivo_foto = "perro.png"
    if residuo == 11: animal = "cerdo"; archivo_foto = "cerdo.png"

    lbl_saludo.config(text=f"Hola {nombre} {apellido_paterno} {apellido_materno}")
    lbl_edad.config(text=f"Tienes {edad} años")
    lbl_signo_nombre.config(text=f"Es {animal}")

    try:
        archivo = Image.open(archivo_foto)
        nueva_imagen = archivo.resize((60, 60))
        foto = ImageTk.PhotoImage(nueva_imagen)
        lbl_imagen.config(image=foto)
        lbl_imagen.image = foto
    except:
        lbl_imagen.config(image="")

def limpiar_datos():
    entry_nombre.delete(0, tk.END)
    entry_apellido_paterno.delete(0, tk.END)
    entry_apellido_materno.delete(0, tk.END)
    entry_dia.delete(0, tk.END)
    entry_mes.delete(0, tk.END)
    entry_año.delete(0, tk.END)
    opcion_sexo.set("") 
    lbl_saludo.config(text="")
    lbl_edad.config(text="")
    lbl_signo_nombre.config(text="")
    lbl_imagen.config(image="")

ventana = tk.Tk()
ventana.title("Zodiaco Chino")

# Entradas
tk.Label(ventana, text="Nombre").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Apellido Paterno").grid(row=1, column=0)
entry_apellido_paterno = tk.Entry(ventana)
entry_apellido_paterno.grid(row=1, column=1)

tk.Label(ventana, text="Apellido Materno").grid(row=2, column=0)
entry_apellido_materno = tk.Entry(ventana)
entry_apellido_materno.grid(row=2, column=1)

tk.Label(ventana, text="Día Nac").grid(row=3, column=0)
entry_dia = tk.Entry(ventana)
entry_dia.grid(row=3, column=1)

tk.Label(ventana, text="Mes Nac").grid(row=4, column=0)
entry_mes = tk.Entry(ventana)
entry_mes.grid(row=4, column=1)

tk.Label(ventana, text="Año Nac").grid(row=5, column=0)
entry_año = tk.Entry(ventana)
entry_año.grid(row=5, column=1)

tk.Label(ventana, text="Sexo").grid(row=6, column=0)
opcion_sexo = tk.StringVar()
tk.Radiobutton(ventana, text="Masculino", variable=opcion_sexo, value="m").grid(row=7, column=0)
tk.Radiobutton(ventana, text="Femenino", variable=opcion_sexo, value="f").grid(row=8, column=0)

tk.Button(ventana, text="Imprimir", command=obtener_signo).grid(row=9, column=0)
tk.Button(ventana, text="Limpiar", command=limpiar_datos).grid(row=9, column=1)

lbl_saludo = tk.Label(ventana, text="")
lbl_saludo.grid(row=1, column=2)

lbl_edad = tk.Label(ventana, text="")
lbl_edad.grid(row=2, column=2)

tk.Label(ventana, text="Tu signo zodiacal").grid(row=3, column=2)

lbl_signo_nombre = tk.Label(ventana, text="")
lbl_signo_nombre.grid(row=4, column=2)

lbl_imagen = tk.Label(ventana)
lbl_imagen.grid(row=5, column=2)

ventana.mainloop()