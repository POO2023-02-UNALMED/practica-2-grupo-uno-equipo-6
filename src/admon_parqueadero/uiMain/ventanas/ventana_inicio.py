from pathlib import Path
import tkinter as tk
from typing import Any, Optional

from admon_parqueadero.uiMain.widgets.label_ajustable import LabelAjustable


class VentanaInicio(tk.Frame):
    def __init__(self, master: tk.Tk, *args: Any, **kwargs: Any) -> None:
        super().__init__(master, *args, **kwargs)
        self.parent = master

        master.wm_title("Inicio")
        self.configurar_menu()
        self.configurar_frames_izq()
        self.configuar_frames_der()

    def configurar_menu(self) -> None:
        menu = tk.Menu(self.parent)
        menu_inicio = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Inicio", menu=menu_inicio)
        menu_inicio.add_command(label="Salir de la applicacion", command=self.salir)
        menu_inicio.add_command(
            label="Descripción del sistema", command=self.mostrar_descripcion
        )
        self.parent.config(menu=menu)

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

        imagenes = Imagenes(p4)
        imagenes.pack(side="top", expand=True, fill="both")

        btn_ingreso = tk.Button(p4, text="Ingresar", command=self.ingresar)
        btn_ingreso.pack(side="bottom", padx=10, pady=10)

    def configuar_frames_der(self) -> None:
        frame_der = tk.Frame(self)
        frame_der.place(relx=0.5, relwidth=0.5, relheight=1)

        p2 = tk.Frame(frame_der, highlightbackground="black", highlightthickness=2)
        p2.pack(expand=True, fill="both", padx=(5, 10), pady=10)

        p5 = Biografias(p2, highlightbackground="black", highlightthickness=2)
        p5.pack(side="top", padx=10, pady=10, fill="x")

        p6 = tk.Frame(p2, highlightbackground="black", highlightthickness=2)
        p6.pack(side="bottom")

    def salir(self) -> None:
        self.parent.destroy()

    def mostrar_descripcion(self) -> None:
        pass

    def ingresar(self) -> None:
        pass


class Biografias(tk.Frame):
    def __init__(self, master: tk.Misc, *args: Any, **kwargs: Any) -> None:
        super().__init__(master, *args, **kwargs)

        self.biografia_mostrada = 0
        self.biografias = [  # TODO: poner biografias
            [
                ("Nombre", "abc"),
                ("Fecha de nacimiento", "..."),
            ],
            [
                ("Nombre", "def"),
                ("Fecha de nacimiento", "..."),
            ],
            [
                ("Nombre", "ghi"),
                ("Fecha de nacimiento", "..."),
            ],
            [
                ("Nombre", "jkl"),
                ("Fecha de nacimiento", "..."),
            ],
            [
                ("Nombre", "mno"),
                ("Fecha de nacimiento", "..."),
            ],
        ]

        self.label_titulo = LabelAjustable(
            self, text="Breve hoja de vida de los desarrolladores", font="Arial 12 bold"
        )
        self.label_titulo.pack(pady=10, padx=10, fill="x")

        self.label_biografia = LabelAjustable(self, text=self.biografia_str(0))
        self.label_biografia.pack(fill="x", padx=10)

        self.label_nota = LabelAjustable(
            self,
            text="Click para cambiar de desarrollador",
            font="Arial 9 italic",
            foreground="blue",
        )
        self.label_nota.pack(fill="x", pady=10)

        self.bind("<Button-1>", lambda _: self.cambiar_biografia())
        self.label_titulo.bind("<Button-1>", lambda _: self.cambiar_biografia())
        self.label_biografia.bind("<Button-1>", lambda _: self.cambiar_biografia())
        self.label_nota.bind("<Button-1>", lambda _: self.cambiar_biografia())

    def cambiar_biografia(self) -> None:
        self.biografia_mostrada += 1
        if self.biografia_mostrada == len(self.biografias):
            self.biografia_mostrada = 0
        self.label_biografia.config(text=self.biografia_str(self.biografia_mostrada))

    def biografia_str(self, indice_biografia: int) -> str:
        biografia = self.biografias[indice_biografia]
        return "\n".join(f"{k}: {v}" for k, v in biografia)


class Imagenes(tk.Frame):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.raiz = Imagenes.encontrar_raiz_proyecto()
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
        file = self.raiz / "imagenes" / imagen
        self.photo_image.config(file=file)

    def cambiar_imagen(self) -> None:
        self.imagen_mostrada += 1
        if self.imagen_mostrada == len(self.imagenes):
            self.imagen_mostrada = 0
        self.configurar_archivo_imagen()

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
        return Imagenes.encontrar_raiz_proyecto(desde.parent, n + 1)
