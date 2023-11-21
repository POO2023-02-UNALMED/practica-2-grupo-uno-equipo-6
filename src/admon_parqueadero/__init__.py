import logging
import tkinter as tk

from admon_parqueadero.uiMain.ventanas.ventana_inicio import VentanaInicio


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    window = tk.Tk()
    window.geometry("960x540")
    window.state('zoomed')
    VentanaInicio(window).pack(side="top", fill="both", expand=True)
    window.mainloop()