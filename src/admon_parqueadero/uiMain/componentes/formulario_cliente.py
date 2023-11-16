import tkinter as tk
from typing import Any, Callable
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente

from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame


class FormularioCliente(tk.Frame):
    def __init__(
            self, master: tk.Misc, baseDatos: BaseDatos, f_final: Callable[[Cliente], None], *args: Any, **kwargs: Any
    ) -> None:
        super().__init__(master, *args, **kwargs)

        self._baseDatos = baseDatos
        self._f_final = f_final

        self.field_frame = FieldFrame(self, "Criterio", ["Cédula"], "Valor", None, None)
        self.field_frame.pack()

        self.botones = tk.Frame(self)
        self.botones.pack()

        btn_entrar = tk.Button(self.botones, text="Entrar", command=self.manejar_entrar)
        btn_entrar.grid(row=0, column=0)

        btn_borrar = tk.Button(
            self.botones, text="Borrar", command=self.field_frame.borrar
        )
        btn_borrar.grid(row=0, column=1)

    def manejar_entrar(self) -> None:
        cedula = int(
            self.field_frame.getValue("Cédula")
        )  # TODO: manejar errores si eso no es un numero
        cliente = self._baseDatos.buscarClienteRegistrado(cedula)
        self.field_frame.destroy()
        self.botones.destroy()
        if cliente is None:
            tk.Label(self, text="Registro de usuario").pack()
            self.field_frame = FieldFrame(
                self,
                "Criterio",
                ["Cédula", "Nombre", "Teléfono", "Correo", "Dirección", "En condición de discapacidad"],
                "Valor",
                [str(cedula), None, None, None, None, None],
                ["Cédula"],
                combobox={"En condición de discapacidad": ["Sí", "No"]}
            )
            self.field_frame.pack()

            self.botones = tk.Frame(self)
            self.botones.pack()

            btn_registrar = tk.Button(
                self.botones, text="Registrarse", command=self._registrar_usuario
            )
            btn_registrar.grid(row=0, column=0)

            btn_borrar = tk.Button(
                self.botones, text="Borrar", command=self.field_frame.borrar
            )
            btn_borrar.grid(row=0, column=1)
        else:
            self.destroy()
            self._f_final(cliente)

    def _registrar_usuario(self) -> None:
        # TODO: verificar que los numeros sí sean números
        # TODO: verificar que todos las entradas sí tienen valores (que no esten vacías)
        cedula = int(self.field_frame.getValue("Cédula"))
        nombre = self.field_frame.getValue("Nombre")
        telefono = int(self.field_frame.getValue("Teléfono"))
        correo = self.field_frame.getValue("Correo")
        direccion = self.field_frame.getValue("Dirección")
        discapacitado_str = self.field_frame.getValue("En condición de discapacidad")

        if discapacitado_str == "Sí":
            discapacitado = True
        else:
            discapacitado = False

        cliente = Cliente(nombre, cedula, telefono, correo, direccion, discapacitado)
        self._baseDatos.registrarCliente(cliente)

        self.destroy()
        self._f_final(cliente)
