from importlib.abc import Traversable
from importlib.resources import as_file
from collections.abc import Callable, Iterable, Iterator
import tkinter as tk
from tkinter import font
from typing import Any, TypeVar, TypedDict

from admon_parqueadero.uiMain.componentes.label_ajustable import LabelAjustable
from admon_parqueadero.utils import ruta_imagen, ruta_imagenes


class VentanaInicio(tk.Frame):
    def __init__(self, master: tk.Tk, *args: Any, **kwargs: Any) -> None:
        super().__init__(master, *args, **kwargs)
        self.master: tk.Tk = master

        master.wm_title("Inicio")
        self._configurar_menu()
        self._configurar_frames_izq()
        self._configuar_frames_der()

    def _configurar_menu(self) -> None:
        menu = tk.Menu(self.master)
        menu_inicio = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Inicio", menu=menu_inicio)
        menu_inicio.add_command(label="Salir de la applicacion", command=self._salir)
        menu_inicio.add_command(
            label="Descripción del sistema", command=self._mostrar_descripcion
        )
        self.master.config(menu=menu)

    def _configurar_frames_izq(self) -> None:
        frame_izq = tk.Frame(self)
        frame_izq.place(relwidth=0.5, relheight=1)

        p1 = tk.Frame(frame_izq, highlightbackground="black", highlightthickness=2)
        p1.pack(expand=True, fill="both", padx=(10, 5), pady=10)

        p3 = tk.Frame(p1, highlightbackground="black", highlightthickness=2)
        p3.pack(side="top", padx=10, pady=10, fill="x")

        self.p4 = tk.Frame(p1, highlightbackground="black", highlightthickness=2)
        self.p4.pack(side="bottom", padx=10, pady=10, fill="both", expand=True)

        msg_bienvenida = LabelAjustable(
            p3,
            text="Bienvenido al Parqueadero. Aquí podrá guardar su(s) vehículo(s), sea carro y/o moto. Podrá obtener distintos servicios de revisión, de cambio de repuestos y más, además podrá comprar el carro que desee o vender uno de su propiedad. Asimismo se logrará acceder a la administración del parqueadero y ser manejado para realizar varios procesos por el encargado.",
        )
        msg_bienvenida.pack(expand=True, fill="x", padx=10, pady=10)

        self._configurar_p4()

    def _configuar_frames_der(self) -> None:
        frame_der = tk.Frame(self)
        frame_der.place(relx=0.5, relwidth=0.5, relheight=1)

        p2 = tk.Frame(frame_der, highlightbackground="black", highlightthickness=2)
        p2.pack(expand=True, fill="both", padx=(5, 10), pady=10)

        class Desarrollador(TypedDict):
            biografia: list[tuple[str, str]]
            fotos: tuple[str, str, str, str]

        desarrolladores: list[Desarrollador] = [
            {
                "biografia": [
                    ("Nombre", "Sara Isabel Suárez Londoño"),
                    ("Fecha de nacimiento", "2004/02/20"),
                    (
                        "Información básica",
                        "Estudiante de tercer semestre de Ingeniería de Sistemas e Informática. Le gusta escuchar música y programar.",
                    ),
                ],
                "fotos": (
                    "blanco2.png",
                    "blancos.png",
                    "blanco3.png",
                    # "300x300_azul.png",
                    "carnet1.png"
                
                ),
            },
            {
                "biografia": [
                    ("Nombre", "Juan Sebastián Pabuena Gómez"),
                    ("Fecha de nacimiento", "2005/06/10"),
                    (
                        "Información básica",
                        "Estudiante de tercer semestre de Ingeniería de Sistemas e Informática. Le gusta dormir y escuchar música.",
                    ),
                ],
                "fotos": (
                    "powerAzul3.png",
                    "azul22.png",
                    "Azul3.png",
                    "300x300_verde.png",
                ),
            },
            {
                "biografia": [
                    ("Nombre", "Sofía Giraldo López"),
                    ("Fecha de nacimiento", "2003/05/02"),
                    (
                        "Información básica",
                        "Estudiante de tercer semestre de Ingeniería de Sistemas e Informática. Le gusta ver series y aprender cosas nuevas.",
                    ),
                ],
                "fotos": (
                    "powerRosa1.png",
                    "imagen2sofi.png",
                    "poweRosa3.png",
                    "poweRosa4.png",
                ),
            },
            {
                "biografia": [
                    ("Nombre", "Alejandro Arias Orozco"),
                    ("Fecha de nacimiento", "2003/05/09"),
                    (
                        "Información básica",
                        "Estudiante de segundo semestre de Ingeniería de Sistemas e Informática. Le gusta ver series y películas.",
                    ),
                ],
                "fotos": (
                    "rojo1.png",
                    "rojo2.png",
                    "300x300_naranja.png",
                    "300x300_naranja.png",
                ),
            },
            {
                "biografia": [
                    ("Nombre", "Katherine Del Pilar Puentes Basilio"),
                    ("Fecha de nacimiento", "2005/01/13"),
                    (
                        "Información básica",
                        "Estudiante de segundo semestre de Ingeniería de Sistemas e Informática. Le gusta jugar voleibol y el helado.",
                    ),
                ],
                "fotos": (
                    "300x300_gris.png",
                    "300x300_gris.png",
                    "300x300_gris.png",
                    "300x300_gris.png",
                ),
            },
        ]

        biografias = map(lambda d: d["biografia"], desarrolladores)
        self.p5 = Biografias(
            p2, biografias, highlightbackground="black", highlightthickness=2
        )
        self.p5.pack(side="top", padx=10, pady=10, fill="x")

        fotos = map(lambda d: self._encontrar_fotos(d["fotos"]), desarrolladores)
        self.p6 = GridFotos(
            p2, fotos, highlightbackground="black", highlightthickness=2
        )
        self.p6.pack(side="bottom", expand=True)

        self.p5.bind_click(self._siguiente_desarrollador)

    def _salir(self) -> None:
        self.master.destroy()

    def _mostrar_descripcion(self) -> None:
        if self.btn_ingreso not in [widget for widget in self.p4.winfo_children()]:
            return
        self.imagenes.destroy()
        self.btn_ingreso.destroy()

        self.descripcion = tk.Frame(self.p4)
        self.descripcion.pack(expand=True, fill="both", padx=10)

        texto_descripcion = LabelAjustable(
            self.descripcion,
            text="Esta aplicación permite administrar de manera conjunta varios establecimientos pertenecientes a un Parqueadero. Especificamente contiene las herramientas necesarias para administrar un parqueadero, comprar y vender vehiculos además de ofrecer servicio de taller y demás servicios similares.",
        )
        texto_descripcion.pack(expand=True, fill="both")

        boton_regresar = tk.Button(
            self.descripcion, text="Regresar", command=self._regresar_de_la_descripcion
        )
        boton_regresar.pack(side="bottom", padx=10, pady=10)

    def _regresar_de_la_descripcion(self) -> None:
        self.descripcion.destroy()
        self._configurar_p4()

    def _configurar_p4(self) -> None:
        self.imagenes = Imagenes(self.p4)
        self.imagenes.pack(side="top", expand=True, fill="both")
        self.btn_ingreso = tk.Button(self.p4, text="Ingresar", command=self._ingresar)
        self.btn_ingreso.pack(side="bottom", padx=10, pady=10)

    def _ingresar(self) -> None:
        from .ventana_principal_usu import ventana_principal_usu

        self.destroy()
        self.master.config(menu=tk.Menu())
        ventana_principal_usu(self.master).pack(side="top", fill="both", expand=True)

    def _siguiente_desarrollador(self) -> None:
        self.p5.siguiente_biografia()
        self.p6.siguiente_imagen()

    def _encontrar_fotos(
        self, fotos: tuple[str, str, str, str]
    ) -> tuple[Traversable, Traversable, Traversable, Traversable]:
        d = ruta_imagenes()
        return (
            d.joinpath(fotos[0]),
            d.joinpath(fotos[1]),
            d.joinpath(fotos[2]),
            d.joinpath(fotos[3]),
        )


