"""Configuración, catálogos y esquema compartido del pipeline F2."""

from pathlib import Path
from datetime import datetime

try:
    from zoneinfo import ZoneInfo
except ImportError:
    ZoneInfo = None

def encontrar_raw_dir() -> Path:
    """Localiza data/raw usando rutas relativas compatibles con raíz o carpeta F2."""
    candidatos = [
        Path.cwd() / "data" / "raw",
        Path.cwd().parent / "data" / "raw",
        Path.cwd() / "F2" / "data" / "raw",
        Path.cwd().parent / "F2" / "data" / "raw",
    ]
    for ruta in candidatos:
        if ruta.exists():
            return ruta.resolve()
    raise FileNotFoundError(
        "No se encontró data/raw. "
        f"Directorio de ejecución: {Path.cwd()}"
    )

def buscar_simce(raw_dir: Path) -> Path:
    """Busca el CSV SIMCE 4° básico 2025 dentro de data/raw."""
    patrones = [
        "simce4b2025_rbd_final.csv",
        "*simce4b2025*.csv",
        "*simce*2025*.csv",
        "*simce*.csv",
    ]
    for patron in patrones:
        archivos = sorted(raw_dir.glob(patron))
        if archivos:
            return archivos[0]
    raise FileNotFoundError(f"No se encontró un CSV SIMCE en {raw_dir}")

def obtener_fecha_ejecucion() -> datetime:
    """Obtiene fecha/hora de ejecución intentando usar America/Santiago."""
    if ZoneInfo is not None:
        try:
            return datetime.now(ZoneInfo("America/Santiago"))
        except Exception:
            pass
    return datetime.now().astimezone()

DEPENDENCIA_1 = {
    1: "Municipal Corporación",
    2: "Municipal DAEM",
    3: "Particular subvencionado",
    4: "Particular pagado",
    5: "Corporación de administración delegada",
    6: "Servicio Local de Educación",
}

DEPENDENCIA_2 = {
    1: "Municipal",
    2: "Particular subvencionado",
    3: "Particular pagado",
    4: "Servicio Local de Educación",
}

GSE = {
    1: "Bajo",
    2: "Medio bajo",
    3: "Medio",
    4: "Medio alto",
    5: "Alto",
}

RURALIDAD = {
    1: "Urbano",
    2: "Rural",
}

OBS_PUNTAJE = {
    1: "No es posible reportar resultados, porque la cantidad de estudiantes evaluados es insuficiente. (6 o menos)",
    2: "Por causas ajenas a la Agencia, los resultados no son representativos del desempeño de los estudiantes",
    3: "Por causas ajenas al establecimiento, los resultados no son representativos del desempeño de los estudiantes",
    4: "La aplicación de la prueba extendida no permite evaluar esta asignatura.",
}

DIM_GEOGRAFIA_B64 = """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"""

COLUMNAS_SIMCE = [
    # Identificación
    "rbd", "dvrbd", "nom_rbd",

    # Geografía: solo claves; los nombres finales vendrán de DimGeografia
    "cod_reg_rbd", "cod_pro_rbd", "cod_com_rbd",

    # Departamento provincial
    "cod_deprov_rbd", "nom_deprov_rbd",

    # Clasificaciones
    "cod_depe1", "cod_depe2", "cod_grupo", "cod_rural_rbd",

    # Matemática
    "nalu_mate4b_rbd", "prom_mate4b_rbd",

    # Control y efectividad
    "marca_mate4b_rbd", "noaplica",
    "codigo_bbdd", "fecha_bbdd", "grado", "agno",
]

COLUMNAS_NUMERICAS = [
    "rbd", "dvrbd",
    "cod_reg_rbd", "cod_pro_rbd", "cod_com_rbd", "cod_deprov_rbd",
    "cod_depe1", "cod_depe2", "cod_grupo", "cod_rural_rbd",
    "nalu_mate4b_rbd", "prom_mate4b_rbd",
    "marca_mate4b_rbd", "noaplica", "agno",
]

COLUMNAS_TEXTO = [
    "nom_rbd", "nom_deprov_rbd", "codigo_bbdd", "grado",
]

CLAVES_GEO = ["cod_reg_rbd", "cod_pro_rbd", "cod_com_rbd"]

RENOMBRE_FINAL = {
    "dvrbd": "dv_rbd",
    "nom_rbd": "nombre_establecimiento",
    "nom_deprov_rbd": "deprov",
    "nalu_mate4b_rbd": "n_alumnos",
    "prom_mate4b_rbd": "puntaje_promedio",
    "noaplica": "no_aplica",
    "agno": "anio",
}

COLUMNAS_FINALES = [
    "rbd", "dv_rbd", "nombre_establecimiento", "asignatura",

    "cod_reg_rbd", "region",
    "cod_pro_rbd", "provincia",
    "cod_com_rbd", "comuna",
    "deprov",

    "pais",
    "ubicacion_region",
    "ubicacion_provincia",
    "ubicacion_comuna",
    "Zona", "Macrozona", "Orden",

    "dependencia_6_cat",
    "dependencia_4_cat",
    "grupo_socioeconomico",
    "ruralidad",

    "n_alumnos",
    "puntaje_promedio",

    "efectividad",
    "no_aplica",
    "codigo_bbdd",
    "fecha_bbdd",
    "grado",
    "anio",
]

