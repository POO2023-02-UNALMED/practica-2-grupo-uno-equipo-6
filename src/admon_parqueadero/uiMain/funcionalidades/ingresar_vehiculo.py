import tkinter as tk
from typing import Any
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame
from admon_parqueadero.uiMain.componentes.formulario_cliente import FormularioCliente

from admon_parqueadero.uiMain.funcionalidades.base_funcionalidad import (
    BaseFuncionalidad,
)


class IngresarVehiculo(BaseFuncionalidad):
    def __init__(
        self, master: tk.Misc, baseDatos: BaseDatos, *args: Any, **kwargs: Any
    ):
        super().__init__(master, baseDatos, *args, **kwargs)

        self.setTitulo("Ingresar Vehiculo")
        self.setDescripcion("descripcion ams asfñasjf asfas fñajs")

        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)

        formulario = FormularioCliente(
            self.contenido, self.getBaseDatos(), f_final=self._configurar_ui
        )
        formulario.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)

        # field_frame = FieldFrame(contenido, "Hola", ["Codigo", "Nombre", "Descripcion", "Ubicacion"], "Adios", None, None, {"Nombre": ["A", "B"]})
        # field_frame.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)

    def _configurar_ui(self, cliente: Cliente) -> None:
        field_frame = FieldFrame(
            self.contenido,
            "Criterio",
            ["Cédula"],
            "Valor",
            [str(cliente.getCedula())],
            ["Cédula"],
        )
        field_frame.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)

        frame_botones = tk.Frame(self.contenido)
        frame_botones.pack(side="bottom", fill="both", expand=True)

        btn1 = tk.Button(frame_botones, text="Aceptar")
        btn1.pack(side="left", fill="both", expand=True, padx=15)
        btn2 = tk.Button(frame_botones, text="Borrar")
        btn2.pack(side="right", fill="both", expand=True, padx=15)
