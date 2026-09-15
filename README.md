# Caracterización e Inequidad en los Resultados Académicos del SIMCE 4º Básico en Chile

**Grupo:** Grupo 7

## Integrantes
- Felipe Palma
- Vicente Aguila
- Cristian Grandon
- Jorge Gutierrez

## Datos
- Dataset: Resultados prueba SIMCE 4º Básico 2025 por Establecimiento
- Fuente: Agencia de Calidad de la Educación
- Plataforma: Bases de datos públicas de la Agencia de Calidad de la Educación
- Enlace: https://informacionestadistica.agenciaeducacion.cl/#/bases
- Unidad de observación: Un establecimiento educacional (RBD)
- Dimensiones: 7,143 filas x 42 columnas

## Estructura del repositorio

- `data/raw/`: datos originales sin modificar.
- `data/processed/`: datos procesados en fases posteriores.
- `docs/`: documentación y metadatos.
- `src/`: módulos reutilizables.
- `F1/`: definición y preparación del proyecto.
- `F2/`: procesamiento de datos.
- `F3/` y `F4/`: fases posteriores.

## Requisitos

Python: 3.14.7

### Dependencias
- ipykernel
- jupyterlab
- matplotlib==3.11.1
- notebook
- numpy==2.5.2
- pandas==3.0.5
- seaborn==0.13.2

## Reproducibilidad

La semilla utilizada durante el proyecto es `42`.

Los datos originales no se modifican durante la Fase 1.

### Ejecución local de F1 y F2

Desde la raíz del proyecto, en PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m ipykernel install --sys-prefix --name simce-grupo7 --display-name "SIMCE Grupo 7 (.venv)"
.\.venv\Scripts\python.exe -m jupyter lab
```

Si `.venv` ya existe, se omite el primer comando. Seleccionar el kernel
`SIMCE Grupo 7 (.venv)` y ejecutar todas las celdas de `F1/F1_Definicion.ipynb`
y luego de `F2/F2_Preprocesamiento.ipynb`, desde un kernel reiniciado.

F1 actualiza el diccionario y los metadatos sin sobrescribir este README.
F2 ejecuta sus pruebas antes de exportar
`data/processed/simce4b2025_matematica_efectiva.csv`.
La salida actual contiene 6.524 establecimientos y 33 columnas.

F2 también genera `data/processed/auditoria_filtro.csv`, con el estado de inclusión
de cada registro del bruto, y `data/processed/cobertura_regional.csv`, con la
retención y disponibilidad de porcentajes por región. Estos reportes ayudan a
interpretar qué parte de los datos estamos comparando.

El alcance actual es preparar y validar la base. Las comparaciones estadísticas
quedan para las fases posteriores. Nuestra unidad de análisis es el establecimiento;
un promedio simple entre colegios no equivale al promedio de todos los estudiantes.

El puntaje y los datos territoriales son necesarios para nuestra comparación.
Los porcentajes de niveles de aprendizaje ausentes se conservan: no equivalen
a cero. Para analizar esos niveles se usarán los casos disponibles, indicando
cuántos establecimientos participan. La fecha corresponde a la base, no al día
en que cada estudiante rindió SIMCE. Conservamos los puntajes en su escala original
porque permiten interpretar las diferencias; no hace falta escalarlos en esta fase.

Los cambios y pendientes técnicos están en
[la minuta de mejoras](Minutas/Minuta_20260914_Mejoras_tecnicas_F1_F2.md).
