"""def Escribir_archivos():
    nombre=input("Nombre del archivo: ")
    texto=input("Escribe el texto a guardar: ")
    
    with open(nombre, "w") as arvhivo:
        archivo.write(texto)
        
    print("Texto guardado correctamente")
    
Escribir_archivos()

def agregar_texto():
    nombre=input("Nombre del archivo: ")
    texto=input("Texto a agregar: ")
    
    with open(nombre, "a") as archivo:
        archivo.write("\n" + texto)
        
agregar_texto()

def leer_archivos():
    nombre=input("Nombre del archivo")
    
    try:
        with open(nombre, "r") as archivo:
            contenido=archivo.read()
            print("\nContenido del archivo: ")
            print(contenido)
            print("------------------------------")
            archivo.seek(0)
            contenido=archivo.read()
            print("contenido")
    except FileNotFoundError:
        print("El archivo no existe")
        
leer_archivos()"""
             
'''def leer_archivos():
    """nombre=input("Nombre del archivo")"""
    nombre = "Ico201-9.txt"
    
    try:
        with open(nombre, "r") as archivo:
            contenido=archivo.readline()
            print("\nContenido del archivo: ")
            print(contenido)
            contenido=archivo.readline()
            print(contenido)
            
            for linea in contenido:
                print(linea.strip())
    except FileNotFoundError:
        print("El archivo no existe")
        
leer_archivos()'''

def buscar_palabra():
    nombre = input("Nombre del archivo: ")
    palabra = input("Palabra a buscar: ")

    try:
        with open(nombre, "r")as archivo:
            contenido=archivo.read()

            if palabra in contenido:
                print("La palabra fue encontrada: ")
            else:
                print("La palabra no se encuentra en el archivo: ")

    except FileNotFoundError:
        print("El archivo no existe")
buscar_palabra()