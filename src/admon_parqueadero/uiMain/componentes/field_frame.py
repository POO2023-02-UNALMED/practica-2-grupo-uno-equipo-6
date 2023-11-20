import tkinter as tk
from tkinter import ttk
from tkinter import font
from typing import Any, Callable, Literal, Optional, TypeVar, Union
from admon_parqueadero.errores import ErrorNumeroEsperado, ErrorValorEsperado


T = TypeVar("T")


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
        titulo: Optional[str] = None,
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

        if titulo is not None:
            tk.Label(self, text=titulo, font=font.Font(weight="bold", size=9)).pack(pady=(0, 15))

        frame_formulario = tk.Frame(self)
        frame_formulario.pack()
        frame_formulario.grid_columnconfigure(0, pad=20)

        tk.Label(frame_formulario, text=tituloCriterios.upper()).grid(row=0, column=0)
        tk.Label(frame_formulario, text=tituloValores.upper()).grid(row=0, column=1)

        self._entradas: dict[str, Union[tk.Entry, ttk.Combobox]] = {}
        self._combobox_textvariables: dict[str, tk.StringVar] = {}
        for i, criterio in enumerate(criterios):
            tk.Label(frame_formulario, text=criterio, justify="left", anchor="w").grid(
                row=i + 1, column=0, sticky="w"
            )
            
            entrada: Union[tk.Entry, ttk.Combobox]
            if (opciones := combobox.get(criterio)) is not None:
                self._combobox_textvariables[criterio] = tk.StringVar(
                    value=FieldFrame._COMBOBOX_TEXTO
                )
                entrada = ttk.Combobox(
                    frame_formulario,
                    values=opciones,
                    textvariable=self._combobox_textvariables[criterio],
                    state="readonly",
                )
                entrada.grid(row=i + 1, column=1)

                if valores is not None and (v := valores[i]) is not None:
                    entrada.set(v)
            else:
                entrada = tk.Entry(frame_formulario)
                entrada.grid(row=i + 1, column=1)

                if valores is not None and (v := valores[i]) is not None:
                    entrada.insert(0, v)

            if habilitado is not None and criterio in habilitado:
                entrada.config(state=tk.DISABLED)
            self._entradas[criterio] = entrada
            frame_formulario.grid_rowconfigure(i + 1, pad=20)

    def getValue(self, criterio: str) -> str:
        """
        @arg criterio el criterio cuyo valor se quiere obtener
        @return el valor del criterio cuyo nombre es 'criterio'
        """
        entrada = self._entradas[criterio]
        v = entrada.get().strip()
        if len(v) == 0 or (isinstance(entrada, ttk.Combobox) and v == FieldFrame._COMBOBOX_TEXTO):
            raise ErrorValorEsperado(criterio)
        return v

    def getValueNumero(self, criterio: str, tipo: Callable[[str], T]) -> T:
        v = self.getValue(criterio)
        try:
            return tipo(v)
        except ValueError:
            raise ErrorNumeroEsperado(criterio)

    def borrar(self) -> None:
        for criterio, entrada in self._entradas.items():
            if isinstance(entrada, ttk.Combobox):
                entrada.set("")
                self._combobox_textvariables[criterio].set(FieldFrame._COMBOBOX_TEXTO)
            else:
                entrada.delete(0, tk.END)

    #metodo para cambiar el estado de una entrada segun su criterio
    def cambiar_estado(self, criterio: str, opcion: Literal['normal', 'readonly', 'disabled']) -> None:
        #ver que hacer con el argumento opcion
        entrada = self._entradas[criterio]
        entrada.config(state=opcion)
        
        
