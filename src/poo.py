"""Núcleo orientado a objetos de F3 para el pipeline SIMCE.

Las clases encapsulan pasos que poseen una responsabilidad clara y una interfaz común.
El notebook F3 orquesta y documenta; la implementación reutilizable vive aquí.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
import pandas as pd

from .transformacion import (
    convertir_tipos, limpiar_textos, agregar_categorias,
    agregar_geografia, clasificar_efectividad, construir_dataset_final,
)


class Transformador(ABC):
    """Contrato común para transformaciones del pipeline."""

    @property
    def nombre(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def transformar(self, df: pd.DataFrame) -> pd.DataFrame:
        """Devuelve una copia transformada del DataFrame."""
        raise NotImplementedError


class TransformadorTipos(Transformador):
    def transformar(self, df: pd.DataFrame) -> pd.DataFrame:
        return convertir_tipos(df)


class TransformadorTextos(Transformador):
    def transformar(self, df: pd.DataFrame) -> pd.DataFrame:
        return limpiar_textos(df)


class TransformadorCategorias(Transformador):
    def transformar(self, df: pd.DataFrame) -> pd.DataFrame:
        return agregar_categorias(df)


class TransformadorGeografia(Transformador):
    """Encapsula la dimensión geográfica necesaria para el JOIN validado."""

    def __init__(self, dim_geografia: pd.DataFrame):
        self._dim_geografia = dim_geografia.copy()

    @property
    def comunas_dimension(self) -> int:
        return len(self._dim_geografia)

    def transformar(self, df: pd.DataFrame) -> pd.DataFrame:
        return agregar_geografia(df, self._dim_geografia)


class TransformadorEfectividad(Transformador):
    def transformar(self, df: pd.DataFrame) -> pd.DataFrame:
        return clasificar_efectividad(df)


class PipelineSIMCE:
    """Compone transformadores con bajo acoplamiento mediante polimorfismo."""

    def __init__(self, pasos: list[Transformador]):
        if not pasos:
            raise ValueError("El pipeline requiere al menos un transformador.")
        self._pasos = tuple(pasos)
        self._registro: list[dict] = []

    @property
    def pasos(self) -> tuple[str, ...]:
        return tuple(p.nombre for p in self._pasos)

    @property
    def registro(self) -> tuple[dict, ...]:
        return tuple(dict(r) for r in self._registro)

    def ejecutar(self, df: pd.DataFrame) -> pd.DataFrame:
        actual = df.copy()
        self._registro = []
        for paso in self._pasos:  # polimorfismo: no pregunta el tipo concreto
            antes = len(actual)
            actual = paso.transformar(actual)
            self._registro.append({
                "paso": paso.nombre,
                "filas_entrada": antes,
                "filas_salida": len(actual),
                "columnas_salida": actual.shape[1],
            })
        return actual

    def construir_producto_final(self, df_transformado: pd.DataFrame) -> pd.DataFrame:
        return construir_dataset_final(df_transformado)