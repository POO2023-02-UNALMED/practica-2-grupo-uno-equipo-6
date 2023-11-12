import tkinter as tk
from typing import Any


class LabelAjustable(tk.Label):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.bind("<Configure>", lambda _: self.configurar_wraplength())

    def configurar_wraplength(self) -> None:
        self.config(wraplength=self.winfo_width())
