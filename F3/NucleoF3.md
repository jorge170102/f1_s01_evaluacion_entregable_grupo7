# Fase 3 — Núcleo algorítmico, eficiencia y POO

Esta fase conserva la lógica validada en F2 y cambia la arquitectura: la implementación reutilizable vive en `src/`, mientras el notebook F3 actúa como orquestador, evidencia y documento ejecutable.

## Componentes nuevos
- `src/poo.py`: jerarquía `Transformador`, transformadores concretos y `PipelineSIMCE`.
- `src/algoritmos.py`: recursividad, implementaciones alternativas del enriquecimiento geográfico y medición de tiempo/memoria.
- `src/arquitectura.py`: tabla de arquitectura generada desde las clases reales.
- `tests/test_f3.py`: pruebas de POO, recursividad, equivalencia y cardinalidad.
- `F3/F3_Nucleo_Algoritmico_SIMCE.ipynb`: notebook ejecutable de evidencia.

## Ejecución
Desde la raíz del repositorio, abrir el notebook F3, reiniciar kernel y ejecutar todas las celdas. Las pruebas también pueden ejecutarse con `python -m unittest discover -s tests -p "test_*.py" -v`.

## Decisiones
Se usa herencia solo para expresar un contrato común de transformación y polimorfismo en el pipeline. La recursividad se aplica a metadatos/configuraciones anidadas, donde la profundidad no está fijada. La comparación de eficiencia enfrenta `pandas.merge` y un diccionario de clave compuesta y mide también el costo de `validate="many_to_one"`.