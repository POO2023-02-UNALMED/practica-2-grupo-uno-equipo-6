import tkinter as tk


class LabelAjustable(tk.Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Configure>", lambda _: self.configure_wraplength())

    def configure_wraplength(self):
        self.config(wraplength=self.winfo_width())
