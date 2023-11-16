import tkinter as tk
from typing import Any
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.uiMain.funcionalidades.base import BaseFuncionalidad
from admon_parqueadero.uiMain.componentes.formulario_cliente import FormularioCliente
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame

class VenderCarro(BaseFuncionalidad):
    def __init__(
        self, master: tk.Misc, baseDatos: BaseDatos, *args: Any, **kwargs: Any
    ):
        super().__init__(master, baseDatos, *args, **kwargs)

        self.setTitulo("Vender Carro")
        self.setDescripcion("Bienvenido, aquí podrá vender un carro, o intercambiarlo por uno de los que\
                    se encuentran disponibles en el parqueadero. Para comenzar, ingrese su cédula,\
                    en caso de no estar registrado se solicita rellenar sus datos y generar el ingreso \
                    al parqueadero del vehículo que desea vender.")
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)

        formulario = FormularioCliente(
            self.contenido, self.getBaseDatos(), f_final=self._configurar_ui
        )
        formulario.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)
    def _configurar_ui(self, cliente: Cliente) -> None:
        placas_vehiculos = map(lambda v: v.getPlaca(), cliente.getVehiculos())

        self.field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Cédula", "Vehículo que desea vender"],
            "Valor",
            [str(cliente.getCedula()), None],
            ["Cédula"],
            combobox={
                "Vehículo que desea vender": [*placas_vehiculos, "Registrar un vehículo"]
            },
        )
        self.field_frame.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)
        #self._generar_botones("Continuar")#, lambda: self._continuar_inicio(cliente))
