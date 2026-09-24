# Arquitectura del proyecto — Fase 3

## Núcleo algorítmico, eficiencia e implementación orientada a objetos

**Asignatura:** MCDI500 — Programación para la Ciencia de Datos  
**Proyecto:** Caracterización e inequidad en los resultados académicos del SIMCE 4.º Básico en Chile  
**Grupo:** 7  
**Fase:** F3 — Núcleo algorítmico, eficiencia e implementación orientada a objetos  

---

# 1. Propósito de la arquitectura

La Fase 3 evoluciona el pipeline desarrollado y validado durante F2 hacia una arquitectura modular, extensible y orientada a objetos, manteniendo las reglas metodológicas previamente definidas para el procesamiento de los resultados SIMCE de Matemática de 4.º Básico 2025.

El propósito de esta reorganización no es modificar arbitrariamente las transformaciones ya validadas, sino separar de forma más clara las distintas responsabilidades del sistema:

- configuración;
- carga de datos;
- diagnóstico;
- transformación;
- auditoría;
- validación;
- programación orientada a objetos;
- algoritmos y recursividad;
- medición de eficiencia;
- documentación de arquitectura.

La lógica reutilizable se mantiene dentro del directorio `src/`, mientras que `F3/F3_Nucleo_Algoritmico.ipynb` funciona como capa de integración, ejecución, documentación y evidencia.

Esta separación permite que el notebook no se transforme en el lugar donde se define toda la lógica del sistema. Las reglas permanecen en módulos reutilizables y el notebook se concentra en importar, ejecutar, verificar, medir e interpretar.

Los principales objetivos arquitectónicos son:

- aumentar la cohesión de cada componente;
- reducir el acoplamiento entre módulos;
- mantener trazabilidad entre F2 y F3;
- facilitar pruebas y validaciones;
- permitir la incorporación futura de nuevas transformaciones;
- evitar duplicación de lógica;
- mantener una única fuente de verdad para cada regla del proyecto;
- favorecer la reproducibilidad del procesamiento.

---

# 2. Continuidad entre F2 y F3

F3 no reemplaza el procesamiento implementado durante F2.

Las funciones desarrolladas y validadas previamente continúan resolviendo las principales reglas de transformación. La diferencia fundamental es que F3 agrega una capa de coordinación orientada a objetos y componentes dedicados al análisis algorítmico.

La continuidad esperada es:

```text
F2
│
├── funciones de carga
├── funciones de transformación
├── auditoría
├── validaciones
└── producto analítico
        │
        ▼
F3
│
├── reutiliza funciones F2
├── incorpora clases Transformador
├── incorpora PipelineSIMCE
├── incorpora recursividad
├── compara implementaciones
├── mide tiempo y memoria
├── analiza sensibilidad
└── documenta la arquitectura
```

Una condición fundamental de la refactorización es preservar las decisiones metodológicas.

La ejecución registrada mantiene:

- **7.143 registros de origen**;
- **6.524 establecimientos efectivos**;
- **619 registros no efectivos conservados para auditoría**;
- **30 variables en el producto analítico final**;
- **346 comunas en la dimensión geográfica**.

Por lo tanto:

```text
7.143 registros originales
        =
6.524 registros efectivos
        +
619 registros auditados
```

Esta reconciliación permite verificar que la reorganización del código no produjo pérdidas silenciosas de observaciones.

---

# 3. Estructura del repositorio

La estructura principal utilizada por F3 es:

```text
f1_s01_evaluacion_entregable_grupo7/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .mailmap
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
│   ├── __init__.py
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
│   ├── __init__.py
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
│
└── Minutas/
```

La estructura separa explícitamente:

```text
notebooks       → ejecución y evidencia
src/            → implementación reutilizable
tests/          → pruebas automatizadas
docs/           → documentación técnica
data/raw/       → fuente
data/processed/ → productos derivados
```

---

# 4. Capas lógicas del sistema

La arquitectura puede entenderse mediante cuatro capas principales.

## 4.1. Capa de datos

Incluye:

```text
data/raw/
data/processed/
```

`data/raw/` conserva la fuente utilizada por el proyecto.

`data/processed/` contiene los productos derivados del pipeline, incluyendo el dataset analítico, auditorías y resúmenes territoriales.

---

## 4.2. Capa funcional

Se encuentra principalmente dentro de:

```text
src/configuracion.py
src/carga.py
src/diagnostico.py
src/transformacion.py
src/auditoria.py
src/validacion.py
src/exportacion.py
```

Esta capa contiene las reglas funcionales provenientes de F2.

---

## 4.3. Capa de coordinación orientada a objetos

Se implementa principalmente en:

```text
src/poo.py
```

Su responsabilidad es organizar las transformaciones mediante objetos que comparten una interfaz común.

---

## 4.4. Capa algorítmica y de evidencia

Incluye:

```text
src/algoritmo.py
src/arquitectura.py
F3/F3_Nucleo_Algoritmico.ipynb
```

Esta capa incorpora:

- recursividad;
- implementaciones alternativas;
- mediciones de eficiencia;
- generación de documentación;
- análisis de sensibilidad;
- evidencia reproducible.

---

# 5. Responsabilidades de los módulos

## 5.1. `src/configuracion.py`

Centraliza los elementos compartidos por el pipeline.

