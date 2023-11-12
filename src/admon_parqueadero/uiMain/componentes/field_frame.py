import tkinter as tk
from typing import Any, Optional


class FieldFrame(tk.Frame):
    def __init__(
        self,
        master: tk.Misc,
        tituloCriterios: str,
        criterios: list[str],
        tituloValores: str,
        valores: Optional[list[str]],
        habilitado: Optional[list[str]],
        *args: Any,
        **kwargs: Any,
    ):
        """
        crea un nuevo objeto de tipo FieldFrame
        @arg tituloCriterios titulo para la columna "Criterio"
        @arg criterios array con los nombres de los criterios
        @arg tituloValores titulo para la columna "valor"
        @arg valores array con los valores iniciales; Si ‘None’, no hay valores iniciales
        @arg habilitado array con los campos no-editables por el usuario; Si ‘None’, todos son editables
        """
        super().__init__(master, *args, **kwargs)

        tk.Label(self, text=tituloCriterios.upper()).grid(row=0, column=0)
        tk.Label(self, text=tituloValores.upper()).grid(row=0, column=1)
        self.grid_rowconfigure(0, pad=10)

        self.entradas: dict[str, tk.Entry] = {}
        for i, criterio in enumerate(criterios):
            tk.Label(self, text=criterio, justify="left", anchor="w").grid(
                row=i + 1, column=0, sticky="w"
            )
            entrada = tk.Entry(self)
            entrada.grid(row=i + 1, column=1)
            if valores is not None and (v := valores[i]) is not None:
                entrada.insert(0, v)
            if habilitado is not None and criterio in habilitado:
                entrada.config(state=tk.DISABLED)
            self.entradas[criterio] = entrada
            self.grid_rowconfigure(i + 1, pad=10)

    def getValue(self, criterio: str) -> str:
        """
        @arg criterio el criterio cuyo valor se quiere obtener
        @return el valor del criterio cuyo nombre es 'criterio'
        """
        entrada = self.entradas[criterio]
        return entrada.get()
