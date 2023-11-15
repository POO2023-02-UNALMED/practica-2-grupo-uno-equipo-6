import tkinter as tk
from tkinter import font


class BaseFuncionalidad(tk.Frame):
    def __init__(self, master: tk.Misc, titulo: str, descripcion: str, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        frame_titulo = tk.Frame(self)
        frame_titulo.pack(pady=(20, 10))
        self.label_titulo = tk.Label(frame_titulo, text=titulo, font=font.Font(size=16))
        self.label_titulo.pack()

        frame_descripcion = tk.Frame(self)
        frame_descripcion.pack(pady=(10, 20))
        self.label_descripcion = tk.Label(frame_descripcion, text=descripcion, font=font.Font(weight="bold"))
        self.label_descripcion.pack()

        self.frame_contenido = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.frame_contenido.pack(padx=20, pady=(10, 20))

    def packContenido(self, contenido: tk.Frame):
        contenido.pack(padx=20, pady=15)