Entre sus responsabilidades se encuentran:

- definición de columnas;
- catálogos categóricos;
- claves territoriales;
- esquema final;
- nombres de archivos;
- localización de datos;
- parámetros reutilizados por distintos módulos.

La centralización evita repetir constantes en distintos archivos.

---

## 5.2. `src/carga.py`

Gestiona la carga de información requerida por el pipeline.

Entre sus responsabilidades se encuentran:

- lectura selectiva del archivo SIMCE;
- validación de las columnas necesarias;
- construcción de `DimGeografia`;
- preparación de la información territorial necesaria para el enriquecimiento posterior.

La dimensión geográfica utilizada por el proyecto contiene:

```text
346 comunas
```

---

## 5.3. `src/diagnostico.py`

Agrupa operaciones destinadas a inspeccionar el estado inicial de los datos y generar evidencia diagnóstica.

Permite mantener separada la exploración de las transformaciones que modifican el DataFrame.

---

## 5.4. `src/transformacion.py`

Contiene las principales reglas de transformación utilizadas por el pipeline.

Entre sus funciones se encuentran:

```text
convertir_tipos()
limpiar_textos()
agregar_categorias()
agregar_geografia()
clasificar_efectividad()
construir_dataset_final()
construir_cobertura_regional()
```

Este módulo conserva la lógica funcional validada durante F2.

---

## 5.5. `src/auditoria.py`

Mantiene trazabilidad de los registros excluidos del producto analítico.

La auditoría permite conservar información que no cumple la regla de efectividad sin eliminarla completamente del proceso.

Esto es especialmente relevante porque:

```text
619 registros
```

quedan fuera del dataset analítico principal, pero permanecen disponibles para revisión.

Dentro de ellos existen:

```text
55 registros
```

con puntaje y marca asociada, utilizados posteriormente en análisis de sensibilidad.

---

## 5.6. `src/validacion.py`

Implementa verificaciones de integridad sobre los datos.

`validar_dataset_final()` ejecuta controles relacionados con:

- dataset no vacío;
- asignatura;
- efectividad;
- número de alumnos;
- RBD;
- unicidad;
- puntaje;
- geografía;
- fecha;
- columnas duplicadas;
- reconciliación de cantidades;
- cobertura regional;
- estructura final.

En la ejecución F3 se obtienen:

```text
14 / 14 validaciones superadas
```

---

## 5.7. `src/exportacion.py`

Centraliza la persistencia de los productos generados por el procesamiento.

Separar la exportación evita que la lógica de transformación dependa directamente de las decisiones de almacenamiento.

---

## 5.8. `src/poo.py`

Contiene la arquitectura orientada a objetos de F3.

Incluye:

```text
Transformador
TransformadorTipos
TransformadorTextos
TransformadorCategorias
TransformadorGeografia
TransformadorEfectividad
PipelineSIMCE
```

---

## 5.9. `src/algoritmo.py`

Contiene los elementos específicos del núcleo algorítmico.

Incluye:

```text
aplanar_recursivo()
construir_jerarquia_geografica()
validar_geografia_recursiva()
enriquecer_geografia_merge()
enriquecer_geografia_diccionario()
medir()
```

Sus responsabilidades principales son:

- recursividad;
- estructuras jerárquicas;
- comparación de algoritmos;
- benchmarking;
- análisis temporal;
- medición de memoria.

---

## 5.10. `src/arquitectura.py`

Genera información de arquitectura directamente desde las clases reales mediante introspección.

Esto permite reducir el riesgo de mantener documentación completamente desacoplada del código.

---

# 6. Flujo operacional del pipeline

El flujo principal es:

```text
Dataset SIMCE
      │
      ▼
Carga
      │
      ▼
Conversión de tipos
      │
      ▼
Normalización de textos
      │
      ▼
Incorporación de categorías
      │
      ▼
Enriquecimiento geográfico
      │
      ▼
Clasificación de efectividad
      │
      ├───────────────┐
      ▼               ▼
Auditoría       Producto efectivo
      │               │
      └───────┬───────┘
              ▼
          Validación
              │
              ▼
       Producto analítico
```

Las cinco transformaciones principales mantienen las 7.143 filas mientras se prepara la información.

La separación entre efectivos y no efectivos ocurre posteriormente.

---

# 7. Programación orientada a objetos

## 7.1. Clase abstracta `Transformador`

La jerarquía parte de:

```python
class Transformador(ABC):

    @property
    def nombre(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def transformar(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError
```

Esta clase establece un contrato común.

Todo objeto que forme parte de la secuencia de transformación debe implementar:

```text
transformar(df)
```

---

# 8. Herencia

Las clases concretas heredan de `Transformador`.

La relación conceptual es:

```text
                    Transformador
                         │
       ┌─────────────────┼───────────────────────┐
       │                 │                       │
TransformadorTipos  TransformadorTextos  TransformadorCategorias
       │
       ├───────────────────────────────┐
       │                               │
TransformadorGeografia       TransformadorEfectividad
```

Cada clase tiene una responsabilidad concreta.

Por ejemplo:

```python
class TransformadorTipos(Transformador):

    def transformar(self, df):
        return convertir_tipos(df)
```

Esta decisión permite reutilizar las funciones validadas en F2 sin duplicar su implementación.

---

# 9. Polimorfismo

