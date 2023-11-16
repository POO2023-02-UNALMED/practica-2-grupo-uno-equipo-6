import tkinter as tk
from typing import Any
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.uiMain.funcionalidades.base import BaseFuncionalidad


class ComprarCarro(BaseFuncionalidad):
    def __init__(
        self, master: tk.Misc, baseDatos: BaseDatos, *args: Any, **kwargs: Any
    ):
        super().__init__(master, baseDatos, *args, **kwargs)

        self.setTitulo("Comprar Carro")
        self.setDescripcion("Bienvenido, aquí podrá comprar un carro según sus preferencias.\
                    Para comenzar, ingrese su documento, en caso de no estar registrado, \
                    ingrese sus datos.")