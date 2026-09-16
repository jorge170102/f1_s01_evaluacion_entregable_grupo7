# Caracterización e Inequidad en los Resultados Académicos del SIMCE 4º Básico en Chile

**Grupo:** Grupo 7

## Integrantes

* Felipe Palma Barrientos
* Vicente Aguila Rojas
* Cristian Grandon Grandon
* Jorge Gutierrez Jaramillo

## Propósito del proyecto

El proyecto desarrolla un flujo reproducible para preparar y analizar los resultados de Matemática del SIMCE 2025 de 4º Básico, considerando como unidad de análisis al establecimiento educacional identificado mediante su RBD.

La Fase 1 define la problemática, los objetivos, el alcance, las restricciones y la estructura técnica del proyecto.

La Fase 2 implementa el proceso de obtención, exploración, limpieza, transformación, auditoría, validación y exportación de los datos necesarios para las fases analíticas posteriores.

Las comparaciones descriptivas, pruebas de significancia estadística, visualizaciones y conclusiones territoriales corresponden a fases posteriores del proyecto.

## Fuente de datos

* **Dataset:** Resultados SIMCE 4º Básico 2025 por establecimiento.
* **Asignatura:** Matemática.
* **Fuente:** Agencia de Calidad de la Educación.
* **Portal:** Bases de datos públicas de la Agencia de Calidad de la Educación.
* **Enlace:** https://informacionestadistica.agenciaeducacion.cl/#/bases
* **Unidad de observación:** establecimiento educacional identificado mediante RBD.
* **Registros disponibles:** 7.143 establecimientos.

Para mantener el pipeline eficiente, la Fase 2 realiza una carga selectiva de **20 variables** necesarias para el procesamiento actual, preservando sin modificaciones el archivo bruto disponible en `data/raw/`.

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
    simce4b2025_matematica_efectiva_AAAAMMDDHHMM.csv
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

El nombre del dataset principal procesado incorpora una marca temporal con formato `AAAAMMDDHHMM`, permitiendo identificar la ejecución que produjo cada archivo.

## Entorno y dependencias

El proyecto fue desarrollado y validado utilizando Python 3.14.7.

Las dependencias se encuentran fijadas en `requirements.txt`.

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

Posteriormente se debe seleccionar el kernel:

```text
SIMCE Grupo 7 (.venv)
```

y ejecutar, desde un kernel reiniciado, los notebooks en el siguiente orden:

```text
1. F1/F1_Definicion.ipynb
2. F2/F2_Preprocesamiento.ipynb
```

Se recomienda utilizar:

```text
Restart Kernel → Run All Cells
```

y conservar los outputs generados como evidencia de ejecución.

En macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
pip check

jupyter lab
```

## Flujo de procesamiento de F2

La Fase 2 implementa el siguiente flujo:

```text
Fuente SIMCE
      ↓
Carga selectiva de variables
      ↓
Diagnóstico inicial
      ↓
Conversión de tipos
      ↓
Limpieza de campos de texto
      ↓
Validación de códigos categóricos
      ↓
Enriquecimiento geográfico
      ↓
Clasificación Efectiva / No Efectiva
      ↓
Auditoría de exclusiones
      ↓
Filtrado de registros efectivos
      ↓
Construcción del dataset final
      ↓
Cobertura regional
      ↓
Validaciones técnicas
      ↓