El polimorfismo se observa dentro de `PipelineSIMCE`.

El pipeline no necesita conocer el tipo concreto de cada objeto.

Ejecuta:

```python
for paso in self._pasos:
    actual = paso.transformar(actual)
```

Todos los transformadores responden al mismo mensaje:

```text
transformar()
```

pero cada uno ejecuta una operación distinta.

Esto permite incorporar en el futuro un nuevo transformador compatible sin modificar la lógica central del pipeline.

Por ejemplo:

```text
TransformadorEscalamiento
TransformadorOutliers
TransformadorFeatures
```

podrían incorporarse mientras respeten el mismo contrato.

---

# 10. Encapsulamiento

El proyecto utiliza estado interno mediante atributos como:

```text
_pasos
_registro
_dim_geografia
```

`PipelineSIMCE` almacena internamente los transformadores:

```python
self._pasos = tuple(pasos)
```

La propiedad pública no entrega directamente una estructura mutable:

```python
@property
def pasos(self):
    return tuple(p.nombre for p in self._pasos)
```

El registro también se expone mediante copias:

```python
@property
def registro(self):
    return tuple(dict(r) for r in self._registro)
```

`TransformadorGeografia` mantiene además:

```python
self._dim_geografia = dim_geografia.copy()
```

Esto reduce el riesgo de que modificaciones externas al DataFrame original alteren el estado utilizado internamente por el transformador.

En Python el prefijo `_` corresponde a una convención y no a una restricción absoluta de acceso, pero permite comunicar claramente qué atributos pertenecen al estado interno del objeto.

---

# 11. Cohesión y acoplamiento

La arquitectura intenta mantener alta cohesión.

Cada módulo posee una responsabilidad reconocible:

```text
configuracion.py   → configuración
carga.py           → entrada de datos
transformacion.py  → reglas de transformación
auditoria.py       → trazabilidad
validacion.py      → controles
poo.py             → coordinación mediante objetos
algoritmo.py       → algoritmos y mediciones
arquitectura.py    → documentación estructural
```

El bajo acoplamiento se observa especialmente en `PipelineSIMCE`, que depende del contrato `Transformador` y no de una clase concreta.

Esto permite separar:

```text
qué transformación se ejecuta
```

de:

```text
cómo se coordina la secuencia
```

---

# 12. Registro de ejecución del pipeline

`PipelineSIMCE` mantiene un registro de cada etapa.

Conceptualmente:

```python
{
    "paso": paso.nombre,
    "filas_entrada": antes,
    "filas_salida": len(actual),
    "columnas_salida": actual.shape[1],
}
```

La ejecución registrada muestra:

| Etapa | Filas entrada | Filas salida |
|---|---:|---:|
| TransformadorTipos | 7.143 | 7.143 |
| TransformadorTextos | 7.143 | 7.143 |
| TransformadorCategorias | 7.143 | 7.143 |
| TransformadorGeografia | 7.143 | 7.143 |
| TransformadorEfectividad | 7.143 | 7.143 |

Este registro permite identificar pérdidas inesperadas de observaciones durante las transformaciones.

---

# 13. Recursividad

La pauta de F3 requiere integrar programación estructurada y recursiva cuando corresponda.

La recursividad se implementa en `src/algoritmo.py`.

---

## 13.1. `aplanar_recursivo()`

Esta función recorre estructuras anidadas formadas por:

- diccionarios;
- listas;
- tuplas;
- valores escalares.

Conceptualmente:

```python
if isinstance(obj, dict):
    ...
    aplanar_recursivo(valor, nuevo_prefijo)

elif isinstance(obj, (list, tuple)):
    ...
    aplanar_recursivo(valor, nuevo_prefijo)

else:
    salida[prefijo] = obj
```

El caso base corresponde a un elemento que ya no contiene estructuras anidadas.

---

## 13.2. Jerarquía territorial

`construir_jerarquia_geografica()` genera una estructura:

```text
Región
 └── Provincia
      └── Comunas
```

Conceptualmente:

```text
{
    "Región A": {
        "Provincia A": [
            "Comuna 1",
            "Comuna 2"
        ]
    }
}
```

---

## 13.3. `validar_geografia_recursiva()`

La función recorre esta estructura sin depender de una cantidad fija de niveles.

Conceptualmente:

```python
def validar_geografia_recursiva(estructura, ruta="raiz"):

    if isinstance(estructura, dict):
        for clave, valor in estructura.items():
            validar_geografia_recursiva(valor)

    elif isinstance(estructura, colección):
        for valor in estructura:
            validar_geografia_recursiva(valor)

    else:
        # caso base
```

En la ejecución guardada se obtienen:

```text
Errores jerarquía: []
Comunas recorridas: 346
```

---

# 14. Complejidad de la recursividad

Si `n` representa la cantidad total de nodos visitados:

```text
Complejidad temporal ≈ O(n)
```

Cada nodo debe inspeccionarse una vez.

La memoria asociada a la pila depende de la profundidad máxima `h`:

```text
Complejidad espacial de pila ≈ O(h)
```

En la estructura territorial utilizada por el proyecto la profundidad es reducida:

```text
Región → Provincia → Comuna
```

por lo que la recursividad no representa un riesgo significativo para el tamaño actual del problema.

---

# 15. Enriquecimiento geográfico

