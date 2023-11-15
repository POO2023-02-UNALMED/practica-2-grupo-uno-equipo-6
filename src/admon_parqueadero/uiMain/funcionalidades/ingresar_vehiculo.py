import tkinter as tk
from typing import Any
from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame

from admon_parqueadero.uiMain.funcionalidades.base_funcionalidad import BaseFuncionalidad


class IngresarVehiculo(BaseFuncionalidad):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

        self.setTitulo("Ingresar Vehiculo")
        self.setDescripcion("descripcion ams asfñasjf asfas fñajs")

        contenido = tk.Frame(self.frame_contenido)
        self.packContenido(contenido)

        field_frame = FieldFrame(contenido, "Hola", ["Codigo", "Nombre", "Descripcion", "Ubicacion"], "Adios", None, None)
        field_frame.pack(anchor="s", fill="both", expand=True, ipadx=15, ipady=5)

        frame_botones = tk.Frame(contenido)
        frame_botones.pack(side="bottom", fill="both", expand=True)

        btn1 = tk.Button(frame_botones, text="Aceptar")
        btn1.pack(side="left" , fill="both", expand=True, padx=15)
        btn2 = tk.Button(frame_botones, text="Borrar")
        btn2.pack(side="right", fill="both", expand=True, padx=15)
