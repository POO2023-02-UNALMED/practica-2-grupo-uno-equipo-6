import tkinter as tk
from tkinter import font

from admon_parqueadero.uiMain.componentes.field_frame import FieldFrame


class ventana_principal_usu:
    def __init__(self, ventana):
        # # Crear una fuente en negrita
        self.fuente_negrita = font.Font(weight="bold")
        # Crear una fuente en estilo normal
        self.fuente_normal = font.Font(size=12)

        self.nombre_aplicacion = "PARQUEADERO"
        self.nombre_proceso = "VENDER CARRO"
        self.ventana = ventana
        self.descripcion = "descripcion parqueadero"

        self.construct_ui()

    # def configurar_menu(self) -> None:
    #     menu = tk.Menu(self.master)
    #     menu_inicio = tk.Menu(menu, tearoff=False)
    #     menu.add_cascade(label="Inicio", menu=menu_inicio)
    #     menu_inicio.add_command(label="Salir de la applicacion", command=self.salir)
    #     menu_inicio.add_command(
    #         label="Descripción del sistema", command=self.mostrar_descripcion
    #     )
    #     self.master.config(menu=menu)

    def create(self):
        label1 = tk.Label(
            self.ventana, text=self.nombre_aplicacion, font=self.fuente_negrita
        )
        label1.pack(anchor="nw", padx=10, pady=10)

        frame_1 = tk.Frame(self.ventana, relief="solid", borderwidth=2)
        frame_1.pack(side="top", padx=10, pady=10, fill="both", expand=True)
        self.frame_1 = frame_1

    def nav(self):
        barra_de_botones = tk.Frame(self.frame_1)
        barra_de_botones.pack(fill="both")
        botones = ["Archivo", "Procesos y Consultas", "Ayuda"]
        row = 0
        for indice in range(0, len(botones)):
            boton2 = tk.Button(barra_de_botones, text=botones[indice])
            boton2.grid(row=row, column=indice)

    def form(self):
        frame_3 = tk.Frame(self.frame_1)
        frame_3.pack(fill="both")

        label1 = tk.Label(
            frame_3,
            text=self.nombre_proceso,
            borderwidth=1,
            relief="solid",
            font=self.fuente_normal,
        )
        label1.pack(side="top", padx=10, pady=10)

        label1 = tk.Label(
            frame_3,
            text=self.descripcion,
            borderwidth=1,
            width=70,
            height=3,
            relief="solid",
            font=self.fuente_negrita,
        )
        label1.pack(side="top", expand=True)

        container_form = tk.Frame(frame_3, relief="solid", borderwidth=2)
        container_form.pack(side="top", padx=100, pady=60, fill="both", expand=True)

        criterios = ["Codigo", "Nombre", "Descripcion", "Ubicacion"]
        FieldFrame(container_form, "Criterio", criterios, "Valor", None, None).pack()

        frame_botones = tk.Frame(container_form)
        frame_botones.pack()

        boton_enviar = tk.Button(frame_botones, text="Ingresar")
        boton_enviar.grid(row=0, column=0)

        boton_borrar = tk.Button(frame_botones, text="Borrar")
        boton_borrar.grid(row=0, column=1)

    def get_framepadre(self):
        return self.frame_1

    def construct_ui(self):
        self.create()
        self.nav()
        self.form()