Una de las operaciones analizadas durante F3 corresponde al enriquecimiento territorial de los establecimientos.

Se comparan dos implementaciones funcionalmente equivalentes.

---

## 15.1. Implementación mediante `pandas.merge`

```python
df.merge(
    dim,
    how="left",
    on=CLAVES_GEO,
    validate="many_to_one",
)
```

Esta es la implementación utilizada finalmente por el pipeline.

---

## 15.2. Implementación mediante diccionario

La segunda alternativa construye una estructura:

```text
clave geográfica compuesta
             ↓
(región, provincia, comuna)
             ↓
información territorial
```

Conceptualmente:

```python
lookup = {
    clave_compuesta: valores_geograficos
}
```

Posteriormente se realiza una búsqueda por establecimiento.

---

# 16. Equivalencia funcional

Antes de comparar rendimiento se comprueba que ambas implementaciones produzcan resultados equivalentes.

El notebook utiliza:

```python
assert_frame_equal(
    merge_result.sort_index(axis=1),
    dict_result.sort_index(axis=1),
    check_dtype=False,
)
```

La ejecución registrada informa:

```text
Equivalencia merge vs diccionario: OK
```

Este paso es fundamental.

Una alternativa no puede considerarse una optimización válida únicamente porque sea más rápida si modifica el resultado esperado.

Por esa razón el orden metodológico es:

```text
1. comprobar equivalencia
2. medir eficiencia
3. interpretar
4. seleccionar
```

---

# 17. Medición reproducible de eficiencia

La función:

```text
medir()
```

se encuentra en:

```text
src/algoritmo.py
```

y utiliza dos herramientas principales.

---

## 17.1. Tiempo

Se utiliza:

```python
time.perf_counter()
```

para obtener un reloj de alta resolución adecuado para mediciones de duración.

---

## 17.2. Memoria

Se utiliza:

```python
tracemalloc
```

para registrar el pico de memoria asignada por Python durante cada ejecución.

---

## 17.3. Repeticiones

Las mediciones se ejecutan varias veces.

La función retorna información como:

```text
tiempo_promedio_s
tiempo_min_s
memoria_pico_promedio_mb
resultado
```

Esto reduce la dependencia de una única observación temporal.

---

# 18. Validación `many_to_one`

El enriquecimiento geográfico utiliza:

```python
validate="many_to_one"
```

Esta opción establece que cada clave presente en los establecimientos puede relacionarse con como máximo una fila de la dimensión geográfica.

Su objetivo es impedir que una dimensión con claves duplicadas provoque una multiplicación silenciosa de registros.

Durante F3 se genera deliberadamente una dimensión con una clave duplicada.

La ejecución produce:

```text
Duplicado detectado correctamente: MergeError
```

Esto demuestra que la validación cumple una función de integridad real.

---

# 19. Costo de la validación

La comprobación `many_to_one` introduce un sobrecosto temporal respecto de realizar el `merge` sin validar cardinalidad.

En la última ejecución actualmente guardada en el notebook se observa aproximadamente:

```text
validate=False → 0,0066 s
validate=True  → 0,0083 s
```

con un sobrecosto temporal cercano al:

```text
25 %
```

Los valores exactos pueden variar entre ejecuciones porque dependen del sistema operativo, carga del equipo, asignación de memoria y entorno de ejecución.

Por esta razón, la arquitectura no depende de un valor puntual de benchmark.

La conclusión relevante es:

```text
el costo absoluto es pequeño para el tamaño actual del dataset
y la garantía de integridad justifica conservar la validación.
```

---

# 20. Crecimiento con el tamaño

La eficiencia no se analiza únicamente sobre el dataset completo.

El notebook mide distintos tamaños:

```text
500 registros
2.000 registros
7.143 registros
```

La ejecución actualmente guardada muestra que `pandas.merge` mantiene tiempos inferiores a la implementación basada en iteración Python mediante diccionario.

El objetivo de estas mediciones no es extrapolar el comportamiento hacia millones de observaciones, sino comprobar que la comparación no dependa de una única muestra.

---

# 21. Complejidad temporal

Para la implementación mediante diccionario se requiere:

1. construir un índice sobre `m` registros geográficos;
2. realizar aproximadamente una búsqueda por cada uno de los `n` establecimientos.

De manera simplificada:

```text
O(m + n)
```

En el proyecto:

```text
m = 346 comunas
n = 7.143 establecimientos
```

La implementación mediante `pandas.merge` se ejecuta internamente mediante algoritmos optimizados de pandas.

Dado que los detalles concretos de implementación pueden variar según versiones y tipos de datos, la decisión final no se fundamenta en asumir una complejidad interna específica que no sea controlada directamente por el proyecto.

Se utiliza evidencia empírica complementada con garantías funcionales.

---

# 22. Complejidad espacial

Ambas implementaciones requieren estructuras auxiliares.

La alternativa de diccionario construye explícitamente:

```text
lookup
lista de claves
lista de valores encontrados
DataFrame enriquecido
```

La solución basada en `merge` también requiere memoria para construir el resultado de la unión.

Por lo tanto, la selección no se basa solamente en complejidad temporal, sino también en:

- legibilidad;
- mantenibilidad;
- integridad;
- tiempo observado;
- uso de memoria;
- comportamiento esperado.

