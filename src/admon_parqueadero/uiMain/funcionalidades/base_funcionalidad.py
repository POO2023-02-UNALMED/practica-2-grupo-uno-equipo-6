import tkinter as tk
from tkinter import font
from typing import Any


class BaseFuncionalidad(tk.Frame):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        frame_titulo = tk.Frame(self)
        frame_titulo.pack(pady=(20, 10))
        self.label_titulo = tk.Label(frame_titulo, font=font.Font(size=16))
        self.label_titulo.pack()

        frame_descripcion = tk.Frame(self)
        frame_descripcion.pack(pady=(10, 20))
        self.label_descripcion = tk.Label(frame_descripcion, font=font.Font(weight="bold"))
        self.label_descripcion.pack()

        self.frame_contenido = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.frame_contenido.pack(padx=20, pady=(10, 20))

    def setTitulo(self, titulo: str) -> None:
        self.label_titulo.config(text=titulo)

    def setDescripcion(self, descripcion: str) -> None:
        self.label_descripcion.config(text=descripcion)

    def packContenido(self, contenido: tk.Frame) -> None:
        contenido.pack(padx=20, pady=15)
