import tkinter as tk

from admon_parqueadero.uiMain.ventanas.ventana_inicio import VentanaInicio


def main() -> None:
    window = tk.Tk()
    window.geometry("600x400")
    VentanaInicio(window).pack(side="top", fill="both", expand=True)
    window.mainloop()