---

# 23. Selección final del algoritmo

Para el tamaño actual del proyecto se mantiene:

```python
pandas.merge(
    ...,
    validate="many_to_one",
)
```

La decisión se fundamenta en:

- equivalencia comprobada;
- menor tiempo observado frente a la alternativa implementada;
- comportamiento consistente en distintos tamaños;
- sintaxis clara;
- integración natural con DataFrames;
- validación explícita de cardinalidad;
- detección de errores mediante `MergeError`.

La optimización no elimina controles de integridad con el único objetivo de reducir unos milisegundos.

---

# 24. Preprocesamiento

F3 conserva el enfoque conservador definido en F2.

---

## 24.1. Conversión de tipos

`convertir_tipos()` utiliza conversión explícita sobre las columnas numéricas.

Si un valor no nulo no puede ser convertido correctamente, el pipeline genera una excepción.

Esto evita convertir silenciosamente errores de datos en valores faltantes.

---

## 24.2. Fecha

`fecha_bbdd` se transforma utilizando el formato esperado:

```text
YYYYMMDD
```

Una fecha inválida detiene la ejecución.

---

## 24.3. Textos

`limpiar_textos()`:

- elimina caracteres de control;
- consolida espacios;
- elimina espacios iniciales y finales;
- convierte cadenas vacías en valores faltantes.

La operación busca consistencia técnica sin modificar el significado del contenido.

---

## 24.4. Categorías

Antes de realizar mapeos categóricos se comprueba que los códigos pertenezcan a los catálogos documentados.

Un código desconocido produce:

```text
ValueError
```

en lugar de ser aceptado silenciosamente.

---

# 25. Regla de efectividad

La regla metodológica se conserva desde F2.

Un establecimiento se clasifica como efectivo cuando:

```text
número de alumnos evaluados > 0
```

y:

```text
no existe observación asociada al puntaje
```

Los registros restantes se clasifican como:

```text
No Efectiva
```

y se conserva el motivo de exclusión.

Esta decisión permite mantener separado:

```text
producto analítico
```

de:

```text
auditoría de registros excluidos
```

---

# 26. Validación técnica

La validación utiliza distintas capas complementarias:

```text
validaciones del dataset
+
pruebas automatizadas
+
assert del notebook
+
pruebas deliberadas de excepción
```

---

# 27. Validaciones integradas

`validar_dataset_final()` contiene 14 controles.

Entre ellos:

1. dataset final no vacío;
2. asignatura correcta;
3. efectividad correcta;
4. alumnos mayores que cero;
5. RBD no nulo;
6. RBD único;
7. puntaje disponible;
8. geografía completa;
9. fecha válida;
10. ausencia de columnas duplicadas;
11. reconciliación bruto = final + auditoría;
12. cobertura regional respecto del bruto;
13. cobertura regional respecto del producto final;
14. ausencia de variables retiradas del alcance.

La ejecución almacenada reporta:

```text
Validaciones F2/F3: 14 / 14
```

---

# 28. Pruebas automatizadas

La suite automatizada real se encuentra en:

```text
tests/test_regla_efectividad.py
```

Contiene cinco pruebas.

---

## 28.1. Caso normal

Comprueba que un establecimiento válido sea clasificado como:

```text
Efectiva
```

---

## 28.2. Caso límite

Comprueba el comportamiento cuando:

```text
número de alumnos = 0
```

El resultado debe ser:

```text
No Efectiva
```

---

## 28.3. Registro con observación

Comprueba que un establecimiento con observación asociada al puntaje no sea incorporado como efectivo.

---

## 28.4. Marca 2 con puntaje

Comprueba que la existencia de un puntaje no invalide automáticamente la regla metodológica de exclusión cuando existe una marca asociada.

---

## 28.5. Código desconocido

Introduce:

```text
marca_mate4b_rbd = 99
```

y verifica que el sistema genere:

```text
ValueError
```

---

# 29. Verificaciones complementarias del notebook

Las pruebas automatizadas de `tests/` se complementan mediante controles ejecutados directamente dentro del notebook.

Entre ellos se encuentran:

- dimensión geográfica = 346 comunas;
- ausencia de duplicados en la clave territorial;
- continuidad 7.143 → 6.524 + 619;
- validez de la jerarquía recursiva;
- equivalencia entre `merge` y diccionario;
- detección de una dimensión inválida mediante `MergeError`;
- existencia de los archivos requeridos para F3;
- estado correcto de la suite automatizada;
- existencia de documentación de arquitectura.

Es importante distinguir ambos niveles:

```text
tests/
→ suite automatizada formal

notebook
→ asserts y comprobaciones de integración
```

---

# 30. Verificación estructural de F3

El notebook verifica explícitamente la existencia de:

```text
src/poo.py
src/algoritmo.py
src/arquitectura.py
tests/test_regla_efectividad.py
docs/arquitectura_f3.md
```

La ejecución almacenada reporta:

```text
OK - src\poo.py
OK - src\algoritmo.py
OK - src\arquitectura.py
OK - tests\test_regla_efectividad.py
OK - docs\arquitectura_f3.md

Estructura F3 verificada correctamente.
```

---

# 31. Verificación final

La última celda del notebook mantiene un conjunto de verificaciones mínimas:

