import tkinter as tk
from tkinter import messagebox
from typing import Any, Type
from admon_parqueadero.baseDatos.baseDatos import BaseDatos
from admon_parqueadero.gestorAplicacion.parqueadero.almacen import Almacen
from admon_parqueadero.gestorAplicacion.parqueadero.parqueadero import Parqueadero

from admon_parqueadero.uiMain.componentes.label_ajustable import LabelAjustable
from admon_parqueadero.uiMain.funcionalidades.base import BaseFuncionalidad
from admon_parqueadero.uiMain.funcionalidades.taller import Taller
from admon_parqueadero.uiMain.funcionalidades.vender_carro import VenderCarro
from admon_parqueadero.uiMain.funcionalidades.comprar_carro import ComprarCarro
from admon_parqueadero.uiMain.funcionalidades.manejo_parqueadero import (
    ManejoParqueadero,
)
from admon_parqueadero.uiMain.funcionalidades.generar_datos import GenerarDatos
from admon_parqueadero.uiMain.funcionalidades.ingresar_vehiculo import IngresarVehiculo
from admon_parqueadero.uiMain.funcionalidades.registrar_cliente import RegistrarCliente
from admon_parqueadero.uiMain.funcionalidades.registrar_vehiculo import (
    RegistrarVehiculo,
)


class ventana_principal_usu(tk.Frame):
    def __init__(self, master: tk.Tk, *args: Any, **kwargs: Any) -> None:
        super().__init__(master, *args, **kwargs)
        self.master: tk.Tk = master
        master.wm_title("Parqueadero")
        self.pack()
        self.configurar_menu()
        self.interfaz_inicio()
        baseDatos = BaseDatos.leerDatos()  # TODO: manejar errores de esto
        if baseDatos is None:
            # crear base de datos inicial
            baseDatos = BaseDatos()
            parqueadero = Parqueadero(
                plazasTotales=200,
                tarifaCarro=4000,
                tarifaMoto=1000,
                almacen=Almacen(200),
            )
            baseDatos.setParqueadero(parqueadero)
        self._baseDatos = baseDatos

        def cerrar() -> None:
            self.master.destroy()
            self._baseDatos.escribirDatos()

        self.master.protocol("WM_DELETE_WINDOW", cerrar)

    def configurar_menu(self) -> None:
        menu_bar = tk.Menu(self.master)
        menu_archivo = tk.Menu(menu_bar, tearoff=False)
        menu_procesos_consultas = tk.Menu(menu_bar, tearoff=False)
        menu_ayuda = tk.Menu(menu_bar, tearoff=False)
        menu_funcionalidades_extra = tk.Menu(menu_procesos_consultas, tearoff=False)

        menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
        menu_bar.add_cascade(label="Procesos y consultas", menu=menu_procesos_consultas)
        menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)

        menu_archivo.add_command(label="Aplicacion", command=self.aplicacion)
        menu_archivo.add_command(label="Salir", command=self.salir)
        menu_procesos_consultas.add_command(
            label="Ingresar Vehiculo",
            command=lambda: self.cambiar_funcionalidad(IngresarVehiculo),
        )
        menu_procesos_consultas.add_command(
            label="Taller", command=lambda: self.cambiar_funcionalidad(Taller)
        )
        menu_procesos_consultas.add_command(
            label="Vender Carro",
            command=lambda: self.cambiar_funcionalidad(VenderCarro),
        )
        menu_procesos_consultas.add_command(
            label="Comprar Carro",
            command=lambda: self.cambiar_funcionalidad(ComprarCarro),
        )
        menu_procesos_consultas.add_command(
            label="Manejo Parqueadero",
            command=lambda: self.cambiar_funcionalidad(ManejoParqueadero),
        )
        menu_procesos_consultas.add_cascade(
            label="Funcionalidades extras", menu=menu_funcionalidades_extra
        )
        menu_funcionalidades_extra.add_command(
            label="Registrar Cliente",
            command=lambda: self.cambiar_funcionalidad(RegistrarCliente),
        )
        menu_funcionalidades_extra.add_command(
            label="Registrar Vehículo",
            command=lambda: self.cambiar_funcionalidad(RegistrarVehiculo),
        )
        menu_funcionalidades_extra.add_command(
            label="Generar Datos de Prueba",
            command=lambda: self.cambiar_funcionalidad(GenerarDatos),
        )
        menu_ayuda.add_command(label="Acerca de", command=self.acerca_de)

        self.master.config(menu=menu_bar)

    def aplicacion(self) -> None:
        messagebox.showinfo(
            title="Información sobre la aplicación.",
            message="Esta aplicación permite al usuario acceder a diferentes servicios prestados por el parqueadero, y facilita el manejo de asuntos relacionados a la gerencia, por parte del administrador. Se puede acceder a estos mediante la pestaña de usuario, en el menú Procesos y Consultas.",
        )  # TODO: poner mensaje

    def salir(self) -> None:
        from .ventana_inicio import VentanaInicio

        self.destroy()
        self.master.config(menu=tk.Menu())
        VentanaInicio(self.master).pack(side="top", fill="both", expand=True)

        self._baseDatos.escribirDatos()

    def acerca_de(self) -> None:
        messagebox.showinfo(
            title="Información sobre los autores.",
            message="Los autores de esta maravillosa aplicacion son:\n- Alejandro (Power ranger rojo)\n- Sofía (Power ranger rosada)\n- Katherine (Power ranger amarilla)\n- Sara (Power ranger blanca)\n- Sebastián (Power ranger azul)",
        )

    def interfaz_inicio(self) -> None:
        self.frame_funcionalidad = tk.Frame(
            self, highlightbackground="black", highlightthickness=2
        )
        self.frame_funcionalidad.pack(
            side="top", fill="both", expand=True, padx=10, pady=10
        )

        texto_bienvenida = tk.Label(
            self.frame_funcionalidad, text="Bienvenido", font=("Arial", 20)
        )
        texto_bienvenida.pack(side="top", padx=5, pady=5)

        texto = "Para empezar a usar la aplicación seleccione una de las opciones listadas en procesos y consultas, recomendamos empezar\
 ingresando un vehiculo que no se encuentre en el parqueadero. Esta aplicación le permitira administrar y realizar servicios\
 varios asociados a un parqueadero con mayor comodidad puesto que solo debera precuparse por introducir los valores correctamente\
 ya que el programa se encargara del resto ;)"

        texto_descripcion = LabelAjustable(
            self.frame_funcionalidad, text=texto, font=("Arial", 12)
        )
        texto_descripcion.pack(padx=5, pady=10, fill="x")

    def cambiar_funcionalidad(
        self, clase_funcionalidad: Type[BaseFuncionalidad]
    ) -> None:
        self.frame_funcionalidad.destroy()
        funcionalidad = clase_funcionalidad(
            self,
            baseDatos=self._baseDatos,
            highlightbackground="black",
            highlightthickness=2,
        )
        self.frame_funcionalidad = funcionalidad
        self.frame_funcionalidad.pack(
            side="top", fill="both", expand=True, padx=10, pady=10
        )
