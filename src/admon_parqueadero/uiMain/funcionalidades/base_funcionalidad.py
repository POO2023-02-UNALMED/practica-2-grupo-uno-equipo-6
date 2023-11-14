import tkinter as tk
from tkinter import font


class BaseFuncionalidad(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        frame_titulo = tk.Frame(self)
        frame_titulo.pack()
        self.label_titulo = tk.Label(frame_titulo, font=font.Font(weight='bold', size=20))
        self.label_titulo.pack()

        frame_descripcion = tk.Frame(self)
        frame_descripcion.pack()
        self.label_descripcion = tk.Label(frame_descripcion)
        self.label_descripcion.pack()

        self.contenido = tk.Frame(self)
        self.contenido.pack()
    
    def setTitulo(self, titulo: str):
        self.label_titulo.config(text=titulo)
    
    def setDescripcion(self, descripcion: str):
        self.label_descripcion.config(text=descripcion)
    
    def setContenido(self, contenido: tk.Frame):
        self.contenido.destroy()
        self.contenido = contenido
        self.contenido.pack()