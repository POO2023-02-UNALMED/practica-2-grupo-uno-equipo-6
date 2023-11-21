#Funcionalidad del módulo: contiene la clase BaseFuncionalidad que hereda de tk.Frame, 
#esta sirve para generar una base con los métodos e información que se utilizan
#en varias o todas las funcionalidades.
#Componentes del módulo: BaseFuncionalidad
#Autores: Sofia, Sara, Alejandro, Sebastián, Katherine


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

    def imprimir(self, *args: str) -> None:
        s = " ".join(args)
        s = s.replace("\t", "    ")
        for linea in s.splitlines():
            self.listbox.insert(tk.END, linea)
