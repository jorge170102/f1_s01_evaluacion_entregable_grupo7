# Minuta — Estado y revisión del proyecto F1 y F2

**Fecha:** 14-09-2026  
**Proyecto:** Grupo 7 — SIMCE 4° Básico 2025, Matemática  
**Tipo:** Registro de trabajo local y evaluación técnica orientativa  
**Alcance:** F1 y F2. No se exige desarrollar F3/F4 en esta entrega.  
**Autoría del documento:** Síntesis elaborada con asistencia de Codex; no constituye un acta de aprobación del profesor.

## 1. Propósito y criterio de trabajo acordado

La problemática busca analizar diferencias en los puntajes promedio de Matemática de los establecimientos según región, provincia y comuna. El procesamiento de F2 debe preparar un conjunto de datos útil para esa comparación.

El objetivo actual es partir del CSV bruto, seleccionar mediciones utilizables, normalizar y transformar lo pertinente, validar y exportar. No es necesario aplicar todas las técnicas a todas las variables ni obtener una evaluación perfecta. Se mantiene la organización y el estilo del proyecto del equipo, con mejoras puntuales en sus notebooks.

F2 prepara los datos; todavía no responde si las diferencias territoriales son estadísticamente significativas. Un puntaje menor tampoco demuestra, por sí solo, una mayor necesidad de recursos. Esas conclusiones requieren análisis posteriores y consideración del contexto.

## 2. Situación inicial y cambios conservados

El proyecto original no tenía un pipeline roto: F1 y F2 ejecutaban y F2 producía 6.524 establecimientos. La selección de columnas ya incluía puntaje, ubicación y contexto pertinentes.

Durante la asistencia se añadieron inicialmente módulos, pruebas, scripts y documentación extensa. El equipo solicitó recuperar su estructura. Esos añadidos fueron retirados y se recuperaron sus documentos y el código de F2 a partir de la lectura previa a la intervención. F2 no se restauró desde Git porque la versión allí registrada solo contenía un ejemplo inicial. Las salidas de los notebooks se regeneraron al verificar su ejecución; no se afirma que sus archivos sean idénticos byte por byte a la ejecución anterior.

La versión actual conserva únicamente ajustes acotados en F2:

| Ajuste | Resultado |
| --- | --- |
| Detectar conversiones numéricas inválidas | El notebook avisa y se detiene en lugar de introducir nulos silenciosamente. Los nulos originales se conservan. |
| Limpiar nombres antes de concatenar ubicaciones | Las ubicaciones compuestas también utilizan nombres normalizados. |
| Comprobar códigos antes de aplicar mapeos | Los códigos no reconocidos no se convierten silenciosamente en categorías ausentes. |
| Conservar códigos de región, provincia y comuna | Se puede agrupar y cruzar información usando códigos y nombres. |
| Comprobar RBD únicos, puntaje y ubicación disponibles | Se protege la unidad de observación y la información principal de la problemática. |
| Validar porcentajes disponibles | Se comprueba el rango 0–100 y la suma de los tres porcentajes completos, admitiendo 0,15 puntos de diferencia por redondeo. |
| Mostrar causas de exclusión y ausencias | Se hace visible el efecto de las decisiones. Las causas pueden solaparse y no deben sumarse como si fueran excluyentes. |
| Releer el CSV exportado | Se compara su contenido con la tabla en memoria, tolerando diferencias de tipos entre pandas y CSV. |

No se modificó el criterio de selección de establecimientos ni se añadieron escalamiento, imputaciones, modelos o una matriz numérica adicional. No se eliminaron los porcentajes complementarios.

## 3. Archivos y resultados actuales

| Elemento | Ubicación | Estado |
| --- | --- | --- |
| Definición del problema | `F1/F1_Definicion.ipynb` | Código y estructura del equipo conservados; ejecución comprobada. |
| Preprocesamiento | `F2/F2_Preprocesamiento.ipynb` | Ajustes puntuales incorporados; ejecución comprobada. |
| Datos originales | `data/raw/simce4b2025_rbd_final.csv` | 7.143 filas y 42 columnas; no se modificaron. |
| Datos procesados | `data/processed/simce4b2025_matematica_efectiva.csv` | 6.524 filas y 33 columnas. |
| Diccionario | `docs/diccionario_variables.csv` | Describe las variables originales, no las 33 columnas de salida. Conserva inconsistencias pendientes señaladas más abajo. |
| Documentación existente | `README.md`, `docs/`, `Minutas/` | Se conserva; esta minuta documenta el estado actual sin reescribir esos archivos. |

El resultado mantiene los mismos establecimientos y puntajes que la salida anterior de 30 columnas. Las tres columnas añadidas son `cod_reg_rbd`, `cod_pro_rbd` y `cod_com_rbd`.

Comprobaciones de la última ejecución de F2:

