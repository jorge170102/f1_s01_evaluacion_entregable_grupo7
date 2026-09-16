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

- **Dataset:** Resultados prueba SIMCE 4º Básico 2025 por establecimiento.
- **Fuente:** Agencia de Calidad de la Educación.
- **Portal:** Bases de datos públicas de la Agencia de Calidad de la Educación.
- **Enlace:** https://informacionestadistica.agenciaeducacion.cl/#/bases
- **Unidad de observación:** establecimiento educacional (RBD).
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
│   └── Fase proyectada
│
├── F4/
│   └── Fase proyectada
│
├── data/
│   ├── raw/
│   │   └── simce4b2025_rbd_final.csv
│   │
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
│
└── src/
```

La estructura separa los datos originales de los resultados procesados y mantiene organizadas las distintas fases del proyecto. Esto facilita localizar los archivos, trabajar de forma colaborativa y mantener la trazabilidad entre la fuente original, el procesamiento realizado y los productos generados.

`data/raw/` conserva el dataset original sin modificaciones, mientras que `data/processed/` almacena los resultados generados por F2. La carpeta `docs/` reúne archivos utilizados para documentar y validar el proyecto, y `src/` queda disponible para componentes reutilizables que puedan incorporarse en fases posteriores.

## Entorno y dependencias

El proyecto fue desarrollado con **Python 3.14.7**. Las dependencias utilizadas se encuentran fijadas en `requirements.txt`.

```text
ipykernel==7.3.0
jupyterlab==4.6.3
matplotlib==3.11.1
notebook==7.6.2
numpy==2.5.2
pandas==3.0.5
seaborn==0.13.2
```

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

Una vez iniciado Jupyter, seleccionar el kernel:

```text
SIMCE Grupo 7 (.venv)
```

Luego, desde un kernel reiniciado, ejecutar los notebooks en el siguiente orden:

1. `F1/F1_Definicion.ipynb`
2. `F2/F2_Preprocesamiento.ipynb`

Este orden permite que primero se realicen las verificaciones y definiciones de F1 y posteriormente se ejecute el pipeline de procesamiento de F2.

## Productos de la Fase 2

`F2/F2_Preprocesamiento.ipynb` genera tres productos principales:

- `data/processed/simce4b2025_matematica_efectiva_AAAAMMDDHHMM.csv`: dataset principal procesado, compuesto por 6.524 establecimientos y 30 columnas.

- `data/processed/auditoria_filtro_AAAAMMDDHHMM.csv`: contiene los registros excluidos del dataset analítico junto con la información necesaria para revisar el motivo de su exclusión.

- `data/processed/cobertura_regional_AAAAMMDDHHMM.csv`: resume por región los registros originales, efectivos y no efectivos, además de los alumnos asociados antes y después del proceso de filtrado.

La marca `AAAAMMDDHHMM` identifica la fecha y hora en que fue realizada cada ejecución.

Después de exportar el dataset principal, el notebook vuelve a leer el archivo generado y compara su contenido con el DataFrame mantenido en memoria. De esta forma se comprueba que la exportación no haya introducido diferencias en los datos procesados.

## Decisiones de preprocesamiento

Los puntajes SIMCE se mantienen en su escala original debido a que son directamente interpretables para las comparaciones territoriales planteadas.

En F2 no se aplica normalización ni escalamiento porque en esta etapa todavía no existe un algoritmo que requiera trabajar con variables numéricas en una escala común. Esta decisión evita incorporar transformaciones innecesarias antes de definir las técnicas de análisis que serán utilizadas en fases posteriores.

Los valores ausentes asociados a identidad, ubicación geográfica o puntaje no son reemplazados artificialmente, ya que hacerlo podría incorporar información que no se encuentra presente en la fuente original.

Los posibles valores atípicos son utilizados como elemento de diagnóstico y no son eliminados automáticamente. Un establecimiento con un número elevado de estudiantes o con un resultado extremo puede representar una observación válida dentro del conjunto de datos.

La regla de filtrado conserva establecimientos con una cantidad de alumnos evaluados mayor a cero y sin una observación asociada al resultado de Matemática. Las marcas `[1, 2, 3, 4]` se consideran observaciones dentro del procesamiento actual.

Existen **55 establecimientos con puntaje disponible que igualmente son excluidos por la regla de efectividad**, principalmente asociados al caso de marca 2. Estos registros no se eliminan sin dejar evidencia, sino que permanecen disponibles en el archivo de auditoría para permitir su revisión.

## Validación técnica

F2 realiza diferentes controles sobre el dataset procesado, entre ellos:

- que el dataset final no se encuentre vacío;
- presencia y unicidad del RBD;
- alumnos evaluados mayores a cero;
- presencia del puntaje promedio;
- asignatura correspondiente a Matemática;
- información territorial completa;
- coherencia entre códigos y nombres geográficos;
- fecha de la base válida;
- ausencia de columnas duplicadas;
- reconciliación entre registros originales, efectivos y excluidos;
- reconciliación de la cobertura regional con la base original;
- ausencia en el producto final de variables retiradas del alcance.

Además de las validaciones realizadas sobre los datos reales, el notebook incluye pruebas controladas para comprobar el comportamiento de las reglas implementadas.

Estas pruebas consideran:

- un caso normal;
- un caso límite sin alumnos evaluados;
- un registro con observación;
- un registro con marca 2 y puntaje disponible;
- un código desconocido que debe generar una excepción.

De esta forma, la validación no se limita únicamente al resultado final, sino que también comprueba el comportamiento esperado de las reglas utilizadas durante el procesamiento.

## Alcance y limitaciones

Las fases F1 y F2 tienen como objetivo preparar una base reproducible, consistente y documentada para las etapas posteriores del proyecto.

En estas fases no se busca establecer causalidad entre ubicación geográfica y rendimiento académico, ni determinar directamente dónde deberían asignarse recursos educativos.

Las comparaciones territoriales, pruebas de significancia, visualizaciones analíticas y conclusiones sobre posibles focos de menor desempeño corresponden a fases posteriores.

Una consideración que permanece documentada es la revisión de las glosas asociadas a `marca_mate4b_rbd`, especialmente para los casos en que una observación puede coexistir con un puntaje numérico. Por esta razón, estos registros permanecen identificados dentro de la auditoría y no se ocultan durante el procesamiento.

## Trazabilidad

El repositorio mantiene historial Git, notebooks ejecutables, documentación técnica, archivos de auditoría y productos procesados.

La relación entre la planificación inicial y el desarrollo realizado se encuentra registrada en:

```text
docs/vinculacion_mapa_conceptual.csv
```

Este archivo permite identificar qué componentes del proyecto ya fueron implementados durante F1 y F2 y cuáles permanecen proyectados para las fases posteriores.

El uso conjunto de Git, los notebooks, la documentación almacenada en `docs/` y los productos de `data/processed/` permite mantener evidencia de las decisiones tomadas y de los resultados generados durante el desarrollo del proyecto.