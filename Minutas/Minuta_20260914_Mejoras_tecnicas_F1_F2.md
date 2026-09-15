# Minuta: mejoras técnicas de F1 y F2

Fecha: 14 de septiembre de 2026. Grupo 7.

## Acuerdo y alcance

Reforzamos el proyecto para preparar una buena entrega de F1 y F2, manteniendo
la comparación territorial de Matemática de cuarto básico como propósito.
Esta minuta registra cambios técnicos realizados en esta revisión. No asignamos
puntajes por portada, exposición, formato institucional ni participación del grupo.

## Cambios realizados

| Archivo | Cambio y motivo |
| --- | --- |
| `F1/F1_Definicion.ipynb` | La ficha calcula dimensiones, tamaño y porcentajes ausentes desde el bruto. Evita mantener cifras manuales desactualizadas. |
| Mismo notebook | Los roles se cuentan desde el diccionario. Comuna y `noaplica` quedan como nominales: no identifican un establecimiento y `noaplica` tiene más de dos valores. |
| Mismo notebook | Comprueba que el diccionario cubra las columnas del bruto y evalúa los criterios después de leerlo. |
| Mismo notebook | La licencia queda pendiente de confirmar, en lugar de declarar apertura sin respaldo. El generador conserva un README existente. |
| `F2/F2_Preprocesamiento.ipynb` | Se separaron funciones con parámetros para leer datos, convertir fechas, filtrar establecimientos y validar la salida. Se agregaron comentarios breves que explican su uso. |
| Mismo notebook | El filtro devuelve una copia y detecta resultados vacíos. La fecha rechaza vacíos, formatos incorrectos y fechas imposibles. |
| Mismo notebook | Se agregó una celda con 11 resultados de pruebas: filtro normal y límite cero, entrada intacta, filtro vacío, columna faltante, fecha válida e inválida, fecha ausente, salida vacía, RBD repetido, porcentaje inválido, puntaje ausente y porcentajes ausentes permitidos. Algunos controles se agrupan en un resultado. |
| `docs/diccionario_variables.csv` | Regenerado con los roles corregidos. |
| `docs/evaluacion_criterios_dataset.csv` | Regenerado con las medidas reales del bruto. |
| `docs/metadatos_fase1.json` | Actualiza la ejecución e incluye conteos de roles, máximo de ausentes y licencia pendiente. |
| `README.md` | Agrega comandos del entorno, selección de kernel, orden de ejecución y explicación breve del tratamiento de ausentes y escala. |
| Informes del dataset, raíz y F1 | Se aclara qué reporte contiene la evaluación vigente para evitar una referencia incorrecta al límite de ausentes. |

## Comprobación realizada

Se ejecutaron F1 y F2 completos con `SIMCE Grupo 7 (.venv)` mediante Jupyter,
fuera de la interfaz de VS Code. Ambos finalizaron sin errores; las salidas quedaron
guardadas en los notebooks. Las 11 pruebas de F2 pasaron y también la comparación
entre el DataFrame final y el CSV vuelto a leer.

Se compararon las huellas SHA-256 antes y después: el bruto y el CSV procesado
conservaron exactamente su contenido. F2 sí volvió a exportar el archivo.
El bruto tiene 7.143 filas y 42 columnas; la salida tiene 6.524 filas y 33 columnas.
Se excluyen 619 establecimientos con el criterio actual.

El máximo de ausentes del bruto es 92,93 %. En la salida faltan los tres
porcentajes de niveles de aprendizaje para 1.446 establecimientos (22,16 %).
No se rellenan con cero ni se eliminan esos colegios de la comparación de puntajes.

## Qué queda pendiente dentro del proyecto

- Confirmar con las glosas oficiales de 2025 el significado de las marcas excluidas.
  Hay 55 establecimientos con puntaje disponible excluidos por marca. Mantenemos
  el criterio del grupo hasta contar con ese respaldo; su justificación sigue pendiente.
- Confirmar las condiciones de uso de la fuente y registrar su referencia.
- Si se exige que ninguna columna del bruto supere 60 % de ausentes, el bruto
  completo no lo cumple. Procesarlo no cambia esa característica de la fuente.
- Los informes exploratorios de los validadores auxiliares usan clasificación
  automática de tipos. El diccionario de F1 es la referencia analítica del proyecto.
- La ejecución comprobada no reproduce el bloqueo de la interfaz de VS Code;
  no se considera resuelto ese problema del editor por haber pasado estas pruebas.

Las mejoras aportan evidencia de funciones, manejo de errores, validación,
reproducibilidad y documentación. La calificación final depende de la revisión
de la entrega; no se garantiza una nota específica.

## Segunda revisión: problemática y preprocesamiento

En F1 agregamos una pregunta específica para esta entrega: cómo preparar una
base comparable para estudiar diferencias territoriales en Matemática de 4° básico
2025. Conservamos la pregunta general del proyecto y aclaramos que las pruebas
de significancia corresponden a fases posteriores.

Declaramos supuestos y criterios de éxito verificables: una fila por establecimiento,
datos del mismo curso y año, puntaje disponible, territorio completo y exclusiones
registradas. Un promedio simple de puntajes de colegios describe establecimientos,
no el promedio individual de todos los estudiantes. Tampoco permite atribuir las
diferencias al territorio ni decidir por sí solo dónde asignar recursos.

En F2 hicimos estos ajustes:

- Normalizamos espacios y caracteres Unicode en los textos, conservando tildes y nombres.
- Validamos año 2025, grado 4b, puntajes finitos, alumnos enteros positivos, fechas
  convertidas y nombres territoriales no vacíos.
- Comprobamos que una comuna no aparezca asociada a varias provincias y que una
  provincia no aparezca asociada a varias regiones dentro de la salida.
- Exportamos `data/processed/auditoria_filtro.csv`: una fila por registro del bruto,
  con indicadores de falta de alumnos, marca excluida, puntaje disponible e inclusión.
  Las razones pueden coincidir y no deben sumarse como causas independientes.
- Exportamos `data/processed/cobertura_regional.csv`: cantidad inicial, incluida,
  excluida, porcentaje de retención y disponibilidad de los tres porcentajes por región.
  Esto permite reconocer diferencias de cobertura antes de comparar resultados.
- Explicamos por qué no imputamos puntajes ni porcentajes, no recortamos extremos
  automáticamente y conservamos la escala SIMCE original. Los niveles de aprendizaje
  se analizarán con casos completos, informando cuántos colegios participan.
- Agregamos cinco pruebas: año distinto, curso distinto, puntaje infinito,
  alumnos fraccionarios y nombre territorial vacío.

Se ejecutaron nuevamente F1 y F2 completos con el kernel de `.venv`: ambos finalizaron
correctamente, pasaron los 16 resultados de pruebas y la verificación de exportación.
El CSV principal mantiene 6.524 filas y 33 columnas. Los dos reportes complementan
esa salida. Confirmar las glosas de las marcas continúa pendiente; la auditoría hace
visible la selección, pero no sustituye su justificación oficial.
