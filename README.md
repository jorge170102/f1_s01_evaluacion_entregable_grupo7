# Caracterización e Inequidad en los Resultados Académicos del SIMCE 4º Básico en Chile

**Grupo:** Grupo 7

## Integrantes

- Felipe Palma Barrientos
- Vicente Aguila Rojas
- Cristian Grandon Grandon
- Jorge Gutierrez Jaramillo

## Propósito del proyecto

El proyecto prepara un flujo reproducible para analizar las diferencias territoriales en los puntajes promedio de Matemática del SIMCE 2025 de 4º Básico. La unidad de análisis es el establecimiento educacional identificado por RBD.

Las fases F1 y F2 definen la problemática, documentan la fuente y construyen una base comparable y validada. Las comparaciones descriptivas, análisis estadísticos y conclusiones territoriales corresponden a fases posteriores del proyecto.

## Datos

- **Dataset:** Resultados prueba SIMCE 4º Básico 2025 por Establecimiento.
- **Fuente:** Agencia de Calidad de la Educación.
- **Portal:** Bases de datos públicas de la Agencia de Calidad de la Educación.
- **Enlace:** https://informacionestadistica.agenciaeducacion.cl/#/bases
- **Unidad de observación:** Un establecimiento educacional (RBD).
- **Base bruta:** 7.143 filas × 42 columnas.
- **Salida F2:** 6.524 establecimientos × 30 columnas.

## Estructura del repositorio

```text
f1_s01_evaluacion_entregable_grupo7/
│
├── .gitignore
├── README.md
├── requirements.txt
├── informe_dataset_simce.md
│
├── F1/
│   ├── F1_Definicion.ipynb
│   ├── Validar_DataSet simce.ipynb
│   └── informe_dataset_simce.md
│
├── F2/
│   └── F2_Preprocesamiento.ipynb
│
├── F3/
├── F4/
│
├── data/
│   ├── raw/
│   │   └── simce4b2025_rbd_final.csv
│   └── processed/
│       ├── simce4b2025_matematica_efectiva_AAAAMMDDHHMM.csv
│       ├── auditoria_filtro_AAAAMMDDHHMM.csv
│       └── cobertura_regional_AAAAMMDDHHMM.csv
│
├── docs/
│   ├── diccionario_variables.csv
│   ├── evaluacion_criterios_dataset.csv
│   ├── metadatos_fase1.json
│   └── vinculacion_mapa_conceptual.csv
│
├── Minutas/
└── src/
```

La estructura separa los datos originales de los resultados procesados y mantiene organizadas las fases, la documentación y los archivos de apoyo. Esto facilita el trabajo colaborativo y la trazabilidad del proyecto.

`data/raw/` conserva la fuente original sin modificaciones, `data/processed/` recibe los productos generados por F2 y `docs/` concentra los artefactos de documentación y validación. `src/` queda disponible para componentes reutilizables de fases posteriores.

## Entorno y dependencias

El proyecto se ejecuta con **Python 3.14.7**.
Las dependencias oficiales se encuentran fijadas en `requirements.txt`.

```text
ipykernel==7.3.0
jupyterlab==4.6.3
matplotlib==3.11.1
notebook==7.6.2
numpy==2.5.2
pandas==3.0.5
seaborn==0.13.2
```

La semilla definida para reproducibilidad es `42`.

## Clonar repositorio

## git clone https://github.com/jorge170102/f1_s01_evaluacion_entregable_grupo7.git

## Reproducción del proyecto

### Windows (PowerShell)

Desde la raíz del repositorio:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m ipykernel install --sys-prefix --name simce-grupo7 --display-name "SIMCE Grupo 7 (.venv)"
.\.venv\Scripts\python.exe -m jupyter lab
```

### macOS / Linux

Desde la raíz del repositorio:

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip check
python -m ipykernel install --sys-prefix --name simce-grupo7 --display-name "SIMCE Grupo 7 (.venv)"
python -m jupyter lab
```

