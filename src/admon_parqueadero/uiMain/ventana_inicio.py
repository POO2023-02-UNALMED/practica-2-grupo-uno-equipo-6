import tkinter as tk


class VentanaInicio(tk.Frame):
    def __init__(self, master: tk.Tk, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.parent = master

        master.wm_title("Inicio")
        self.configurar_menu()
        self.configurar_frames_izq()
        self.configuar_frames_der()

    def configurar_menu(self):
        menu = tk.Menu(self.parent)
        menu_inicio = tk.Menu(menu)
        menu.add_cascade(label="Inicio", menu=menu_inicio)
        menu_inicio.add_command(label="Salir de la applicacion", command=self.salir)
        menu_inicio.add_command(
            label="Descripción del sistema", command=self.mostrar_descripcion
        )
        self.parent.config(menu=menu)

    def configurar_frames_izq(self):
        frame_izq = tk.Frame(self)
        frame_izq.place(relwidth=0.5, relheight=1)

        p1 = tk.Frame(frame_izq, highlightbackground="black", highlightthickness=2)
        p1.pack(expand=True, fill="both", padx=(10, 5), pady=10)

        p3 = tk.Frame(p1, highlightbackground="black", highlightthickness=2)
        p3.pack(side="top", padx=10, pady=10, fill="x")

        p4 = tk.Frame(p1, highlightbackground="black", highlightthickness=2)
        p4.pack(side="bottom", padx=10, pady=10)

        msg_bienvenida = tk.Label(  # TODO: poner el mensaje de bienvenida
            p3,
            text="Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.",
        )
        msg_bienvenida.bind(
            "<Configure>",
            lambda _: msg_bienvenida.config(wraplength=msg_bienvenida.winfo_width()),
        )
        msg_bienvenida.pack(expand=True, fill="x")

    def configuar_frames_der(self):
        frame_der = tk.Frame(self)
        frame_der.place(relx=0.5, relwidth=0.5, relheight=1)

        p2 = tk.Frame(frame_der, highlightbackground="black", highlightthickness=2)
        p2.pack(expand=True, fill="both", padx=(5, 10), pady=10)

        p5 = tk.Frame(p2, highlightbackground="black", highlightthickness=2)
        p5.pack(side="top")

        p6 = tk.Frame(p2, highlightbackground="black", highlightthickness=2)
        p6.pack(side="bottom")


    def salir(self):
        self.parent.destroy()

    def mostrar_descripcion(self):
        pass
