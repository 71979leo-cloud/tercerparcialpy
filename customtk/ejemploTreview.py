import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# Configuración de CustomTkinter
ctk.set_appearance_mode("dark") # "dark" o "light"
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CustomTkinter + Treeview")
        self.geometry("700x400")

        # Frame principal
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill="both", expand=False, padx=10, pady=10)

        # ====== TREEVIEW ======
        self.tabla = ttk.Treeview(self.frame)

        # Scrollbar
        scroll_y = ttk.Scrollbar(self.frame, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll_y.set)

        # Posición
        self.tabla.pack(side="left", fill="both", expand=False)
        scroll_y.pack(side="right", fill="y")

        # Columnas
        self.tabla["columns"] = ("ID", "Nombre", "Edad")

        self.tabla.column("#0", width=0, stretch=tk.NO)
        self.tabla.column("ID", anchor=tk.CENTER, width=80)
        self.tabla.column("Nombre", anchor=tk.W, width=200)
        self.tabla.column("Edad", anchor=tk.CENTER, width=80)

        # Encabezados
        self.tabla.heading("#0", text="")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Edad", text="Edad")