import tkinter as tk
from tkinter import messagebox
from typing import Any

from admon_parqueadero.uiMain.componentes.label_ajustable import LabelAjustable


class ventana_principal_usu(tk.Frame):
    def __init__(self, master: tk.Tk, *args: Any, **kwargs: Any) -> None:
        super().__init__(master, *args, **kwargs)
        self.master: tk.Tk = master
        master.wm_title("Parqueadero")
        self.pack()
        self.configurar_menu()
        self.interfaz_inicio()

    def configurar_menu(self) -> None:
        menu_bar = tk.Menu(self.master)
        menu_archivo = tk.Menu(menu_bar, tearoff=False)
        menu_procesos_consultas = tk.Menu(menu_bar, tearoff=False)
        menu_ayuda = tk.Menu(menu_bar, tearoff=False)

        menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
        menu_bar.add_cascade(label="Procesos y consultas", menu=menu_procesos_consultas)
        menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)

        menu_archivo.add_command(label="Aplicacion", command=self.aplicacion)
        menu_archivo.add_command(label="Salir", command=self.salir)
        menu_procesos_consultas.add_command(label="Ingresar Vehiculo")
        menu_procesos_consultas.add_command(label="Taller")
        menu_procesos_consultas.add_command(label="Vender Carro")
        menu_procesos_consultas.add_command(label="Comprar Carro")
        menu_procesos_consultas.add_command(label="Manejo Parqueadero")
        menu_procesos_consultas.add_command(label="Funcionalidades extras")
        menu_ayuda.add_command(label="Acerca de", command=self.acerca_de)

        self.master.config(menu=menu_bar)

    def aplicacion(self) -> None:
        messagebox.showinfo(
            title="Hola!!",
            message="Esta aplicación permite administrar un parqueadero ...",
        )  # TODO: poner mensaje

    def salir(self) -> None:
        from .ventana_inicio import VentanaInicio

        self.destroy()
        self.master.config(menu=tk.Menu())
        VentanaInicio(self.master).pack(side="top", fill="both", expand=True)

    def acerca_de(self) -> None:
        messagebox.showinfo(
            title="Hola!!",
            message="Los autores de esta maravillosa aplicacion somos:\n-Alejandro(power ranger azul)\n-Sofia(power ranger rosada)\n-Katherine(power ranger amarilla)\n-Sara(power ranger blanca)\n-Sebastian(power ranger rojo)",
        )

    def interfaz_inicio(self) -> None:
        interfaz_inicio = tk.Frame(
            self, highlightbackground="black", highlightthickness=2
        )
        interfaz_inicio.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        texto_bienvenida = tk.Label(
            interfaz_inicio, text="Bienvenido", font=("Arial", 20)
        )
        texto_bienvenida.pack(anchor="n", padx=5, pady=5)

        texto = "Para empezar a usar la aplicación seleccione una de las opciones listadas en procesos y consultas, recomendamos empezar\
 ingresando un vehiculo que no se encuentre en el parqueadero. Esta aplicación le permitira administrar y realizar servicios\
 varios asociados a un parqueadero con mayor comodidad puesto que solo debera precuparse por introducir los valores correctamente\
 ya que el programa se encargara del resto ;)"

        texto_descripcion = LabelAjustable(
            interfaz_inicio, text=texto, font=("Arial", 12)
        )
        texto_descripcion.pack(padx=5, pady=10, fill="x")