Exportación y verificación
```

## Regla de efectividad

La clasificación de los registros se realiza de forma explícita y reproducible.

Un establecimiento se considera **Efectivo** cuando:

1. presenta una cantidad de alumnos evaluados mayor que cero; y
2. no presenta una observación de puntaje asociada a `marca_mate4b_rbd`.

En caso contrario se clasifica como **No Efectivo**.

Las observaciones actualmente documentadas corresponden a los códigos:

* `1`: cantidad insuficiente de estudiantes evaluados;
* `2`: resultados no representativos por causas ajenas a la Agencia;
* `3`: resultados no representativos por causas ajenas al establecimiento;
* `4`: aplicación de prueba extendida que no permite evaluar la asignatura.

Cualquier código de marca desconocido provoca una excepción durante el procesamiento para evitar interpretar silenciosamente categorías no documentadas.

## Resultado del procesamiento

La ejecución actual procesa:

```text
Registros originales:          7.143
Registros efectivos:           6.524
Registros no efectivos:          619
Registros con puntaje:          6.579
No efectivos con puntaje:         55
```

El dataset analítico final contiene:

```text
6.524 filas × 30 columnas
```

con una fila por establecimiento efectivo.

## Productos de F2

El notebook `F2/F2_Preprocesamiento.ipynb` genera tres productos principales.

### Dataset procesado

```text
data/processed/simce4b2025_matematica_efectiva_AAAAMMDDHHMM.csv
```

Contiene exclusivamente los **6.524 establecimientos clasificados como Efectivos** y las 30 variables seleccionadas para las fases posteriores.

Entre ellas se incluyen:

* identificación del establecimiento;
* ubicación regional, provincial y comunal;
* zona y macrozona;
* dependencia administrativa;
* grupo socioeconómico;
* ruralidad;
* cantidad de alumnos;
* puntaje promedio de Matemática;
* fecha y código de la base;
* grado y año.

### Auditoría de exclusiones

```text
data/processed/auditoria_filtro.csv
```

Contiene los **619 registros clasificados como No Efectivos**.

Permite identificar para cada exclusión:

* RBD;
* establecimiento;
* ubicación territorial;
* número de alumnos;
* puntaje disponible;
* `marca_mate4b_rbd`;
* descripción de la observación;
* motivo de exclusión;
* metadatos de la base.

Además incorpora el indicador:

```text
marca_2_con_puntaje
```

para mantener trazabilidad específica sobre los casos con marca 2 que todavía poseen un puntaje registrado.

### Cobertura regional

```text
data/processed/cobertura_regional.csv
```

Resume el impacto del filtro para cada región.

Incluye, entre otros:

* registros originales;
* registros efectivos;
* registros no efectivos;
* registros no efectivos con puntaje;
* alumnos presentes en la base original;
* alumnos asociados a registros efectivos;
* alumnos asociados a registros no efectivos.

Esto permite verificar si el proceso de exclusión afecta de manera diferente a determinadas regiones.

## Caso especial: marca 2 con puntaje

Durante la auditoría se detectaron:

```text
55 registros
```

con `marca_mate4b_rbd = 2` que poseen puntaje disponible.

Estos registros permanecen clasificados como No Efectivos de acuerdo con la regla operacional del proyecto y son conservados explícitamente dentro de `auditoria_filtro.csv`.

La auditoría permite verificar posteriormente estos casos contra la documentación oficial SIMCE 2025 antes de realizar interpretaciones definitivas.

La diferencia observada entre el promedio de los establecimientos efectivos y el promedio de todos los registros con puntaje se calcula como análisis de sensibilidad, sin utilizarse automáticamente para reincorporar registros cuya representatividad se encuentra observada.

## Transformaciones aplicadas

Durante F2 se realizan las siguientes operaciones:

* conversión controlada de variables numéricas;
* conversión y validación de `fecha_bbdd`;
* limpieza de caracteres de control y espacios en variables de texto;
* traducción de códigos categóricos mediante catálogos explícitos;
* enriquecimiento territorial mediante una dimensión geográfica;
* validación de relaciones geográficas mediante un `merge many-to-one`;
* clasificación de efectividad;
* construcción de una auditoría de exclusiones;
* estandarización de nombres de variables;
* selección del esquema final;
* generación de cobertura regional;
* exportación y relectura del archivo final.

## Tratamientos no aplicados en F2

De manera deliberada, en esta fase:

* no se imputan puntajes;
* no se imputa información territorial;
* no se eliminan establecimientos únicamente por ser potenciales atípicos según IQR;
* no se realiza escalamiento o normalización;
* no se aplica codificación one-hot;
* no se realizan gráficos analíticos;
* no se realizan pruebas inferenciales;
* no se incorporan variables de porcentajes de niveles de aprendizaje al esquema final de F2.

Estas decisiones mantienen el dataset interpretable y reservan las transformaciones dependientes de una técnica estadística o modelo específico para las fases posteriores.

## Validación técnica

La Fase 2 realiza comprobaciones automáticas sobre el producto final y sobre la trazabilidad del proceso.

Entre ellas:

* el dataset final no puede estar vacío;
* todos los registros finales deben corresponder a Matemática;
* todos deben estar clasificados como Efectivos;
* el número de alumnos debe ser mayor que cero;
* el RBD debe estar presente;
* el RBD debe ser único;
* el puntaje promedio debe estar presente;
* la información geográfica debe estar completa;
* `fecha_bbdd` debe encontrarse correctamente convertida;
* no pueden existir columnas duplicadas;
* la suma de registros efectivos y auditados debe reconciliar con la cantidad de registros originales;
* la cobertura regional debe reconciliar con el dataset original y con el dataset final;
* las columnas de porcentajes excluidas del esquema no deben reaparecer accidentalmente.

## Pruebas de reglas críticas

F2 incluye pruebas reproducibles de la lógica de efectividad utilizando datos sintéticos controlados.

Se verifican:

* caso normal de establecimiento efectivo;
* caso límite sin alumnos;
* registro con observación de puntaje;
* registro con marca 2 y puntaje disponible;
* excepción ante un código de marca desconocido.

Estas pruebas se ejecutan sin modificar el dataset analítico final.

## Verificación de exportación

Después de generar el CSV principal, el notebook vuelve a leer el archivo desde disco y compara su contenido con el DataFrame existente en memoria mediante:

```python
pd.testing.assert_frame_equal(...)
```

Esto permite verificar que la exportación y posterior lectura no alteren el contenido del producto generado.

## Alcance y limitaciones

Las fases F1 y F2 preparan una base reproducible para los análisis posteriores.

En estas fases:

* no se establece causalidad entre ubicación territorial y rendimiento;
* no se determina directamente dónde deben asignarse recursos;
* no se realizan todavía pruebas de significancia estadística;
* no se construyen modelos predictivos;
* no se realizan conclusiones territoriales definitivas.

Estas tareas corresponden a fases posteriores del proyecto.

La interpretación definitiva de los códigos de `marca_mate4b_rbd`, especialmente los registros con código 2 y puntaje disponible, debe mantenerse vinculada a la documentación oficial de la base SIMCE 2025.

## Vinculación con las fases del proyecto

| Elemento                     | Estado             | Evidencia                                             |
| ---------------------------- | ------------------ | ----------------------------------------------------- |
| Fuente oficial SIMCE 2025    | Implementado       | `data/raw/` y carga selectiva                         |
| Exploración y calidad        | Implementado en F2 | Diagnóstico de tipos, nulos, duplicados y atípicos    |
| Limpieza                     | Implementado en F2 | Conversión de tipos, fechas y limpieza de textos      |
| Transformación               | Implementado en F2 | Categorías y dimensión geográfica                     |
| Control de representatividad | Implementado en F2 | Clasificación de efectividad y `auditoria_filtro.csv` |
| Validación técnica           | Implementado en F2 | Validaciones y pruebas controladas                    |
| Cobertura territorial        | Implementado en F2 | `cobertura_regional.csv`                              |
| Análisis estadístico         | Proyectado         | Fase posterior                                        |
| Escalamiento y encoding      | Proyectado         | Según técnica o modelo utilizado                      |
| Visualización                | Proyectado         | Fase posterior                                        |
| Comunicación de resultados   | Proyectado         | Informe final                                         |

## Control de versiones y trazabilidad

El repositorio utiliza Git y GitHub para mantener:

* historial verificable de cambios;
* contribuciones individuales;
* documentación de decisiones;
* notebooks ejecutables;
* productos procesados;
* minutas de avance;
* trazabilidad entre F1, F2 y las fases posteriores.

Los archivos generados en `data/processed/` permiten verificar la correspondencia entre las decisiones documentadas y los resultados del pipeline.