Una vez iniciado Jupyter, seleccionar el kernel `SIMCE Grupo 7 (.venv)` y ejecutar, desde un kernel reiniciado:

1. `F1/F1_Definicion.ipynb`
2. `F2/F2_Preprocesamiento.ipynb`

## Productos de la Fase 2

`F2/F2_Preprocesamiento.ipynb` genera tres productos principales:

- `data/processed/simce4b2025_matematica_efectiva_AAAAMMDDHHMM.csv`: dataset principal procesado, con 6.524 establecimientos y 30 columnas.
- `data/processed/auditoria_filtro_AAAAMMDDHHMM.csv`: contiene los 619 registros excluidos junto con la información necesaria para revisar el motivo de exclusión.
- `data/processed/cobertura_regional_AAAAMMDDHHMM.csv`: resume por región los registros originales, efectivos y no efectivos, además de los alumnos asociados antes y después del filtrado.

La marca `AAAAMMDDHHMM` corresponde a la fecha y hora de cada ejecución.

Después de exportar el dataset principal, F2 vuelve a leer el CSV y compara su contenido con el DataFrame en memoria mediante `pd.testing.assert_frame_equal`.

## Decisiones de preprocesamiento

Los puntajes SIMCE se mantienen en su escala original porque son directamente interpretables para las comparaciones territoriales planteadas.

En F2 no se aplica normalización ni escalamiento porque en esta etapa no existe un algoritmo que requiera trabajar con variables numéricas en una escala común. Esta decisión evita aplicar transformaciones antes de definir las técnicas de análisis posteriores.

No se imputan RBD, información geográfica ni puntajes faltantes, porque hacerlo podría incorporar identidad, ubicación o rendimiento que no existe en la fuente original.

Los posibles valores atípicos se utilizan como diagnóstico y no se eliminan automáticamente, ya que un establecimiento con un resultado extremo o una cantidad elevada de estudiantes puede representar una observación válida.

La regla de efectividad conserva establecimientos con alumnos evaluados mayores a cero y sin observaciones asociadas al puntaje. Los registros que no cumplen la regla se mantienen en la auditoría.

Existen 55 registros no efectivos que conservan puntaje, incluyendo los casos identificados mediante `marca_2_con_puntaje`.

## Validación técnica

F2 comprueba, entre otros elementos:

- que el dataset final no esté vacío;
- asignatura y efectividad esperadas;
- alumnos evaluados mayores a cero;
- presencia y unicidad del RBD;
- presencia del puntaje promedio;
- información geográfica completa;
- fecha de la base válida;
- ausencia de columnas duplicadas;
- reconciliación entre registros originales, efectivos y auditados;
- reconciliación de la cobertura regional;
- ausencia en el producto final de variables retiradas del alcance.

Además, el notebook incluye pruebas controladas para:

- un caso normal;
- un caso límite sin alumnos evaluados;
- un registro con observación;
- un registro con marca 2 y puntaje disponible;
- un código desconocido que debe generar una excepción.

## Alcance y limitaciones

F1 y F2 preparan una base reproducible, consistente y documentada para las fases posteriores.

Estas fases no establecen causalidad entre territorio y rendimiento y no determinan por sí solas dónde asignar recursos educativos.

Las comparaciones territoriales, pruebas de significancia, visualizaciones y conclusiones analíticas corresponden a fases posteriores.

Los registros con observaciones asociadas a `marca_mate4b_rbd` permanecen identificados en la auditoría para conservar la trazabilidad y permitir su revisión.

## Trazabilidad

El repositorio mantiene historial Git, notebooks ejecutables, documentación en `docs/`, minutas de trabajo, archivos de auditoría y productos procesados.

La relación entre el mapa conceptual, F1, F2 y las fases posteriores se registra en `docs/vinculacion_mapa_conceptual.csv`.
