# Caracterización e Inequidad en los Resultados Académicos del SIMCE 4º Básico en Chile

**Grupo:** Grupo 7

## Integrantes
- Felipe Palma Barrientos
- Vicente Aguilar Rojas
- Cristian Grandon Grandon
- Jorge Gutierrez Jaramillo

## Propósito del proyecto

El proyecto prepara un flujo reproducible para analizar las diferencias territoriales en los puntajes promedio de Matemática del SIMCE 2025 de 4º Básico. La unidad de análisis es el establecimiento educacional identificado por RBD. Las fases F1 y F2 definen la problemática, documentan la fuente y construyen una base comparable y validada; las comparaciones descriptivas e inferenciales corresponden a fases posteriores.

## Datos

- **Dataset:** Resultados prueba SIMCE 4º Básico 2025 por establecimiento.
- **Fuente:** Agencia de Calidad de la Educación.
- **Portal:** Bases de datos públicas de la Agencia de Calidad de la Educación.
- **Enlace:** https://informacionestadistica.agenciaeducacion.cl/#/bases
- **Unidad de observación:** establecimiento educacional (RBD).
- **Base bruta:** 7.143 filas × 42 columnas.
- **Salida F2:** 6.524 establecimientos × 33 columnas.

## Estructura del repositorio

```text
F1/
  F1_Definicion.ipynb
F2/
  F2_Preprocesamiento.ipynb
data/
  raw/
    simce4b2025_rbd_final.csv
  processed/
    simce4b2025_matematica_efectiva.csv
    auditoria_filtro.csv
    cobertura_regional.csv
docs/
  diccionario_variables.csv
  evaluacion_criterios_dataset.csv
  metadatos_fase1.json
  vinculacion_mapa_conceptual.csv
Minutas/
src/
requirements.txt
README.md
```

## Entorno y dependencias

El proyecto fue desarrollado con Python 3.14.7. Las dependencias se encuentran fijadas en `requirements.txt`.

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

Desde la raíz del repositorio, en PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m ipykernel install --sys-prefix --name simce-grupo7 --display-name "SIMCE Grupo 7 (.venv)"
.\.venv\Scripts\python.exe -m jupyter lab
```

Seleccionar el kernel `SIMCE Grupo 7 (.venv)` y ejecutar, desde un kernel reiniciado, primero `F1/F1_Definicion.ipynb` y después `F2/F2_Preprocesamiento.ipynb`.

En macOS/Linux, después de crear el entorno se activa con:

```bash
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip check
jupyter lab
```

## Productos de la Fase 2

`F2/F2_Preprocesamiento.ipynb` regenera tres productos:

- `data/processed/simce4b2025_matematica_efectiva.csv`: dataset principal procesado, con 6.524 establecimientos y 33 columnas.
- `data/processed/auditoria_filtro.csv`: una fila por registro del bruto, con indicadores de ausencia de alumnos, marca excluida, disponibilidad de puntaje e inclusión final.
- `data/processed/cobertura_regional.csv`: resumen por región con establecimientos iniciales, incluidos, excluidos, porcentaje de retención y disponibilidad de los porcentajes de niveles de aprendizaje.

El notebook vuelve a leer el CSV principal después de exportarlo y compara su contenido con el DataFrame en memoria.

## Decisiones de preprocesamiento

Los puntajes SIMCE se mantienen en su escala original, ya que son directamente interpretables para las comparaciones territoriales planteadas. No se aplica escalamiento en F2 porque no es necesario para este objetivo.

Los porcentajes `pct_insuficiente`, `pct_elemental` y `pct_adecuado` conservan sus valores ausentes. No se reemplazan por cero, ya que la ausencia de información no implica que ningún estudiante pertenezca al nivel correspondiente. Tampoco se eliminan esos establecimientos cuando mantienen puntaje y ubicación válidos para la pregunta principal.

La regla de filtrado actual conserva registros con alumnos evaluados mayores a cero y excluye las marcas `[1, 2, 3, 4]`. Esta lista corresponde al criterio de trabajo actual del equipo. Su significado institucional debe confirmarse con las glosas oficiales de la base SIMCE 2025 antes de atribuir a cada código una interpretación específica. Actualmente existen 55 establecimientos con puntaje disponible que son excluidos por esta regla, por lo que su efecto permanece visible mediante `auditoria_filtro.csv`.

## Validación técnica

F2 valida, entre otros elementos:

- unicidad del RBD;
- alumnos evaluados positivos y enteros;
- puntajes presentes y finitos;
- año 2025 y grado 4b;
- códigos y nombres territoriales completos;
- coherencia comuna → provincia → región;
- porcentajes dentro del rango 0–100 cuando están disponibles;
- suma aproximada de 100% para filas con los tres porcentajes presentes;
- generación y relectura de los archivos exportados.

Además, el notebook contiene pruebas controladas para casos normales, límite y excepciones, sin modificar el dataset final.

## Alcance y limitaciones

F1 y F2 preparan una base reproducible para el análisis. No establecen causalidad entre territorio y rendimiento y no determinan por sí solas dónde asignar recursos. Las comparaciones estadísticas, pruebas de significancia y conclusiones territoriales corresponden a fases posteriores.

La principal limitación pendiente es confirmar documentalmente las glosas oficiales de `marca_mate4b_rbd` para la versión 2025 de la base.

## Trazabilidad

El repositorio mantiene historial Git, notebooks ejecutables, documentación en `docs/`, minutas de decisiones y artefactos procesados. La vinculación entre mapa conceptual, F1, F2 y fases posteriores se registra en `docs/vinculacion_mapa_conceptual.csv`.