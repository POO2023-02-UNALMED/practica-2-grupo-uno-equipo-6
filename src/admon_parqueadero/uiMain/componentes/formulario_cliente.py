#Funcionalidad del módulo: contiene la clase FormularioCliente que hereda de tk.Frame, 
#esta sirve para solicitar los datos del cliente antes de iniciar cualquier funcionalidad, 
#y verificar que se encuentra registrado o realizar el registro.
#Componentes del módulo: FormularioCliente
#Autores: Sofia, Sara, Alejandro, Sebastián, Katherine


import tkinter as tk
from tkinter import messagebox
from typing import Any, Callable
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.errores import ErrorObjetoInexistente

from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame


class FormularioCliente(tk.Frame):
    def __init__(
        self,
        master: tk.Misc,
        baseDatos: BaseDatos,
        f_final: Callable[[Cliente], None],
        imprimir: Callable[..., None],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(master, *args, **kwargs)

        self._baseDatos = baseDatos
        self._f_final = f_final
        self._imprimir = imprimir

        self.field_frame_container = tk.Frame(self)
        self.field_frame_container.pack()

        self.field_frame = FieldFrame(self.field_frame_container, "Criterio", ["Cédula"], "Valor", None, None, titulo="Ingrese su número de cédula")
        self.field_frame.pack()

        self.botones = tk.Frame(self)
        self.botones.pack()

        self.btn_principal = tk.Button(self.botones, text="Entrar", command=self.manejar_entrar)
        self.btn_principal.grid(row=0, column=0)

        self.btn_borrar = tk.Button(
            self.botones, text="Borrar", command=lambda: self.field_frame.borrar()
        )
        self.btn_borrar.grid(row=0, column=1)

    def manejar_entrar(self) -> None:
        cedula = self.field_frame.getValueNumero("Cédula", int)
        cliente = self._baseDatos.buscarClienteRegistrado(cedula)
        if cliente is None:
            try:
                raise ErrorObjetoInexistente(f"cliente con cedula {cedula}")
            finally:
                self.field_frame.destroy()
                self.field_frame = FieldFrame(
                    self.field_frame_container,
                    "Criterio",
                    [
                        "Cédula",
                        "Nombre",
                        "Teléfono",
                        "Correo",
                        "Dirección",
                        "En condición de discapacidad",
                    ],
                    "Valor",
                    [str(cedula), None, None, None, None, None],
                    ["Cédula"],
                    combobox={"En condición de discapacidad": ["Sí", "No"]},
                    titulo="Registro de usuario"
                )
                self.field_frame.pack()

                self.btn_principal.config(text="Registrarse")
                self.btn_principal.config(command=self._registrar_usuario)
                self.btn_borrar.config(command=self.field_frame.borrar)
        else:
            self.destroy()
            self._f_final(cliente)

    def _registrar_usuario(self) -> None:
        cedula = self.field_frame.getValueNumero("Cédula", int)
        nombre = self.field_frame.getValue("Nombre")
        telefono = self.field_frame.getValueNumero("Teléfono", int)
        correo = self.field_frame.getValue("Correo")
        direccion = self.field_frame.getValue("Dirección")
        discapacitado_str = self.field_frame.getValue("En condición de discapacidad")

        if discapacitado_str == "Sí":
            discapacitado = True
        else:
            discapacitado = False

        cliente = Cliente(nombre, cedula, telefono, correo, direccion, discapacitado)
        self._baseDatos.registrarCliente(cliente)

        self._imprimir("Cliente registrado exitosamente")

        self.destroy()
        self._f_final(cliente)
