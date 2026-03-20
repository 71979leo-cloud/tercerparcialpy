
'''
manejo de archivos de texto
apertura de archivos
   open("archivo1.txt", "r")


Modo    Descripccion
r       leer
w       escribir(sobrescribe)
a       agregar
x       crear archivo


***** Lectura de archivos
    * archivo.read()
    * archivo.readline()
    * archivo.readlines()

***** Escritura de archivos
    * archivos.write("Texto a escribir")
    * archivo.writelines(["Linea 1/n")
    
'''


def crear_archivo():
    nombre = input("Nombre del archivo (con .txt): ")
    with open(nombre, "w") as archivo:
        print(f"Archivo '{nombre}' creado correctamente.")

def escribir_archivo():
    nombre = input("Nombre del archivo: ")
    texto = input("Escribir el texto a guardar: ")
    with open(nombre, "w") as archivo:
        archivo.write(texto) 
    print("Texto guardado correctamente.")

def agregar_texto():
    nombre = input("Nombre del archivo: ")
    texto = input("Texto a agregar: ")
    with open(nombre, "a") as archivo:
        archivo.write("\n" + texto)
    print("Texto agregado.")

def leer_archivos():
    nombre = input("Nombre del archivo a leer: ")
    try:
        with open(nombre, "r") as archivo:
            print("\n--- Contenido del archivo ---")
            print(archivo.read())
    except FileNotFoundError:
        print("Error: El archivo no existe.")

def buscar_palabra():
    nombre = input("Nombre del archivo: ")
    palabra = input("Palabra a buscar: ")
    try:
        with open(nombre, "r") as archivo:
            contenido = archivo.read()
            if palabra in contenido:
                print(f"¡Encontrada! La palabra '{palabra}' está en el archivo.")
            else:
                print(f"La palabra '{palabra}' no se encuentra.")
    except FileNotFoundError:
        print("Error: El archivo no existe.")

def menu():
    while True:
        print("\n--- GESTOR DE ARCHIVOS ---")
        print("1. Crear archivo")
        print("2. Escribir en archivo")
        print("3. Agregar texto")
        print("4. Leer archivo")
        print("5. Buscar palabra")
        print("6. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            escribir_archivo() 
        elif opcion == "3":
            agregar_texto()
        elif opcion == "4":
            leer_archivos()
        elif opcion == "5":
            buscar_palabra() 
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, intenta de nuevo.")

menu()