```text
Fuente cargada
346 comunas
Producto final no vacío
Continuidad 6524 efectivos
619 excluidos auditados
Jerarquía recursiva válida
Suite de tests OK
Arquitectura documentada
```

La ejecución final utiliza:

```python
assert all(checks.values())
```

Por lo tanto, si uno de estos controles falla, el notebook no debe considerarse correctamente ejecutado.

La ejecución almacenada finaliza con:

```text
F3 verificada: notebook reproducible y núcleo modular operativo.
```

---

# 32. Análisis de sensibilidad

F3 mantiene la regla metodológica definida por el proyecto, pero incorpora escenarios experimentales para medir su impacto.

Se analizan tres escenarios.

---

## Escenario A

```text
Solo establecimientos efectivos
```

Cantidad:

```text
6.524
```

Media observada:

```text
≈ 254,6971
```

---

## Escenario B

```text
Todos los registros que conservan puntaje
```

Cantidad:

```text
6.579
```

Media observada:

```text
≈ 254,7348
```

---

## Escenario C

```text
Efectivos + registros marca 2 con puntaje
```

Cantidad:

```text
6.579
```

Media observada:

```text
≈ 254,7348
```

---

# 33. Interpretación de sensibilidad

La diferencia entre los escenarios B y A es aproximadamente:

```text
0,0376 puntos
```

Además, en el análisis regional la mayor diferencia absoluta observada es aproximadamente:

```text
0,3857 puntos
```

en Arica y Parinacota.

Estos resultados muestran que la inclusión experimental de los 55 registros no efectivos que conservan puntaje produce cambios descriptivos pequeños en las medias observadas.

Sin embargo, este ejercicio no modifica el criterio oficial del pipeline.

Su función es:

```text
evaluar sensibilidad
```

y no:

```text
reincorporar automáticamente registros excluidos.
```

---

# 34. Normalización y escalamiento

F3 no aplica escalamiento automático a las variables numéricas.

La decisión se fundamenta en el tipo de operaciones realizadas actualmente.

El núcleo utiliza principalmente:

- comparaciones lógicas;
- reglas de negocio;
- mapeos;
- joins;
- validaciones;
- agregaciones;
- auditoría.

Estas operaciones no requieren variables expresadas en una escala común.

---

# 35. Conservación de unidades

El puntaje SIMCE mantiene su escala original.

En la ejecución almacenada se observa aproximadamente:

```text
prom_mate4b_rbd

mínimo ≈ 152
media   ≈ 254,73
máximo ≈ 341
```

También se conserva `nalu_mate4b_rbd` en su unidad original.

Esto favorece la interpretación.

---

# 36. Cuándo se justificaría escalar

Una futura etapa debería reconsiderar esta decisión si utiliza algoritmos sensibles a magnitudes o distancias, por ejemplo:

```text
KNN
K-Means
SVM
redes neuronales
otros modelos sensibles a escala
```

En ese escenario el escalamiento debería incorporarse como una transformación claramente documentada y, cuando corresponda a aprendizaje automático, ajustarse únicamente utilizando el conjunto de entrenamiento para evitar fuga de información.

---

# 37. Documentación generada desde código

`src/arquitectura.py` utiliza introspección sobre las clases reales.

La función:

```text
tabla_arquitectura()
```

obtiene información como:

- nombre de clase;
- clase base;
- responsabilidad;
- métodos públicos;
- módulo.

Esto permite generar una tabla directamente desde la implementación.

La idea es reducir el riesgo de mantener documentación con nombres de clases o métodos que hayan dejado de existir.

---

# 38. Arquitectura de clases

La arquitectura actual puede representarse conceptualmente como:

```text
                   ┌───────────────────┐
                   │   Transformador   │
                   │      (ABC)        │
                   └─────────┬─────────┘
                             │
          ┌──────────────────┼───────────────────┐
          │                  │                   │
          ▼                  ▼                   ▼
TransformadorTipos  TransformadorTextos  TransformadorCategorias
          │
          ├───────────────────────┐
          ▼                       ▼
TransformadorGeografia   TransformadorEfectividad


                   ┌─────────────────┐
                   │  PipelineSIMCE  │
                   └────────┬────────┘
                            │
                            ▼
               coordina Transformadores
```

La relación principal de `PipelineSIMCE` con los transformadores es de:

```text
composición
```

mientras que entre `Transformador` y sus implementaciones existe:

```text
herencia
```

---

# 39. Relación entre funciones y objetos

F3 no duplica la lógica funcional dentro de las clases.

Por ejemplo:

```text
TransformadorTipos
        │
        ▼
convertir_tipos()
```

```text
TransformadorTextos
        │
        ▼
limpiar_textos()
```

```text
TransformadorCategorias
        │
        ▼
agregar_categorias()
```

```text
TransformadorGeografia
        │
        ▼
agregar_geografia()
```

```text
TransformadorEfectividad
        │
        ▼
clasificar_efectividad()
```

Esta estrategia permite aprovechar las reglas verificadas en F2 y utilizar POO como mecanismo de coordinación, no como excusa para duplicar implementación.

---

# 40. Evolución arquitectónica F2 → F3

