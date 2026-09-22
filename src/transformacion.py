"""Limpieza y transformaciones del dataset SIMCE."""

import pandas as pd
from IPython.display import display

from .configuracion import (
    COLUMNAS_NUMERICAS, COLUMNAS_TEXTO, CLAVES_GEO,
    DEPENDENCIA_1, DEPENDENCIA_2, GSE, RURALIDAD, OBS_PUNTAJE,
    RENOMBRE_FINAL, COLUMNAS_FINALES,
)
from .validacion import validar_codigos_catalogo

def convertir_tipos(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte numéricos y fecha; falla ante valores no convertibles no nulos."""
    out = df.copy()

    for col in COLUMNAS_NUMERICAS:
        convertida = pd.to_numeric(out[col], errors="coerce")
        invalidos = out[col].notna() & convertida.isna()
        if invalidos.any():
            ejemplos = out.loc[invalidos, col].astype(str).head(5).tolist()
            raise ValueError(
                f"Valores no numéricos en {col}: {int(invalidos.sum())}. "
                f"Ejemplos: {ejemplos}"
            )
        out[col] = convertida

    fecha_num = pd.to_numeric(out["fecha_bbdd"], errors="coerce").astype("Int64")
    fecha_texto = fecha_num.astype("string")
    out["fecha_bbdd"] = pd.to_datetime(
        fecha_texto,
        format="%Y%m%d",
        errors="coerce",
    )

    if out["fecha_bbdd"].isna().any():
        raise ValueError(
            f"fecha_bbdd contiene {int(out['fecha_bbdd'].isna().sum())} "
            "valores inválidos o vacíos."
        )

    return out

def limpiar_textos(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza campos de texto sin modificar semánticamente su contenido."""
    out = df.copy()
    for col in COLUMNAS_TEXTO:
        out[col] = (
            out[col]
            .astype("string")
            .str.replace(r"[\x00-\x1F\x7F]", "", regex=True)
            .str.replace(r"\s+", " ", regex=True)
            .str.strip()
            .replace("", pd.NA)
        )
    return out

def agregar_categorias(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega etiquetas categóricas conservando los códigos originales."""
    validar_codigos_catalogo(df)
    out = df.copy()
    out["dependencia_6_cat"] = out["cod_depe1"].map(DEPENDENCIA_1)
    out["dependencia_4_cat"] = out["cod_depe2"].map(DEPENDENCIA_2)
    out["grupo_socioeconomico"] = out["cod_grupo"].map(GSE)
    out["ruralidad"] = out["cod_rural_rbd"].map(RURALIDAD)
    return out

def agregar_geografia(
    df: pd.DataFrame,
    dim_geografia: pd.DataFrame,
) -> pd.DataFrame:
    """Enriquece el dataset mediante un JOIN many-to-one validado."""
    out = df.copy()

    for col in CLAVES_GEO:
        out[col] = pd.to_numeric(out[col], errors="coerce").astype("Int64")

    filas_antes = len(out)
    out = out.merge(
        dim_geografia,
        how="left",
        on=CLAVES_GEO,
        validate="many_to_one",
    )

    if len(out) != filas_antes:
        raise AssertionError(
            "El JOIN geográfico modificó la cantidad de registros."
        )

    sin_geo = out["comuna"].isna()
    if sin_geo.any():
        claves = (
            out.loc[sin_geo, CLAVES_GEO]
            .drop_duplicates()
            .sort_values(CLAVES_GEO)
        )
        display(claves)
        raise ValueError(
            f"Hay {int(sin_geo.sum())} registros sin coincidencia en DimGeografia."
        )

    return out

def clasificar_efectividad(df: pd.DataFrame) -> pd.DataFrame:
    """Clasifica Efectiva/No Efectiva y explicita el motivo de exclusión."""
    out = df.copy()

    out["obs_puntaje"] = out["marca_mate4b_rbd"].map(OBS_PUNTAJE)

    tiene_alumnos = out["nalu_mate4b_rbd"].fillna(0).gt(0)
    sin_observacion = out["obs_puntaje"].isna()

    out["efectividad"] = "No Efectiva"
    out.loc[tiene_alumnos & sin_observacion, "efectividad"] = "Efectiva"

    out["motivo_exclusion"] = "Registro efectivo"

    sin_alumnos = ~tiene_alumnos
    con_observacion = ~sin_observacion

    out.loc[
        sin_alumnos & ~con_observacion,
        "motivo_exclusion",
    ] = "Sin alumnos evaluados"

    out.loc[
        ~sin_alumnos & con_observacion,
        "motivo_exclusion",
    ] = "Observación de puntaje"

    out.loc[
        sin_alumnos & con_observacion,
        "motivo_exclusion",
    ] = "Sin alumnos y con observación de puntaje"

    return out

def construir_dataset_final(df: pd.DataFrame) -> pd.DataFrame:
    """Filtra efectivos, renombra y selecciona exclusivamente el esquema final."""
    out = df.loc[df["efectividad"].eq("Efectiva")].copy()
    out = out.rename(columns=RENOMBRE_FINAL)

    out["asignatura"] = "Matematica"

    # Tipos finales
    for col in [
        "rbd", "dv_rbd",
        "cod_reg_rbd", "cod_pro_rbd", "cod_com_rbd",
        "n_alumnos", "anio", "Orden",
    ]:
        out[col] = pd.to_numeric(out[col], errors="coerce").astype("Int64")

    out["puntaje_promedio"] = pd.to_numeric(
        out["puntaje_promedio"],
        errors="coerce",
    )

    out["no_aplica"] = (
        pd.to_numeric(out["no_aplica"], errors="coerce")
        .astype("Int64")
        .astype("string")
    )

    return out[COLUMNAS_FINALES].copy()

def construir_cobertura_regional(df: pd.DataFrame) -> pd.DataFrame:
    """Resume la cobertura antes y después del filtro por región."""
    trabajo = df.copy()
    trabajo["es_efectiva"] = trabajo["efectividad"].eq("Efectiva")
    trabajo["es_no_efectiva"] = ~trabajo["es_efectiva"]
    trabajo["no_efectiva_con_puntaje"] = (
        trabajo["es_no_efectiva"]
        & trabajo["prom_mate4b_rbd"].notna()
    )
    trabajo["alumnos_efectivos"] = (
        trabajo["nalu_mate4b_rbd"].fillna(0)
        * trabajo["es_efectiva"].astype(int)
    )
    trabajo["alumnos_no_efectivos"] = (
        trabajo["nalu_mate4b_rbd"].fillna(0)
        * trabajo["es_no_efectiva"].astype(int)
    )

    cobertura = (
        trabajo.groupby(
            ["cod_reg_rbd", "region", "Zona", "Macrozona", "Orden"],
            dropna=False,
        )
        .agg(
            registros_originales=("rbd", "size"),
            registros_efectivos=("es_efectiva", "sum"),
            registros_no_efectivos=("es_no_efectiva", "sum"),
            no_efectivos_con_puntaje=("no_efectiva_con_puntaje", "sum"),
            alumnos_bruto=("nalu_mate4b_rbd", "sum"),
            alumnos_efectivos=("alumnos_efectivos", "sum"),
            alumnos_no_efectivos=("alumnos_no_efectivos", "sum"),
        )
        .reset_index()
        .sort_values("Orden")
    )

    return cobertura

