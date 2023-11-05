from collections.abc import Callable, Iterator
from pathlib import Path
import tkinter as tk
from typing import Any, Optional, TypeVar, TypedDict

from admon_parqueadero.uiMain.widgets.label_ajustable import LabelAjustable


class VentanaInicio(tk.Frame):
    def __init__(self, master: tk.Tk, *args: Any, **kwargs: Any) -> None:
        super().__init__(master, *args, **kwargs)
        self.master: tk.Tk = master
        self.raiz = VentanaInicio.encontrar_raiz_proyecto()

        master.wm_title("Inicio")
        self.configurar_menu()
        self.configurar_frames_izq()
        self.configuar_frames_der()

    def configurar_menu(self) -> None:
        menu = tk.Menu(self.master)
        menu_inicio = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Inicio", menu=menu_inicio)
        menu_inicio.add_command(label="Salir de la applicacion", command=self.salir)
        menu_inicio.add_command(
            label="Descripción del sistema", command=self.mostrar_descripcion
        )
        self.master.config(menu=menu)

    def configurar_frames_izq(self) -> None:
        frame_izq = tk.Frame(self)
        frame_izq.place(relwidth=0.5, relheight=1)

        p1 = tk.Frame(frame_izq, highlightbackground="black", highlightthickness=2)
        p1.pack(expand=True, fill="both", padx=(10, 5), pady=10)

        p3 = tk.Frame(p1, highlightbackground="black", highlightthickness=2)
        p3.pack(side="top", padx=10, pady=10, fill="x")

        p4 = tk.Frame(p1, highlightbackground="black", highlightthickness=2)
        p4.pack(side="bottom", padx=10, pady=10, fill="both", expand=True)

        msg_bienvenida = LabelAjustable(  # TODO: poner el mensaje de bienvenida
            p3,
            text="Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.",
        )
        msg_bienvenida.pack(expand=True, fill="x", padx=10, pady=10)

        imagenes = Imagenes(p4, self.raiz)
        imagenes.pack(side="top", expand=True, fill="both")

        btn_ingreso = tk.Button(p4, text="Ingresar", command=self.ingresar)
        btn_ingreso.pack(side="bottom", padx=10, pady=10)

    def configuar_frames_der(self) -> None:
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
                    ("Nombre", "abc"),
                    ("Fecha de nacimiento", "..."),
                ],
                "fotos": (
                    "300x300_azul.png",
                    "300x300_azul.png",
                    "300x300_azul.png",
                    "300x300_azul.png",
                ),
            },
            {
                "biografia": [
                    ("Nombre", "def"),
                    ("Fecha de nacimiento", "..."),
                ],
                "fotos": (
                    "300x300_verde.png",
                    "300x300_verde.png",
                    "300x300_verde.png",
                    "300x300_verde.png",
                ),
            },
            {
                "biografia": [
                    ("Nombre", "ghi"),
                    ("Fecha de nacimiento", "..."),
                ],
                "fotos": (
                    "300x300_rojo.png",
                    "300x300_rojo.png",
                    "300x300_rojo.png",
                    "300x300_rojo.png",
                ),
            },
            {
                "biografia": [
                    ("Nombre", "jkl"),
                    ("Fecha de nacimiento", "..."),
                ],
                "fotos": (
                    "300x300_naranja.png",
                    "300x300_naranja.png",
                    "300x300_naranja.png",
                    "300x300_naranja.png",
                ),
            },
            {
                "biografia": [
                    ("Nombre", "mno"),
                    ("Fecha de nacimiento", "..."),
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

        fotos = map(lambda d: self.encontrar_fotos(d["fotos"]), desarrolladores)
        self.p6 = GridFotos(
            p2, fotos, highlightbackground="black", highlightthickness=2
        )
        self.p6.pack(side="bottom", expand=True)

        self.p5.bind_click(self.siguiente_desarrollador)

    def salir(self) -> None:
        self.master.destroy()

    def mostrar_descripcion(self) -> None:
        pass

    def ingresar(self) -> None:
        pass

    def siguiente_desarrollador(self) -> None:
        self.p5.siguiente_biografia()
        self.p6.siguiente_imagen()

    @staticmethod
    def encontrar_raiz_proyecto(desde: Optional[Path] = None, n: int = 0) -> Path:
        if n > 10:
            print(
                "Advertencia: No fue encontrada la raiz del proyecto, usando la carpeta superior"
            )
            return Path("..")
        if desde is None:
            desde = Path.cwd()
        if "pyproject.toml" in map(lambda p: p.name, desde.iterdir()):
            return desde
        return VentanaInicio.encontrar_raiz_proyecto(desde.parent, n + 1)

    def encontrar_fotos(
        self, fotos: tuple[str, str, str, str]
    ) -> tuple[Path, Path, Path, Path]:
        return (
            ruta_imagen(self.raiz, fotos[0]),
            ruta_imagen(self.raiz, fotos[1]),
            ruta_imagen(self.raiz, fotos[2]),
            ruta_imagen(self.raiz, fotos[3]),
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
            self, text="Breve hoja de vida de los desarrolladores", font="Arial 12 bold"
        )
        self.label_titulo.pack(pady=10, padx=10, fill="x")

        self.label_biografia = LabelAjustable(self)
        self.siguiente_biografia()
        self.label_biografia.pack(fill="x", padx=10)

        self.label_nota = LabelAjustable(
            self,
            text="Click para cambiar de desarrollador",
            font="Arial 9 italic",
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
        self.label_biografia.config(text=self.biografia_str(actual))

    def biografia_str(self, biografia: list[tuple[str, str]]) -> str:
        return "\n".join(f"{k}: {v}" for k, v in biografia)


class Imagenes(tk.Frame):
    def __init__(self, master: tk.Misc, raiz: Path, *args: Any, **kwargs: Any) -> None:
        super().__init__(master, *args, **kwargs)
        self.raiz = raiz

        self.imagen_mostrada = 0
        self.imagenes = [  # TODO: agregar las 5 imagenes
            "300x300_rojo.png",
            "300x300_naranja.png",
            "300x300_gris.png",
            "300x300_verde.png",
            "300x300_azul.png",
        ]

        self.photo_image = tk.PhotoImage()
        self.configurar_archivo_imagen()
        self.label = tk.Label(self, image=self.photo_image)
        self.label.pack(expand=True)
        self.label.bind("<Enter>", lambda _: self.cambiar_imagen())

    def configurar_archivo_imagen(self) -> None:
        imagen = self.imagenes[self.imagen_mostrada]
        file = ruta_imagen(self.raiz, imagen)
        self.photo_image.config(file=file)

    def cambiar_imagen(self) -> None:
        self.imagen_mostrada += 1
        if self.imagen_mostrada == len(self.imagenes):
            self.imagen_mostrada = 0
        self.configurar_archivo_imagen()


class GridFotos(tk.Frame):
    def __init__(
        self,
        master: tk.Misc,
        fotos: Iterator[tuple[Path, Path, Path, Path]],
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
        self.photo_img0_0.config(file=actual[0])
        self.photo_img0_1.config(file=actual[1])
        self.photo_img1_0.config(file=actual[2])
        self.photo_img1_1.config(file=actual[3])


def ruta_imagen(raiz: Path, imagen: str) -> Path:
    return raiz / "imagenes" / imagen


T = TypeVar("T")


def infinito(iterator: Iterator[T]) -> Iterator[T]:
    l = list(iterator)
    i = 0
    limite = len(l)
    while True:
        if i == limite:
            i = 0
        yield l[i]
        i += 1
