"""Validaciones de catálogos e integridad del producto F2."""

import pandas as pd

from .configuracion import DEPENDENCIA_1, DEPENDENCIA_2, GSE, RURALIDAD, OBS_PUNTAJE

def validar_codigos_catalogo(df: pd.DataFrame) -> None:
    """Detiene el proceso si aparecen códigos categóricos desconocidos."""
    controles = [
        ("cod_depe1", DEPENDENCIA_1),
        ("cod_depe2", DEPENDENCIA_2),
        ("cod_grupo", GSE),
        ("cod_rural_rbd", RURALIDAD),
    ]
    for columna, catalogo in controles:
        desconocidos = sorted(
            set(df[columna].dropna().astype(int).tolist()) - set(catalogo.keys())
        )
        if desconocidos:
            raise ValueError(
                f"Códigos sin catálogo en {columna}: {desconocidos}"
            )

    marcas_desconocidas = sorted(
        set(df["marca_mate4b_rbd"].dropna().astype(int).tolist())
        - set(OBS_PUNTAJE.keys())
    )
    if marcas_desconocidas:
        raise ValueError(
            "Aparecieron marcas de puntaje no documentadas: "
            f"{marcas_desconocidas}"
        )

def validar_dataset_final(
    df_final: pd.DataFrame,
    df_transformado: pd.DataFrame,
    auditoria: pd.DataFrame,
    cobertura: pd.DataFrame,
) -> dict[str, bool]:
    """Valida integridad, consistencia y reconciliación del resultado de F2."""
    validaciones = {
        "Dataset final no vacío":
            not df_final.empty,

        "Asignatura = Matematica":
            bool(df_final["asignatura"].eq("Matematica").all()),

        "Efectividad = Efectiva":
            bool(df_final["efectividad"].eq("Efectiva").all()),

        "n_alumnos > 0":
            bool(df_final["n_alumnos"].gt(0).all()),

        "RBD no nulo":
            bool(df_final["rbd"].notna().all()),

        "RBD único":
            bool(df_final["rbd"].is_unique),

        "Puntaje no nulo":
            bool(df_final["puntaje_promedio"].notna().all()),

        "Geografía completa":
            bool(
                df_final[
                    [
                        "cod_reg_rbd", "region",
                        "cod_pro_rbd", "provincia",
                        "cod_com_rbd", "comuna",
                        "Zona", "Macrozona", "Orden",
                    ]
                ].notna().all().all()
            ),

        "fecha_bbdd válida":
            bool(df_final["fecha_bbdd"].notna().all()),

        "Sin columnas duplicadas":
            bool(not df_final.columns.duplicated().any()),

        "Reconciliación bruto = final + auditoría":
            len(df_transformado) == len(df_final) + len(auditoria),

        "Cobertura regional reconcilia con bruto":
            int(cobertura["registros_originales"].sum())
            == len(df_transformado),

        "Cobertura regional reconcilia con final":
            int(cobertura["registros_efectivos"].sum())
            == len(df_final),

        "Sin columnas pct eliminadas":
            not any(
                col in df_final.columns
                for col in [
                    "pct_insuficiente",
                    "pct_elemental",
                    "pct_adecuado",
                ]
            ),
    }

    fallidas = [
        nombre
        for nombre, cumple in validaciones.items()
        if not cumple
    ]

    if fallidas:
        raise AssertionError(
            "Fallaron las validaciones: " + "; ".join(fallidas)
        )

    return validaciones
