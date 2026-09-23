"""Algoritmos, recursividad y medición reproducible usados en F3."""
from __future__ import annotations

from time import perf_counter
import tracemalloc
import pandas as pd

from .configuracion import CLAVES_GEO


def aplanar_recursivo(obj, prefijo="") -> dict:
    """Aplana diccionarios/listas anidados mediante recursividad.

    Caso base: valor escalar. Caso recursivo: dict/list/tuple.
    Complejidad temporal O(n); pila O(h), con h = profundidad máxima.
    """
    salida = {}
    if isinstance(obj, dict):
        for clave, valor in obj.items():
            nuevo = f"{prefijo}.{clave}" if prefijo else str(clave)
            salida.update(aplanar_recursivo(valor, nuevo))
    elif isinstance(obj, (list, tuple)):
        for i, valor in enumerate(obj):
            nuevo = f"{prefijo}[{i}]"
            salida.update(aplanar_recursivo(valor, nuevo))
    else:
        salida[prefijo] = obj
    return salida


def enriquecer_geografia_merge(df: pd.DataFrame, dim: pd.DataFrame, validar=True) -> pd.DataFrame:
    """JOIN vectorizado; opcionalmente verifica cardinalidad many-to-one."""
    return df.merge(
        dim,
        how="left",
        on=CLAVES_GEO,
        validate="many_to_one" if validar else None,
    )


def enriquecer_geografia_diccionario(df: pd.DataFrame, dim: pd.DataFrame, validar=True) -> pd.DataFrame:
    """Alternativa basada en diccionario de clave geográfica compuesta."""
    columnas_dim = [c for c in dim.columns if c not in CLAVES_GEO]
    # Duplicados invalidan el supuesto many-to-one también en esta implementación.
    if validar and dim.duplicated(CLAVES_GEO).any():
        raise ValueError("La dimensión geográfica contiene claves duplicadas.")
    lookup = {
        tuple(fila[c] for c in CLAVES_GEO): tuple(fila[c] for c in columnas_dim)
        for _, fila in dim.iterrows()
    }
    out = df.copy()
    claves = list(zip(*(out[c] for c in CLAVES_GEO)))
    valores = [lookup.get(tuple(k), (pd.NA,) * len(columnas_dim)) for k in claves]
    enriquecido = pd.DataFrame(valores, columns=columnas_dim, index=out.index)
    return pd.concat([out, enriquecido], axis=1)


def medir(funcion, *args, repeticiones=7, **kwargs) -> dict:
    """Mide tiempo y memoria pico; conserva el último resultado para validarlo."""
    tiempos, memorias, resultado = [], [], None
    for _ in range(repeticiones):
        tracemalloc.start()
        inicio = perf_counter()
        resultado = funcion(*args, **kwargs)
        tiempos.append(perf_counter() - inicio)
        _, pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        memorias.append(pico / 1024**2)
    return {
        "tiempo_promedio_s": sum(tiempos) / len(tiempos),
        "tiempo_min_s": min(tiempos),
        "memoria_pico_promedio_mb": sum(memorias) / len(memorias),
        "resultado": resultado,
    }


def validar_geografia_recursiva(estructura, ruta="raiz") -> list[str]:
    """Recorre recursivamente una jerarquía territorial y reporta hojas inválidas.

    Se usa cuando la jerarquía Región -> Provincia -> Comuna se representa como
    diccionarios anidados. La profundidad queda desacoplada del algoritmo.
    """
    errores = []
    if isinstance(estructura, dict):
        if not estructura:
            errores.append(f"{ruta}: nodo vacío")
            return errores
        for clave, valor in estructura.items():
            errores.extend(validar_geografia_recursiva(valor, f"{ruta}/{clave}"))
    elif isinstance(estructura, (list, tuple, set)):
        if not estructura:
            errores.append(f"{ruta}: colección vacía")
        for i, valor in enumerate(estructura):
            errores.extend(validar_geografia_recursiva(valor, f"{ruta}[{i}]"))
    elif estructura is None or (isinstance(estructura, str) and not estructura.strip()):
        errores.append(f"{ruta}: valor vacío")
    return errores


def construir_jerarquia_geografica(dim: pd.DataFrame) -> dict:
    """Convierte DimGeografia en Región -> Provincia -> lista de comunas."""
    jerarquia = {}
    for region, bloque_region in dim.groupby("region", sort=True):
        jerarquia[region] = {}
        for provincia, bloque_prov in bloque_region.groupby("provincia", sort=True):
            jerarquia[region][provincia] = sorted(bloque_prov["comuna"].dropna().tolist())
    return jerarquia