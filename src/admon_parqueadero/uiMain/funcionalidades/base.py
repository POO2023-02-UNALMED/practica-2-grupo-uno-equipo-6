import tkinter as tk
from tkinter import font
from typing import Any, cast

from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.gestorAplicacion.parqueadero.parqueadero import Parqueadero
from admon_parqueadero.uiMain.componentes.label_ajustable import LabelAjustable


class BaseFuncionalidad(tk.Frame):
    def __init__(
        self, master: tk.Misc, baseDatos: BaseDatos, *args: Any, **kwargs: Any
    ) -> None:
        super().__init__(master, *args, **kwargs)

        self._baseDatos = baseDatos
        self._parqueadero = cast(Parqueadero, baseDatos.getParqueadero())

        frame_titulo = tk.Frame(
            self, highlightbackground="cornflowerblue", highlightthickness=2
        )
        frame_titulo.pack(pady=10)
        self.label_titulo = tk.Label(
            frame_titulo, font=font.Font(weight="bold", size=16)
        )
        self.label_titulo.pack(fill="both", expand=True)

        frame_descripcion = tk.Frame(
            self, highlightbackground="cornflowerblue", highlightthickness=2
        )
        frame_descripcion.pack(pady=10)
        self.label_descripcion = LabelAjustable(
            frame_descripcion, font=font.Font(weight="bold", size=12)
        )
        self.label_descripcion.pack(fill="both", expand=True, padx=20)

        self.frame_contenido = tk.Frame(
            self, highlightbackground="black", highlightthickness=2
        )
        self.frame_contenido.pack(padx=20, pady=(10, 20))

        self.listbox = tk.Listbox(self)
        self.listbox.pack(side="bottom", expand=True, fill="both")

    def setTitulo(self, titulo: str) -> None:
        self.label_titulo.config(text=titulo)

    def setDescripcion(self, descripcion: str) -> None:
        self.label_descripcion.config(text=descripcion)

    def packContenido(self, contenido: tk.Frame) -> None:
        contenido.pack(padx=20, pady=20)

    def getBaseDatos(self) -> BaseDatos:
        return self._baseDatos

    def getParqueadero(self) -> Parqueadero:
        return self._parqueadero

    def imprimir(self, s: str) -> None:
        self.listbox.insert(tk.END, s)
