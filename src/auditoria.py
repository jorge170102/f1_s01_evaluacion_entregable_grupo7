"""Auditoría de la regla de efectividad y análisis de materialidad."""

import pandas as pd

def construir_auditoria(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Construye auditoría detallada y resúmenes antes de filtrar."""

    total = len(df)

    efectiva = df["efectividad"].eq("Efectiva")
    no_efectiva = ~efectiva
    con_puntaje = df["prom_mate4b_rbd"].notna()
    no_efectiva_con_puntaje = no_efectiva & con_puntaje

    # --------------------------------------------------------
    # Promedios para análisis de materialidad
    # --------------------------------------------------------

    promedio_efectivos = df.loc[
        efectiva,
        "prom_mate4b_rbd",
    ].mean()

    promedio_todos_con_puntaje = df.loc[
        con_puntaje,
        "prom_mate4b_rbd",
    ].mean()

    diferencia_promedio = (
        promedio_todos_con_puntaje - promedio_efectivos
        if pd.notna(promedio_efectivos)
        and pd.notna(promedio_todos_con_puntaje)
        else pd.NA
    )

    # --------------------------------------------------------
    # Resumen general
    # --------------------------------------------------------

    resumen = pd.DataFrame({
        "indicador": [
            "Registros originales",
            "Registros efectivos",
            "Registros no efectivos",
            "Registros con puntaje",
            "No efectivos con puntaje",
            "Alumnos asociados al bruto",
            "Alumnos asociados a no efectivos",
            "Promedio puntaje - efectivos",
            "Promedio puntaje - todos con puntaje",
            "Diferencia de promedio (puntos)",
        ],
        "valor": [
            total,
            int(efectiva.sum()),
            int(no_efectiva.sum()),
            int(con_puntaje.sum()),
            int(no_efectiva_con_puntaje.sum()),

            float(
                df["nalu_mate4b_rbd"]
                .fillna(0)
                .sum()
            ),

            float(
                df.loc[
                    no_efectiva,
                    "nalu_mate4b_rbd",
                ]
                .fillna(0)
                .sum()
            ),

            (
                round(
                    float(promedio_efectivos),
                    4,
                )
                if pd.notna(promedio_efectivos)
                else pd.NA
            ),

            (
                round(
                    float(promedio_todos_con_puntaje),
                    4,
                )
                if pd.notna(promedio_todos_con_puntaje)
                else pd.NA
            ),

            (
                round(
                    float(diferencia_promedio),
                    4,
                )
                if pd.notna(diferencia_promedio)
                else pd.NA
            ),
        ],
    })

    # --------------------------------------------------------
    # Auditoría de registros excluidos
    # --------------------------------------------------------

    columnas_auditoria = [
        "rbd",
        "dvrbd",
        "nom_rbd",

        "cod_reg_rbd",
        "region",

        "cod_pro_rbd",
        "provincia",

        "cod_com_rbd",
        "comuna",

        "nalu_mate4b_rbd",
        "prom_mate4b_rbd",

        "marca_mate4b_rbd",
        "obs_puntaje",
        "motivo_exclusion",

        "noaplica",
        "codigo_bbdd",
        "fecha_bbdd",
        "grado",
        "agno",
    ]

    auditoria = df.loc[
        no_efectiva,
        columnas_auditoria,
    ].copy()

    # --------------------------------------------------------
    # Identificación de marca 2 con puntaje
    # --------------------------------------------------------
    # Se conserva solo como información de auditoría.
    # No genera warning.
    # --------------------------------------------------------

    auditoria["marca_2_con_puntaje"] = (
        auditoria["marca_mate4b_rbd"].eq(2)
        & auditoria["prom_mate4b_rbd"].notna()
    )

    # --------------------------------------------------------
    # Resumen por marca
    # --------------------------------------------------------

    resumen_marcas = (
        df.groupby(
            [
                "marca_mate4b_rbd",
                "obs_puntaje",
            ],
            dropna=False,
        )
        .agg(
            registros=(
                "rbd",
                "size",
            ),
            alumnos=(
                "nalu_mate4b_rbd",
                "sum",
            ),
            con_puntaje=(
                "prom_mate4b_rbd",
                "count",
            ),
        )
        .reset_index()
        .sort_values(
            "registros",
            ascending=False,
        )
    )

    return (
        auditoria,
        resumen,
        resumen_marcas,
    )
