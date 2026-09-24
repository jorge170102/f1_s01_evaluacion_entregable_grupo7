# Caracterización e inequidad en los resultados académicos del SIMCE 4.º Básico en Chile

**Curso:** MCDI500 — Programación para la Ciencia de Datos  
**Grupo:** 7  
**Fase actual:** F3 — Núcleo algorítmico, eficiencia e implementación orientada a objetos

## Integrantes

- Felipe Palma Barrientos
- Vicente Aguila Rojas
- Cristian Grandon Grandon
- Jorge Gutierrez Jaramillo

## Propósito del proyecto

El proyecto construye un flujo reproducible para preparar y analizar los resultados de Matemática del SIMCE 2025 de 4.º Básico a nivel de establecimiento educacional (RBD), manteniendo trazabilidad de las transformaciones y de los registros excluidos.

F1 define el problema y documenta la fuente; F2 implementa y valida el preprocesamiento; F3 conserva las reglas metodológicas ya validadas y evoluciona el núcleo del proyecto hacia una arquitectura modular orientada a objetos, incorporando recursividad aplicada, validaciones reejecutables, comparación de implementaciones y mediciones reproducibles de eficiencia.

## Datos y continuidad entre fases

- **Fuente:** Agencia de Calidad de la Educación.
- **Dataset:** Resultados prueba SIMCE 4.º Básico 2025 por establecimiento.
- **Unidad de análisis:** establecimiento educacional identificado por RBD.
- **Base de origen:** 7.143 registros × 42 variables.
- **Producto analítico F2/F3:** 6.524 establecimientos × 30 variables.
- **Registros mantenidos para auditoría:** 619.
- **Dimensión geográfica:** 346 comunas.

La regla de efectividad definida en F2 se conserva en F3: un establecimiento se considera efectivo cuando presenta alumnos evaluados mayores a cero y no posee observaciones asociadas al puntaje. Los registros excluidos no se eliminan de la trazabilidad, sino que permanecen en la salida de auditoría.

## Estructura del repositorio

```text
f1_s01_evaluacion_entregable_grupo7/
│
├── README.md
├── requirements.txt
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
│   ├── F3_Nucleo_Algoritmico.ipynb
│   └── NucleoF3.md
│
├── src/
│   ├── configuracion.py
│   ├── carga.py
│   ├── diagnostico.py
│   ├── transformacion.py
│   ├── auditoria.py
│   ├── validacion.py
│   ├── exportacion.py
│   ├── poo.py
│   ├── algoritmo.py
│   └── arquitectura.py
│
├── tests/
│   └── test_regla_efectividad.py
│
├── docs/
│   ├── arquitectura_f3.md
│   ├── diccionario_variables.csv
│   ├── evaluacion_criterios_dataset.csv
│   ├── metadatos_fase1.json
│   └── vinculacion_mapa_conceptual.csv
│
├── data/
│   ├── raw/
│   │   └── simce4b2025_rbd_final.csv
│   └── processed/
│       ├── simce4b2025_matematica_efectiva_*.csv
│       ├── auditoria_filtro_*.csv
│       └── cobertura_regional_*.csv
│
└── Minutas/
```

La lógica reutilizable se mantiene en `src/`; los notebooks concentran la ejecución, la evidencia y la documentación del proceso; `tests/` contiene pruebas reejecutables y `docs/` mantiene documentación técnica y de trazabilidad.

## Entorno reproducible

La última ejecución registrada de F3 utiliza:

- Python 3.14.7
- pandas 3.0.5
- NumPy 2.5.2

Las dependencias se encuentran declaradas en `requirements.txt`.

### Windows (PowerShell)

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m ipykernel install --sys-prefix --name simce-grupo7 --display-name "SIMCE Grupo 7 (.venv)"
.\.venv\Scripts\python.exe -m jupyter lab
```

### macOS / Linux

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip check
python -m ipykernel install --sys-prefix --name simce-grupo7 --display-name "SIMCE Grupo 7 (.venv)"
python -m jupyter lab
```

## Orden de ejecución

Desde un kernel reiniciado, ejecutar en este orden:

1. `F1/F1_Definicion.ipynb`
2. `F2/F2_Preprocesamiento.ipynb`
3. `F3/F3_Nucleo_Algoritmico.ipynb`

Para cada notebook se recomienda utilizar **Restart Kernel + Run All Cells** y guardar posteriormente las salidas.

Las pruebas automatizadas se pueden ejecutar desde la raíz con:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## F2 — Preprocesamiento validado

F2 implementa la obtención, limpieza, transformación y validación del dataset. Entre sus controles se encuentran:

- conversión explícita de tipos;
- limpieza y estandarización de variables textuales;
- incorporación de categorías documentadas;
- enriquecimiento geográfico con validación de cardinalidad;
- aplicación de la regla de efectividad;
- auditoría de registros no efectivos;
- reconciliación entre registros originales, efectivos y auditados;
- validación de unicidad del RBD;
- controles sobre puntaje, fecha, geografía y estructura final.

Los productos principales son el dataset analítico, la auditoría de exclusiones y la cobertura regional.

## F3 — Núcleo algorítmico

F3 conserva las reglas de F2 y reorganiza su ejecución mediante componentes especializados.

### Programación orientada a objetos

`src/poo.py` implementa:

- `Transformador`: clase abstracta que define la interfaz común.
- `TransformadorTipos`.
- `TransformadorTextos`.
- `TransformadorCategorias`.
- `TransformadorGeografia`.
- `TransformadorEfectividad`.
- `PipelineSIMCE`: compone y ejecuta los transformadores de forma secuencial.

