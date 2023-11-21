#Funcionalidad del módulo: contiene la clase combobox que hereda de ttk.Combobox, 
#sirve para mostrar una lista de opciones, y ajusta de manera automatica 
#su tamaño según la información que se le ingrese.
#Componentes del módulo: Combobox
#Autores: Sofia, Sara, Alejandro, Sebastián, Katherine


import tkinter as tk
from tkinter import ttk


class ComboboxAjustable(ttk.Combobox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._valor_inicial = None
        if (v := kwargs.get("textvariable")) is not None:
            self._valor_inicial = v.get()
        self.bind("<Configure>", self._configurar)

    def _configurar(self, event: tk.Event):
        combo: ttk.Combobox = event.widget
        valores = combo.cget("values")
        if len(valores) == 0:
            return
        valor_largo = max(valores, key=len)
        if self._valor_inicial is not None and len(self._valor_inicial) > len(valor_largo):
            valor_largo = self._valor_inicial
        self.config(width=len(valor_largo))