- El notebook completó su ejecución sin errores y verificó la relectura del CSV.
- Se mantuvieron los RBD y los puntajes respecto del CSV anterior.
- La huella SHA-256 del archivo bruto permaneció igual antes y después.
- No hay RBD duplicados en la salida.
- En la inspección para esta minuta, las únicas columnas con nulos son los tres porcentajes de niveles de aprendizaje, con 1.446 ausencias cada una.

Las pruebas extensas de doce casos y la matriz de 25 columnas pertenecían a la ampliación retirada. No forman parte de la versión actual ni se utilizan para evaluarla.

## 4. Selección de registros y sentido de las columnas

El filtro actual conserva establecimientos con `nalu_mate4b_rbd > 0` y cuya `marca_mate4b_rbd` no pertenece a `[1, 2, 3, 4]`. Las marcas ausentes se admiten según esa regla. Se excluyen 619 establecimientos en total.

Esta es la regla de trabajo del equipo; queda pendiente confirmar el significado institucional de las marcas con el diccionario oficial. El código no agrega un filtro independiente por `noaplica`. No se debe afirmar que lo hace. Después de seleccionar se comprueba que los puntajes y la ubicación necesaria estén disponibles.

La tabla conserva:

- Identificación y nombres de establecimientos.
- Región, provincia y comuna, con códigos y nombres; departamento provincial y ubicaciones compuestas.
- Zona, macrozona y orden geográfico definidos por los mapeos del proyecto.
- Dependencia, grupo socioeconómico y ruralidad como contexto.
- Cantidad de alumnos evaluados y puntaje promedio de Matemática.
- Porcentajes de niveles de aprendizaje como información complementaria.
- Datos de identificación de la base, año y grado.

No se eligieron mal las columnas. Algunas son complementarias y no serán necesarias para todas las comparaciones. Los puntajes se mantienen en unidades originales y los nombres se conservan para facilitar la interpretación.

## 5. Qué significan las celdas vacías de Excel

Hay 1.446 establecimientos con puntaje de Matemática disponible, pero sin información en `pct_insuficiente`, `pct_elemental` y `pct_adecuado`. Representan aproximadamente el 22,16% de las 6.524 filas seleccionadas.

Excel muestra esos valores ausentes como celdas vacías. No indican que el CSV no se haya actualizado ni que los alumnos tengan puntaje cero. El motivo exacto de su ausencia requiere la documentación oficial de la base; no se presume una causa específica.

La decisión actual es conservarlos vacíos:

1. La pregunta principal utiliza puntaje y territorio, que están disponibles.
2. Rellenar con cero afirmaría que ningún alumno pertenece a ese nivel, algo que no sabemos.
3. Eliminar esas filas perdería establecimientos útiles para comparar puntajes.
4. Si después se estudian niveles de aprendizaje, se utilizarán los registros con porcentajes disponibles y se informará su denominador. Actualmente son 5.078 establecimientos con los tres porcentajes.

Un dataset procesado puede conservar nulos documentados. Estar procesado significa que las decisiones están definidas y las variables necesarias son utilizables, no que se rellenaron todas las celdas. En particular, escalar una variable no resuelve sus datos ausentes.

## 6. Evaluación orientativa del 1 al 10

**Evaluación general: 7/10.** La preparación orientada a la problemática está bien encaminada y mejoró su control de calidad. Todavía hay evidencia académica y documentación por completar. La calificación es un juicio técnico orientativo, no un promedio matemático de la tabla ni una nota del profesor.

| Aspecto | Logro | Fundamento y pendiente |
| --- | ---: | --- |
| Problemática y selección de variables | 9/10 | Puntaje, territorio y contexto permiten preparar las comparaciones planteadas. La inferencia corresponde a fases posteriores. |
| Organización y ejecución local | 8/10 | F1/F2 ejecutan con la estructura actual. Falta resolver rutas de validadores auxiliares y verificar un entorno limpio. |
| Ficha y diccionario de F1 | 6/10 | Existe documentación de 42 variables, pero contiene cifras y roles inconsistentes. |
| Carga, filtrado y normalización de F2 | 8/10 | El flujo funciona y conserva 6.524 establecimientos; se mejoró el orden de limpieza. Falta respaldo oficial de las marcas. |
| Tratamiento de datos incompletos | 7/10 | Las ausencias se identifican, se explican y no afectan las variables principales. Falta una comparación cuantitativa de alternativas si la rúbrica la exige. |
| Transformaciones acordes a la problemática | 7/10 | Tipos numéricos, texto, etiquetas y geografía son pertinentes. Codificación adicional y escalamiento dependen del uso y de la exigencia formal del curso. |
| Funciones y recursividad | 5/10 | F1 contiene funciones; F2 sigue organizado principalmente en bloques y no muestra recursividad. |
| Validación de datos y exportación | 8/10 | Hay controles de identidad, ubicación, conversiones, categorías, porcentajes y relectura. No equivale a una batería de pruebas de funciones. |
| Pruebas normales, límites y excepciones | 5/10 | Las comprobaciones están aplicadas al dataset real; faltan pequeños casos artificiales para comprobar el comportamiento ante entradas inválidas. |
| Reflexión y trazabilidad documental | 7/10 | Esta minuta explica decisiones y resultados; quedan desajustes en la documentación de F1 y falta un cierre breve propio dentro de F2. |

