"""Diagnóstico descriptivo previo a las transformaciones."""

import pandas as pd
from IPython.display import display

def diagnosticar_inicial(df: pd.DataFrame) -> dict:
    """Genera evidencia descriptiva sin modificar el DataFrame recibido."""
    trabajo = df.copy()

    resumen = pd.DataFrame({
        "tipo_original": trabajo.dtypes.astype(str),
        "nulos": trabajo.isna().sum(),
        "unicos": trabajo.nunique(dropna=True),
    }).sort_index()

    duplicados_fila = int(trabajo.duplicated().sum())
    duplicados_rbd = int(trabajo["rbd"].duplicated().sum())

    numericas_interes = pd.DataFrame({
        "nalu_mate4b_rbd": pd.to_numeric(
            trabajo["nalu_mate4b_rbd"], errors="coerce"
        ),
        "prom_mate4b_rbd": pd.to_numeric(
            trabajo["prom_mate4b_rbd"], errors="coerce"
        ),
    })

    atipicos = {}
    for col in numericas_interes.columns:
        serie = numericas_interes[col].dropna()
        if serie.empty:
            atipicos[col] = 0
            continue
        q1 = serie.quantile(0.25)
        q3 = serie.quantile(0.75)
        iqr = q3 - q1
        limite_inf = q1 - 1.5 * iqr
        limite_sup = q3 + 1.5 * iqr
        atipicos[col] = int(((serie < limite_inf) | (serie > limite_sup)).sum())

    print("=" * 72)
    print("DIAGNÓSTICO INICIAL")
    print("=" * 72)
    print(f"Dimensiones: {trabajo.shape[0]:,} filas x {trabajo.shape[1]} columnas")
    print(f"Filas duplicadas completas: {duplicados_fila:,}")
    print(f"RBD repetidos: {duplicados_rbd:,}")
    print("Potenciales atípicos IQR (solo diagnóstico):", atipicos)

    display(resumen)
    display(numericas_interes.describe())

    return {
        "resumen_columnas": resumen,
        "duplicados_fila": duplicados_fila,
        "duplicados_rbd": duplicados_rbd,
        "atipicos": atipicos,
    }