class Biografias(tk.Frame):
    def __init__(
        self,
        master: tk.Misc,
        biografias: Iterator[list[tuple[str, str]]],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(master, *args, **kwargs)
        self.biografias = infinito(biografias)

        self.label_titulo = LabelAjustable(
            self,
            text="Breve hoja de vida de los desarrolladores",
            font=font.Font(weight=font.BOLD),
        )
        self.label_titulo.pack(pady=10, padx=10, fill="x")

        self.label_biografia = LabelAjustable(self)
        self.siguiente_biografia()
        self.label_biografia.pack(fill="x", padx=10)

        self.label_nota = LabelAjustable(
            self,
            text="Click para cambiar de desarrollador",
            font=font.Font(slant=font.ITALIC, size=9),
            foreground="blue",
        )
        self.label_nota.pack(fill="x", pady=10)

    def bind_click(self, func: Callable[[], None]) -> None:
        self.bind("<Button-1>", lambda _: func())
        self.label_titulo.bind("<Button-1>", lambda _: func())
        self.label_biografia.bind("<Button-1>", lambda _: func())
        self.label_nota.bind("<Button-1>", lambda _: func())

    def siguiente_biografia(self) -> None:
        actual = next(self.biografias)
        self.label_biografia.config(text=self._biografia_str(actual))

    def _biografia_str(self, biografia: list[tuple[str, str]]) -> str:
        return "\n".join(f"{k}: {v}" for k, v in biografia)


class Imagenes(tk.Frame):
    def __init__(self, master: tk.Misc, *args: Any, **kwargs: Any) -> None:
        super().__init__(master, *args, **kwargs)

        self.imagenes = infinito(
            [  # TODO: agregar las 5 imagenes
                "mecanico.png",
                "Carro1.png",
                "cars1.png",
                "cars2.png",
                "ventaAuto.png",
            ]
        )

        self.photo_image = tk.PhotoImage()
        self.siguiente_imagen()
        self.label = tk.Label(self, image=self.photo_image)
        self.label.pack(expand=True)
        self.label.bind("<Enter>", lambda _: self.siguiente_imagen())

    def siguiente_imagen(self) -> None:
        imagen = next(self.imagenes)
        ruta = ruta_imagen(imagen)
        with as_file(ruta) as file:
            self.photo_image.config(file=file)


class GridFotos(tk.Frame):
    def __init__(
        self,
        master: tk.Misc,
        fotos: Iterator[tuple[Traversable, Traversable, Traversable, Traversable]],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(master, *args, **kwargs)
        self.fotos = infinito(fotos)

        self.photo_img0_0 = tk.PhotoImage()
        self.photo_img0_1 = tk.PhotoImage()
        self.photo_img1_0 = tk.PhotoImage()
        self.photo_img1_1 = tk.PhotoImage()
        self.siguiente_imagen()

        self.label_img0_0 = tk.Label(self, image=self.photo_img0_0)
        self.label_img0_0.grid(row=0, column=0)

        self.label_img0_1 = tk.Label(self, image=self.photo_img0_1)
        self.label_img0_1.grid(row=0, column=1)

        self.label_img1_0 = tk.Label(self, image=self.photo_img1_0)
        self.label_img1_0.grid(row=1, column=0)

        self.label_img1_1 = tk.Label(self, image=self.photo_img1_1)
        self.label_img1_1.grid(row=1, column=1)

    def siguiente_imagen(self) -> None:
        actual = next(self.fotos)
        print(actual[0])
        with (
            as_file(actual[0]) as f0,
            as_file(actual[1]) as f1,
            as_file(actual[2]) as f2,
            as_file(actual[3]) as f3,
        ):
            self.photo_img0_0.config(file=f0)
            self.photo_img0_1.config(file=f1)
            self.photo_img1_0.config(file=f2)
            self.photo_img1_1.config(file=f3)


T = TypeVar("T")


def infinito(iterator: Iterable[T]) -> Iterator[T]:
    l = list(iterator)
    i = 0
    limite = len(l)
    while True:
        if i == limite:
            i = 0
        yield l[i]
        i += 1
