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
        self.config(width=round(len(valor_largo) * 1.1))
