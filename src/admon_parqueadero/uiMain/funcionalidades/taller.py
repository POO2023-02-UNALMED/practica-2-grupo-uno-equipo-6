import tkinter as tk
from typing import Any
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.uiMain.funcionalidades.base import BaseFuncionalidad


class Taller(BaseFuncionalidad):
    def __init__(
        self, master: tk.Misc, baseDatos: BaseDatos, *args: Any, **kwargs: Any
    ):
        super().__init__(master, baseDatos, *args, **kwargs)

        self.setTitulo("Taller")

        self.setDescripcion("Bienvenido al taller, será atendido por el mecánico de su preferencia. \
                    Para hacer uso de los servicios del taller, su vehículo debe encontrarse en el \
                    parqueadero. Para comenzar, ingrese sus datos y los de su vehículo.")