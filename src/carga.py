"""Funciones de carga de datos y construcción de la dimensión geográfica."""

from pathlib import Path
from io import StringIO
import base64
import zlib
import pandas as pd

from .configuracion import DIM_GEOGRAFIA_B64

def construir_dim_geografia() -> pd.DataFrame:
    """Reconstruye y valida DimGeografia embebida sin archivos externos."""
    datos = zlib.decompress(
        base64.b64decode(DIM_GEOGRAFIA_B64.encode("ascii"))
    ).decode("utf-8")

    dim = pd.read_csv(StringIO(datos), sep=";")

    for col in ["region", "provincia", "comuna", "Zona", "Macrozona"]:
        dim[col] = (
            dim[col]
            .astype("string")
            .str.replace(r"\s+", " ", regex=True)
            .str.strip()
        )

    for col in ["codigo_region", "codigo_provincia", "codigo_comuna", "Orden"]:
        dim[col] = pd.to_numeric(dim[col], errors="raise").astype("Int64")

    dim["pais"] = "Chile"
    dim["ubicacion_region"] = dim["region"] + ", Chile"
    dim["ubicacion_provincia"] = (
        dim["provincia"] + ", " + dim["region"] + ", Chile"
    )
    dim["ubicacion_comuna"] = (
        dim["comuna"] + ", " + dim["provincia"] + ", " + dim["region"] + ", Chile"
    )

    # Renombrar claves para unir directamente con SIMCE y conservar esos códigos en la salida.
    dim = dim.rename(columns={
        "codigo_region": "cod_reg_rbd",
        "codigo_provincia": "cod_pro_rbd",
        "codigo_comuna": "cod_com_rbd",
    })

    claves = ["cod_reg_rbd", "cod_pro_rbd", "cod_com_rbd"]

    assert len(dim) == 346, (
        f"DimGeografia debería contener 346 comunas y contiene {len(dim)}."
    )
    assert not dim.duplicated(claves).any(), (
        "DimGeografia contiene claves geográficas duplicadas."
    )
    assert dim[claves].notna().all().all(), (
        "DimGeografia contiene claves geográficas nulas."
    )

    return dim.copy()

def cargar_simce(archivo: Path, columnas: list[str]) -> pd.DataFrame:
    """Carga de manera selectiva la base SIMCE sin alterar el archivo bruto."""
    cabecera = pd.read_csv(
        archivo,
        sep=";",
        encoding="cp1252",
        nrows=0,
    )
    faltantes = sorted(set(columnas) - set(cabecera.columns))
    if faltantes:
        raise ValueError(f"Faltan columnas requeridas en la fuente: {faltantes}")

    return pd.read_csv(
        archivo,
        sep=";",
        encoding="cp1252",
        usecols=columnas,
        low_memory=False,
    ).copy()
