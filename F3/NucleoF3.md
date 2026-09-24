# Fase 3 — Núcleo algorítmico, eficiencia y POO

Esta fase conserva la lógica funcional validada en F2 y evoluciona la arquitectura del proyecto hacia una solución modular orientada a objetos.

La implementación reutilizable permanece en `src/`, mientras que `F3/F3_Nucleo_Algoritmico.ipynb` actúa como punto de integración, ejecución, medición y evidencia.

## Componentes principales

- `src/poo.py`: clase abstracta `Transformador`, transformadores concretos y `PipelineSIMCE`.
- `src/algoritmo.py`: recursividad, enriquecimiento geográfico mediante implementaciones alternativas y medición de tiempo/memoria.
- `src/arquitectura.py`: generación de documentación de arquitectura mediante introspección.
- `tests/test_regla_efectividad.py`: pruebas automatizadas de reglas críticas de efectividad y validación de categorías.
- `docs/arquitectura_f3.md`: documentación técnica detallada de la arquitectura y decisiones implementadas.
- `F3/F3_Nucleo_Algoritmico.ipynb`: notebook ejecutable que integra POO, recursividad, validación, eficiencia y análisis de sensibilidad.

## Flujo

El procesamiento sigue la secuencia:

`carga → tipos → textos → categorías → geografía → efectividad → auditoría/validación → producto final`

La arquitectura F3 reutiliza las funciones desarrolladas en F2 y coordina las principales transformaciones mediante objetos con una interfaz común.

## Programación orientada a objetos

`Transformador` define el contrato `transformar(df)`.

Las clases concretas son:

- `TransformadorTipos`
- `TransformadorTextos`
- `TransformadorCategorias`
- `TransformadorGeografia`
- `TransformadorEfectividad`

`PipelineSIMCE` ejecuta estos componentes mediante polimorfismo y mantiene un registro de cada etapa.

## Recursividad

`src/algoritmo.py` incorpora:

- `aplanar_recursivo()`
- `construir_jerarquia_geografica()`
- `validar_geografia_recursiva()`

La recursividad se aplica a estructuras anidadas y a la jerarquía territorial Región → Provincia → Comuna.

## Eficiencia

Se comparan dos implementaciones del enriquecimiento territorial:

1. `pandas.merge(..., validate="many_to_one")`
2. búsqueda mediante diccionario de clave geográfica compuesta.

Antes de medir rendimiento se comprueba la equivalencia funcional entre ambas implementaciones.

Las mediciones utilizan:

- `time.perf_counter()` para tiempo;
- `tracemalloc` para memoria pico;
- múltiples repeticiones;
- diferentes tamaños del dataset.

También se analiza el costo de `validate="many_to_one"` y se comprueba su utilidad provocando deliberadamente una violación de cardinalidad.

## Validación

La validación se realiza mediante dos niveles complementarios:

- pruebas automatizadas disponibles en `tests/test_regla_efectividad.py`;
- verificaciones de integración y `assert` ejecutados dentro del notebook F3.

La ejecución registrada mantiene:

- 7.143 registros de origen;
- 6.524 registros efectivos;
- 619 registros auditados;
- 346 comunas;
- 14/14 validaciones del dataset;
- 5/5 pruebas automatizadas.

## Ejecución

Desde la raíz del repositorio:

1. seleccionar el entorno declarado en `requirements.txt`;
2. abrir `F3/F3_Nucleo_Algoritmico.ipynb`;
3. reiniciar el kernel;
4. ejecutar todas las celdas;
5. guardar las salidas.

Las pruebas también pueden ejecutarse mediante:

```bash
python -m unittest discover -s tests -p "test_*.py" -v