La versión actual no necesita rehacerse para mejorar. Lo más útil sería resolver las inconsistencias y completar algunas funciones y pruebas dentro del mismo notebook, sin volver a ampliar innecesariamente el repositorio.

## 7. Pendientes concretos

### Prioridad alta: precisión de la documentación y del filtro

1. **Confirmar las marcas con el diccionario oficial.** Revisar qué significa cada código y su relación con `noaplica`, sin cambiar el filtro basándose solo en suposiciones.
2. **Corregir la ficha de F1.** Declara 28,4% como máximo de nulos, mientras que el máximo de la base completa es aproximadamente 92,93% en las marcas. El 28,4% corresponde a otro grupo de variables, no al máximo general.
3. **Corregir los roles y sus conteos.** `noaplica` está descrita como binaria, aunque en el bruto presenta cuatro valores. La evaluación registra ocho variables continuas, mientras el diccionario clasifica doce.
4. **Resolver el criterio docente de ausencias.** El ejemplo incluye un umbral máximo de 60% por variable y la base completa lo supera. La naturaleza de las marcas puede sustentar una explicación, pero su aceptación corresponde al profesor. Que el procesamiento funcione no concede automáticamente una excepción.

### Prioridad media: completar evidencia sin cambiar el rumbo

5. Convertir algunos bloques de F2 en funciones, por ejemplo carga, filtrado y validación, manteniéndolas dentro del notebook.
6. Añadir pocos casos de prueba: una entrada correcta, una vacía y una con datos inválidos. No es necesario crear otra carpeta de pruebas para ello.
7. Incorporar una aplicación pequeña de recursividad si es exigida por la rúbrica, por ejemplo al recorrer metadatos anidados.
8. Mostrar una tabla de nulos y el efecto de conservar o eliminar filas con porcentajes ausentes. Justificar con esos números la decisión actual.
9. Comprobar qué transformaciones exige la rúbrica. Para la comparación territorial no es necesario escalar el puntaje ni convertir toda la tabla a números. Si se exige demostrar esas técnicas, puede hacerse sobre una copia sin cambiar la salida principal.
10. Añadir un cierre breve en F2 con las dimensiones finales, exclusiones, tratamiento de nulos y limitaciones.

### Ajustes documentales y de ejecución

11. Actualizar las rutas personales de los dos validadores auxiliares: uno todavía apunta al dataset de IPC. F1 y F2 principales sí ejecutan con las rutas actuales.
12. Alinear el título y alcance del README con el planteamiento actual de Matemática, conservando su estructura. Las 7.143 filas y 42 columnas del README describen correctamente el bruto; falta distinguir allí la salida de 6.524 × 33.
13. Documentar las columnas renombradas y añadidas por F2 sin confundir su diccionario con el de la base original.
14. Verificar un entorno virtual y la instalación en otro equipo. Los metadatos conservados de F1 indican uso de Python del sistema y una fecha anterior de ejecución.
15. Revisar las contribuciones y commits reales del equipo antes de publicar. No se generan autorías ni se modifica el historial para aparentar cumplimiento.

F3/F4, modelado, pruebas de significancia y conclusiones territoriales no son pendientes para esta entrega de F1/F2.

## 8. Guardado y uso local

El notebook F2 y su CSV actualizado ya están guardados. Esta minuta también queda guardada en `Minutas/`. No se crearon commits ni se realizó una publicación en GitHub en esta intervención.

Para regenerar el CSV después de editar el código, abrir `F2/F2_Preprocesamiento.ipynb` y ejecutar todas sus celdas en orden. La última sección exporta y verifica `data/processed/simce4b2025_matematica_efectiva.csv`. Conviene cerrar el archivo en Excel antes de regenerarlo para evitar bloqueos de escritura. Si VS Code mantiene una vista anterior, cerrar y abrir la pestaña.

Las pestañas de archivos retirados, como los módulos y pruebas añadidos durante la ampliación, pueden seguir visibles en el editor aunque esos archivos ya no formen parte del proyecto guardado.

## 9. Referencias de la comparación

- [Ejemplo docente del proyecto](https://github.com/magistercienciadatos/Material_Didactico_Semana1/tree/main/proyecto-grupoX-mcdi500).
- [Notebook F1 del profesor](https://github.com/magistercienciadatos/Material_Didactico_Semana1/blob/main/proyecto-grupoX-mcdi500/F1/notebooks/S1_F1_Definicion.ipynb).
- [Notebook F2 del profesor](https://github.com/magistercienciadatos/Material_Didactico_Semana1/blob/main/proyecto-grupoX-mcdi500/F2/S1_F2_Preprocesamiento.ipynb).

La comparación utiliza la lectura del ejemplo realizada durante esta sesión y el estado local inspeccionado al redactar esta minuta. No sustituye la rúbrica formal, el diccionario oficial del SIMCE ni la evaluación del docente.