La arquitectura evidencia herencia, polimorfismo y encapsulamiento. El pipeline utiliza el contrato común `transformar()` y mantiene internamente sus pasos y su registro de ejecución.

### Algoritmos, recursividad y eficiencia

`src/algoritmo.py` contiene:

- `aplanar_recursivo`;
- `construir_jerarquia_geografica`;
- `validar_geografia_recursiva`;
- `enriquecer_geografia_merge`;
- `enriquecer_geografia_diccionario`;
- `medir`.

La recursividad se aplica a estructuras anidadas y a la validación de la jerarquía territorial Región → Provincia → Comuna.

Para eficiencia se comparan dos implementaciones funcionalmente equivalentes del enriquecimiento geográfico:

1. `pandas.merge`;
2. búsqueda mediante diccionario de clave geográfica compuesta.

Las mediciones utilizan `time.perf_counter()` para tiempo y `tracemalloc` para memoria pico. También se evalúa el costo/beneficio de `validate="many_to_one"` y el crecimiento con diferentes tamaños de entrada.

### Arquitectura

`src/arquitectura.py` genera una tabla de arquitectura directamente desde las clases del proyecto mediante introspección. La documentación complementaria se encuentra en `docs/arquitectura_f3.md`.

### Sensibilidad y escalamiento

El notebook F3 incorpora un análisis de sensibilidad sobre la regla de efectividad, manteniendo separados los escenarios experimentales de la regla metodológica principal.

Los puntajes se conservan en su escala original. En esta fase no se aplica normalización o escalamiento porque el núcleo actual utiliza reglas lógicas, joins, mapeos, validaciones y agregaciones, y no un algoritmo que requiera distancias o variables en una escala común.

## Reproducibilidad y validación

La ejecución F3 registra:

- 7.143 registros de origen;
- 6.524 registros efectivos;
- 619 registros auditados;
- 346 comunas en la dimensión geográfica;
- ejecución completa de las celdas del notebook;
- controles de equivalencia entre implementaciones antes de interpretar las mediciones;
- validaciones finales mediante `assert` y pruebas reejecutables.

La comparación de eficiencia no modifica las reglas metodológicas: primero se comprueba la equivalencia de las salidas y luego se comparan tiempo y memoria.

## Historial de evolución F3

El desarrollo de F3 se incorporó de forma incremental. Entre los commits representativos se encuentran:

- `e6d5945` / `ec45620`: creación del cuaderno F3.
- `1d158e8`: incorporación de arquitectura POO.
- `b541bcd`: algoritmos, recursividad y medición reproducible.
- `ca7559b`: evidencia de POO.
- `7e57cc5`: flujo y diseño estructurado.
- `f540c44`: recursividad aplicada.
- `f0a1e45`: validación técnica y pruebas reejecutables.
- `b7175b9`: eficiencia y optimización.
- `974c707`: análisis del costo/beneficio de `validate="many_to_one"`.
- `79cc5ab`: crecimiento con el tamaño.
- `c9d2986`: análisis de sensibilidad.
- `4a885e7`: decisión sobre normalización y escalamiento.
- `e9d85c3`: documentación de arquitectura y trazabilidad.
- `16c8e6e`: verificación final de F3.
- `272ce20`, `0e98765` y `913a925`: correcciones de F3.

Esto permite seguir la evolución desde el pipeline funcional de F2 hasta la arquitectura modular y el núcleo algorítmico de F3.

## Contribuciones individuales

La trazabilidad se mantiene mediante el historial Git y los mensajes de commit.

| Integrante | Identidad(es) Git observadas | Contribuciones trazables en el historial |
|---|---|---|
| Jorge Gutierrez Jaramillo | `jorge170102`, `Jorge Gutierrez` | Modularización del pipeline F2 en `src/`, incorporación de pruebas, correcciones de rutas y reproducibilidad, documentación/README. |
| Vicente Aguila Rojas | `strongercoelt` | Arquitectura POO, documentación automática de arquitectura, validación, eficiencia, sensibilidad y decisión de normalización/escalamiento en F3. |
| Cristian Grandon Grandon | `Crisrgg` | Creación e integración del notebook F3, pipeline, evidencia POO, diseño estructurado y recursividad. |
| Felipe Palma Barrientos | `Felipe Palma`, `felipeandrespalmabarrientos-cpu` | Mejoras F2, minutas, verificación final, documentación/trazabilidad y correcciones de F3. |

> Existe además la identidad Git `TIC Cuarto Turno`, utilizada en dos commits de corrección de F3. Antes de la entrega debe asociarse explícitamente al integrante correspondiente mediante `.mailmap` o documentarse en esta sección para evitar ambigüedad de autoría.

## Trazabilidad

La relación entre definición del problema, preprocesamiento, arquitectura y evidencia se mantiene mediante:

- historial de commits;
- notebooks ejecutables;
- funciones reutilizables en `src/`;
- pruebas en `tests/`;
- documentación de arquitectura en `docs/`;
- minutas de trabajo;
- productos de auditoría y cobertura.

El objetivo es que cada decisión relevante pueda rastrearse desde el informe y el notebook hasta el código y su historial de versiones.

## Alcance

F3 consolida el núcleo de procesamiento, su arquitectura y la evidencia de eficiencia. No establece causalidad entre territorio y rendimiento ni reemplaza las fases posteriores de análisis estadístico e interpretación territorial.