| Aspecto | F2 | F3 |
|---|---|---|
| Organización | Funciones modulares | Funciones + objetos |
| Transformaciones | Funciones | Objetos `Transformador` que reutilizan funciones |
| Coordinación | Flujo funcional | `PipelineSIMCE` |
| Reutilización | Módulos `src` | Módulos + contrato común |
| Recursividad | No central | Aplicada a estructuras jerárquicas |
| Benchmarks | No constituyen eje principal | Comparación formal de implementaciones |
| Tiempo | Sin benchmark central | `perf_counter()` |
| Memoria | Sin benchmark central | `tracemalloc` |
| Integridad geográfica | Join validado | Join + análisis costo/beneficio |
| Sensibilidad | Diagnóstico previo | Escenarios formalmente comparados |
| Arquitectura | Modular funcional | Modular + POO |
| Documentación | Código/notebook | Código + notebook + arquitectura |

---

# 41. Escalabilidad del diseño

La arquitectura permite incorporar nuevos componentes sin modificar completamente el pipeline.

Una extensión futura podría implementar:

```python
class TransformadorNuevo(Transformador):

    def transformar(self, df):
        ...
        return resultado
```

y luego incorporarse en:

```python
PipelineSIMCE([
    TransformadorTipos(),
    TransformadorTextos(),
    TransformadorNuevo(),
    ...
])
```

El pipeline seguiría funcionando utilizando la interfaz común.

---

# 42. Sostenibilidad del diseño

La arquitectura intenta evitar dos extremos:

```text
un notebook monolítico
```

y:

```text
una arquitectura innecesariamente compleja
```

No se agregan patrones únicamente para aumentar la sofisticación aparente.

Las decisiones utilizadas responden a necesidades concretas:

- clase abstracta → contrato común;
- herencia → especialización;
- polimorfismo → ejecución uniforme;
- encapsulamiento → protección del estado interno;
- composición → construcción flexible del pipeline;
- módulos → separación de responsabilidades.

---

# 43. Reproducibilidad

La primera celda del notebook detecta la raíz del proyecto.

Esto permite ejecutar el notebook tanto desde:

```text
raíz/
```

como desde:

```text
F3/
```

sin codificar una ruta absoluta personal como requisito del sistema.

Posteriormente incorpora la raíz al `sys.path` para permitir importaciones desde `src`.

---

# 44. Entorno registrado

La ejecución actual del notebook registra las versiones utilizadas.

Entre ellas:

```text
Python 3.14.7
pandas 3.0.5
NumPy 2.5.2
```

Las dependencias del proyecto se encuentran declaradas en:

```text
requirements.txt
```

---

# 45. Orden reproducible de ejecución

La continuidad del proyecto se organiza mediante:

```text
1. F1/F1_Definicion.ipynb
2. F2/F2_Preprocesamiento.ipynb
3. F3/F3_Nucleo_Algoritmico.ipynb
```

Para verificar F3 se recomienda:

```text
Restart Kernel
↓
Run All Cells
↓
guardar notebook
```

La versión almacenada en el repositorio mantiene las 16 celdas de código ejecutadas secuencialmente.

---

# 46. README y trazabilidad

El `README.md` documenta:

- propósito del proyecto;
- integrantes;
- estructura;
- dependencias;
- configuración del entorno;
- orden de ejecución;
- F2;
- F3;
- POO;
- algoritmos;
- recursividad;
- eficiencia;
- arquitectura;
- sensibilidad;
- contribuciones individuales;
- commits representativos.

De esta manera el README funciona como punto de entrada técnico al repositorio.

---

# 47. Control de versiones

El proyecto se mantiene bajo Git y GitHub.

La evolución de F3 se distribuye en múltiples commits vinculados con:

- creación del notebook;
- POO;
- algoritmos;
- recursividad;
- pruebas;
- eficiencia;
- sensibilidad;
- documentación;
- correcciones;
- reproducibilidad.

Esto permite observar una evolución incremental en lugar de una única carga final.

---

# 48. Identidades Git

El archivo:

```text
.mailmap
```

documenta y normaliza las identidades utilizadas por los integrantes durante el desarrollo.

Esto resulta especialmente relevante cuando una persona ha realizado commits desde distintos equipos o configuraciones locales de Git.

`.mailmap` no modifica los hashes ni reescribe el historial.

Su objetivo es mejorar la presentación y trazabilidad de identidades en herramientas compatibles con Git mailmap.

---

# 49. Principios de diseño aplicados

## Responsabilidad única

Cada módulo se concentra en un dominio específico.

## Alta cohesión

Funciones relacionadas se agrupan dentro del mismo módulo.

## Bajo acoplamiento

Los componentes dependen de interfaces y funciones específicas en lugar de concentrar toda la lógica en un único archivo.

## Reutilización

Las clases de F3 reutilizan las funciones verificadas en F2.

## Separación de evidencia e implementación

El notebook documenta y coordina, mientras `src/` contiene la lógica reutilizable.

## Fallo explícito

Cuando se detecta una condición incompatible con los supuestos del proyecto se utilizan:

```text
ValueError
AssertionError
MergeError
```

en lugar de continuar silenciosamente.

---

# 50. Decisiones deliberadamente no adoptadas

La arquitectura evita introducir componentes que no resuelvan una necesidad concreta.

No se incorporan:

- múltiples capas abstractas innecesarias;
- patrones de diseño artificiales;
- escalamiento sin necesidad algorítmica;
- imputaciones arbitrarias;
- eliminación automática de valores extremos;
- optimizaciones que reduzcan integridad;
- duplicación de reglas F2 dentro de F3.

