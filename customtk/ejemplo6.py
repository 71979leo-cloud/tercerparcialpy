import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class Tabla(ctk.CTkFrame):
    def _init_(self,master, columnas, datos):
        super()._init_(master)

        self.columnas=columnas
        self.datos=datos

        #crear encabezados
        for col, texto in enumerate(self.columnas):
            header = ctk.CTkLabel(self, text=texto, font=("Arial", 14, "bold"))
            header.grid(row=0, column=col, padx=5, pady=5)

        #crear filas
        for fila, registro in enumerate(self.datos, start=1):
            for col, valor in enumerate(registro):
                cell= ctk.CTkLabel(self,text=str(valor))
                cell.grid(row=fila,column=col,padx=5,pady=5)
# App principal
class App(ctk.CTk):
    def _init_(self):
        super()._init_()

        self.title("Tabla con CustomTkinter")
        self.geometry("500x300")

        columnas = ["ID", "Nombre", "Edad"]
        datos = [
            [1, "Ana", 23],
            [2, "Luis", 30],
            [3, "Carlos", 28],
        ]

        tabla = Tabla(self, columnas, datos)
        tabla.pack(pady=20, padx=20)             
if _name_ == "_main_":
    app=App()
    app.mainloop()