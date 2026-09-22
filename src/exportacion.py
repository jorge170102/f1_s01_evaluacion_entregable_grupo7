"""Exportación y verificación de los productos generados por F2."""

from pathlib import Path
import pandas as pd


def exportar_resultados(
    df_final: pd.DataFrame,
    auditoria: pd.DataFrame,
    cobertura: pd.DataFrame,
    output_file: Path,
    auditoria_file: Path,
    cobertura_file: Path,
) -> None:
    """Exporta los tres productos de F2 y verifica el archivo principal."""
    df_final.to_csv(output_file, index=False, encoding="utf-8-sig", date_format="%Y-%m-%d")
    auditoria.to_csv(auditoria_file, index=False, encoding="utf-8-sig", date_format="%Y-%m-%d")
    cobertura.to_csv(cobertura_file, index=False, encoding="utf-8-sig")

    releido = pd.read_csv(output_file, encoding="utf-8-sig")
    releido["fecha_bbdd"] = pd.to_datetime(releido["fecha_bbdd"], format="%Y-%m-%d", errors="raise")
    releido["no_aplica"] = (pd.to_numeric(releido["no_aplica"], errors="coerce").astype("Int64").astype("string"))
    pd.testing.assert_frame_equal(releido, df_final.reset_index(drop=True), check_dtype=False)
