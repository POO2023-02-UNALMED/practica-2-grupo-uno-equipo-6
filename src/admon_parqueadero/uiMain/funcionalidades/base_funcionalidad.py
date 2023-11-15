import tkinter as tk
from tkinter import font
from typing import Any, Optional

from admon_parqueadero.baseDatos.baseDatos import BaseDatos


class BaseFuncionalidad(tk.Frame):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self._baseDatos: Optional[BaseDatos] = None

        frame_titulo = tk.Frame(self, highlightbackground="cornflowerblue", highlightthickness=2)
        frame_titulo.pack(pady=10)
        self.label_titulo = tk.Label(frame_titulo, font=font.Font(weight='bold', size=16))
        self.label_titulo.pack(fill='both', expand=True)

        frame_descripcion = tk.Frame(self, highlightbackground="cornflowerblue", highlightthickness=2)
        frame_descripcion.pack(pady=10)
        self.label_descripcion = tk.Label(frame_descripcion, font=font.Font(weight='bold', size=12))
        self.label_descripcion.pack(fill='both', expand=True)

        self.frame_contenido = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.frame_contenido.pack(padx=20, pady=(10, 20))

    def setTitulo(self, titulo: str) -> None:
        self.label_titulo.config(text=titulo)

    def setDescripcion(self, descripcion: str) -> None:
        self.label_descripcion.config(text=descripcion)

    def packContenido(self, contenido: tk.Frame) -> None:
        contenido.pack(padx=20, pady=20)
    
    def setBaseDatos(self, baseDatos: BaseDatos) -> None:
        self._baseDatos = baseDatos
