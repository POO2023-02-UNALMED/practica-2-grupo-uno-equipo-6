import tkinter as tk
from admon_parqueadero.baseDatos.baseDatos import BaseDatos

from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame

class FormularioCliente(tk.Frame):
    def __init__(self, master, baseDatos: BaseDatos, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self._baseDatos = baseDatos

        self.field_frame_container = tk.Frame(self)
        self.field_frame_container.pack()
        self.field_frame = FieldFrame(self.field_frame_container, "Criterio", ["Cédula"], "Valor", None, None)
        self.field_frame.pack()

        botones = tk.Frame(self)
        botones.pack()
        
        btn_entrar = tk.Button(botones, text="Entrar", command=self.manejar_entrar)
        btn_entrar.grid(row=0, column=0)
        
        btn_borrar = tk.Button(botones, text="Borrar")
        btn_borrar.grid(row=0, column=1)

    def manejar_entrar(self):
        cedula = int(self.field_frame.getValue("Cédula"))  # TODO: manejar errores si eso no es un numero
        cliente = self._baseDatos.buscarClienteRegistrado(cedula)
        if cliente is None:
            self.field_frame.destroy()
            tk.Label(self.field_frame_container, text="Registro de usuario").pack()
            self.field_frame = FieldFrame(
                self.field_frame_container, "Criterio", ["Cédula", "Nombre", "Telefono", "Correo", "Direccion", ""], "Valor", [str(cedula)], ["Cédula"]
            )
