import tkinter as tk
from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame

from admon_parqueadero.uiMain.funcionalidades.base_funcionalidad import BaseFuncionalidad


class IngresarVehiculo(BaseFuncionalidad):
    def __init__(self, master: tk.Frame):
        super().__init__(master)

        self.setTitulo("Ingresar Vehiculo")
        self.setDescripcion("descripcion")

        contenido = tk.Frame(self.frame_contenido)
        self.packContenido(contenido)

        field_frame = FieldFrame(contenido, "Hola", [], "Adios", None, None)
        field_frame.pack()

        frame_botones = tk.Frame(contenido)
        frame_botones.pack()

        btn1 = tk.Button(frame_botones, text="Hola")
        btn1.pack()