El objetivo es mantener el sistema comprensible.

---

# 51. Limitaciones actuales

La arquitectura actual corresponde a un proyecto académico en evolución y no pretende constituir una plataforma productiva de procesamiento masivo.

Entre sus límites se encuentran:

- volumen de datos relativamente acotado;
- ejecución local;
- persistencia principalmente mediante archivos;
- ausencia de una base de datos transaccional;
- ausencia de procesamiento distribuido;
- ausencia de entrenamiento de modelos predictivos en esta fase;
- benchmarks dependientes del entorno de ejecución.

Por esta razón los tiempos obtenidos deben interpretarse como evidencia comparativa dentro del entorno utilizado, no como garantías universales de rendimiento.

---

# 52. Extensiones futuras

La estructura actual permite incorporar posteriormente:

- ingeniería de variables;
- escalamiento;
- análisis estadístico;
- modelos de aprendizaje automático;
- validación de modelos;
- nuevos transformadores;
- nuevas fuentes territoriales;
- persistencia en base de datos;
- automatización del pipeline;
- integración continua;
- nuevas pruebas automatizadas.

Estas extensiones pueden incorporarse sin trasladar nuevamente toda la lógica al notebook.

---

# 53. Trazabilidad completa

La relación esperada entre componentes es:

```text
Problema
  │
  ▼
F1
  │
  ▼
Definición del dataset
  │
  ▼
F2
  │
  ├── carga
  ├── limpieza
  ├── transformación
  ├── auditoría
  └── validación
  │
  ▼
F3
  │
  ├── POO
  ├── recursividad
  ├── eficiencia
  ├── sensibilidad
  └── documentación
  │
  ▼
Producto analítico
```

Cada decisión relevante puede rastrearse entre:

```text
informe
↕
notebook
↕
src/
↕
tests/
↕
docs/
↕
historial Git
```

---

# 54. Correspondencia con la Fase 3

La arquitectura implementada responde a los componentes centrales solicitados para F3.

## Programación estructurada

Se conserva mediante funciones y módulos reutilizables.

## Programación recursiva

Se implementa mediante las funciones de recorrido de estructuras anidadas y validación territorial.

## Programación orientada a objetos

Se implementa mediante:

```text
Transformador
subclases especializadas
PipelineSIMCE
```

## Eficiencia

Se evalúa mediante:

```text
perf_counter
tracemalloc
comparación de implementaciones
múltiples tamaños
repeticiones
```

## Validación

Se implementa mediante:

```text
14 validaciones integradas
5 pruebas automatizadas
asserts
pruebas deliberadas de excepción
```

## Reproducibilidad

Se mantiene mediante:

```text
requirements.txt
detección automática de PROJECT_ROOT
notebook ejecutado
README
estructura Git
```

---

# 55. Síntesis arquitectónica

La Fase 3 transforma el pipeline funcional de F2 en una estructura modular orientada a objetos sin abandonar las reglas que ya habían sido verificadas.

La arquitectura final separa:

```text
reglas
coordinación
validación
algoritmos
documentación
evidencia
```

La lógica funcional permanece reutilizable.

`PipelineSIMCE` coordina transformadores mediante polimorfismo.

La recursividad se utiliza sobre una estructura territorial real.

La eficiencia se evalúa mediante implementaciones equivalentes antes de seleccionar una solución.

Las pruebas automatizadas y los controles del notebook verifican distintos niveles del sistema.

La documentación de arquitectura se complementa con introspección desde el propio código.

El resultado es una estructura diseñada para ser:

- comprensible;
- reproducible;
- verificable;
- modular;
- mantenible;
- extensible;
- coherente con el desarrollo previo del proyecto.

---

# 56. Decisión arquitectónica final

La principal decisión de F3 puede resumirse como:

> Mantener las reglas funcionales validadas en F2 como fuente de verdad y construir sobre ellas una capa de coordinación orientada a objetos, acompañada de recursividad pertinente, validación sistemática, análisis de eficiencia y documentación trazable.

Esta estrategia permite mejorar la arquitectura sin introducir cambios innecesarios en los resultados del procesamiento.

La evidencia obtenida confirma que la reorganización mantiene:

```text
7.143 registros originales
6.524 registros efectivos
619 registros auditados
346 comunas
14/14 validaciones
5/5 pruebas automatizadas
16/16 celdas de código ejecutadas
```

y finaliza con una verificación explícita de que el núcleo modular se encuentra operativo.

---

# 57. Referencias técnicas utilizadas

La arquitectura y las decisiones técnicas se apoyan en las fuentes utilizadas por el informe de F3, entre ellas:

- documentación oficial de Python para `time.perf_counter`;
- documentación oficial de Python para `tracemalloc`;
- documentación oficial de pandas para `DataFrame.merge`;
- documentación de Jupyter;
- documentación de Git;
- material docente de MCDI500;
- literatura académica reciente sobre reproducibilidad de notebooks.

Las referencias bibliográficas completas se encuentran en el informe institucional de Fase 3.

---

**Documento:** Arquitectura del proyecto — Fase 3  
**Grupo:** 7  
**Asignatura:** MCDI500 — Programación para la Ciencia de Datos