"""Documentación de arquitectura generada desde el código de F3."""
import inspect
import pandas as pd
from . import poo


def tabla_arquitectura() -> pd.DataFrame:
    clases = [
        poo.Transformador,
        poo.TransformadorTipos,
        poo.TransformadorTextos,
        poo.TransformadorCategorias,
        poo.TransformadorGeografia,
        poo.TransformadorEfectividad,
        poo.PipelineSIMCE,
    ]
    filas = []
    for cls in clases:
        base = next((b.__name__ for b in cls.__bases__ if b is not object), "object")
        metodos = [n for n, v in inspect.getmembers(cls, inspect.isfunction) if not n.startswith("_")]
        filas.append({
            "clase": cls.__name__,
            "hereda_de": base,
            "responsabilidad": (inspect.getdoc(cls) or "").split("\n")[0],
            "metodos_publicos": ", ".join(metodos),
            "modulo": "src/poo.py",
        })
    return pd.DataFrame(filas)