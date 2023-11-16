import tkinter as tk
from tkinter import ttk
from typing import Any, Optional, Union


class FieldFrame(tk.Frame):
    _COMBOBOX_TEXTO = "Seleccione una opción"

    def __init__(
        self,
        master: tk.Misc,
        tituloCriterios: str,
        criterios: list[str],
        tituloValores: str,
        valores: Optional[list[Optional[str]]],
        habilitado: Optional[list[str]],
        combobox: dict[str, list[str]] = {},
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
        @arg valores combobox {clave: Nombre critero  , valor: [valor1, valor2, ...]}
        """

        if valores is not None:
            assert len(criterios) == len(valores), "hay criterios sin valores por defecto"

        super().__init__(master, *args, **kwargs)

        tk.Label(self, text=tituloCriterios.upper()).grid(row=0, column=0)
        tk.Label(self, text=tituloValores.upper()).grid(row=0, column=1)
        self.columnconfigure(0, pad=20)

        self.entradas: dict[str, Union[tk.Entry, ttk.Combobox]] = {}
        self.combobox_textvariables: dict[str, tk.StringVar] = {}
        for i, criterio in enumerate(criterios):
            tk.Label(self, text=criterio, justify="left", anchor="w").grid(
                row=i + 1, column=0, sticky="w"
            )

            entrada: Union[tk.Entry, ttk.Combobox]
            if (opciones := combobox.get(criterio)) is not None:
                self.combobox_textvariables[criterio] = tk.StringVar(value=FieldFrame._COMBOBOX_TEXTO)
                entrada = ttk.Combobox(
                    self,
                    values=opciones,
                    textvariable=self.combobox_textvariables[criterio],
                    state="readonly",
                )
                entrada.grid(row=i + 1, column=1)

                if valores is not None and (v := valores[i]) is not None:
                    entrada.set(v)
            else:
                entrada = tk.Entry(self)
                entrada.grid(row=i + 1, column=1)

                if valores is not None and (v := valores[i]) is not None:
                    entrada.insert(0, v)

            if habilitado is not None and criterio in habilitado:
                entrada.config(state=tk.DISABLED)
            self.entradas[criterio] = entrada
            self.grid_rowconfigure(i + 1, pad=20)

    def getValue(self, criterio: str) -> str:
        """
        @arg criterio el criterio cuyo valor se quiere obtener
        @return el valor del criterio cuyo nombre es 'criterio'
        """
        entrada = self.entradas[criterio]
        return entrada.get()

    def borrar(self) -> None:
        for criterio, entrada in self.entradas.items():
            if isinstance(entrada, ttk.Combobox):
                entrada.set("")
                self.combobox_textvariables[criterio].set(FieldFrame._COMBOBOX_TEXTO)
            else:
                entrada.delete(0, tk.END)
