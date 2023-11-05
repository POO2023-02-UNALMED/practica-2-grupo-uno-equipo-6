import tkinter as tk

from .uiMain.ventanas.ventana_inicio import VentanaInicio


def main() -> None:
    window = tk.Tk()
    window.geometry("960x540")
    VentanaInicio(window).pack(side="top", fill="both", expand=True)
    window.mainloop()
