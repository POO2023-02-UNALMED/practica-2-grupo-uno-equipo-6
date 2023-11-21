#Funcionalidad del módulo: contiene la clase RegistrarCliente que hereda de BaseFuncionalidad, 
#esta sirve para registrar los datos de un nuevo cliente, 
#la encontramos en Otras Funcionalidades.
#Componentes del módulo: RegistrarCliente
#Autores: Sofia, Sara, Alejandro, Sebastián, Katherine


import tkinter as tk
from tkinter import messagebox
from typing import Any
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.gestorAplicacion.personas.cliente import Cliente
from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame
from admon_parqueadero.uiMain.funcionalidades.base import BaseFuncionalidad


class RegistrarCliente(BaseFuncionalidad):
    def __init__(
        self, master: tk.Misc, baseDatos: BaseDatos, *args: Any, **kwargs: Any
    ):
        super().__init__(master, baseDatos, *args, **kwargs)

        self.setTitulo("Registrar Cliente")
        self.setDescripcion("Bienvenido, aqui podra registrar un cliente, para empezar ingrese el número de cédula del cliente a resgistrar")

        #aca solo deberia acceder el administrador?
        self.contenido = tk.Frame(self.frame_contenido)
        self.packContenido(self.contenido)

        self._frame_inicial()

    def _frame_inicial(self) -> None:
        self.field_frame = FieldFrame(self.contenido, "Criterio", ["Cédula"], "Valor", None, None)
        self.field_frame.pack()
        self.botones = tk.Frame(self.contenido)
        self.botones.pack()

        self.btn_principal = tk.Button(self.botones, text="Continuar", command=self._continuar)
        self.btn_principal.grid(row=0, column=0)

        self.btn_borrar = tk.Button(
            self.botones, text="Borrar", command=lambda: self.field_frame.borrar()
        )
        self.btn_borrar.grid(row=0, column=1)

    def _continuar(self) -> None:
        cedula = self.field_frame.getValueNumero("Cédula", int)
        cliente = self._baseDatos.buscarClienteRegistrado(cedula)
        if cliente is None:
            self.field_frame.destroy()
            self.field_frame = FieldFrame(
                self.contenido,
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

            self.botones.destroy()
            self.botones = tk.Frame(self.contenido)
            self.botones.pack()

            self.btn_principal = tk.Button(self.botones, text="Registrar", command=self._registrar_usuario)
            self.btn_principal.grid(row=0, column=0)

            self.btn_borrar = tk.Button(
                self.botones, text="Borrar", command=lambda: self.field_frame.borrar()
            )
            self.btn_borrar.grid(row=0, column=1)
        else:
            messagebox.showwarning("No se puede", "El cliente ya se encuentra registrado")

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

        messagebox.showinfo("Registro exitoso", f"El cliente de nombre {nombre.title()} ha sido registrado exitosamente")
        self.field_frame.destroy()
        self.botones.destroy()
        return self._frame_inicial()
