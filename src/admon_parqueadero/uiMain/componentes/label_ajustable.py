#Funcionalidad del módulo: contiene la clase LabelAjustable que hereda de tk.Label, 
#esta sirve para colocar un texto en la pantalla, y la diferencia con el label
#normal es que este se ajusta al tamaño de la pantalla, segun si se encuentra en
#pantalla completa o la ventana es pequeña.
#Componentes del módulo: LabelAjustable
#Autores: Sofia, Sara, Alejandro, Sebastián, Katherine


import tkinter as tk
from typing import Any


class LabelAjustable(tk.Label):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.bind("<Configure>", lambda _: self._configurar_wraplength())

    def _configurar_wraplength(self) -> None:
        self.config(wraplength=self.winfo_width())
