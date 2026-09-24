# Arquitectura del proyecto — Fase 3

## 1. Propósito de la arquitectura

La Fase 3 reorganiza el pipeline validado en F2 hacia una arquitectura modular y orientada a objetos, manteniendo las reglas metodológicas ya definidas para el procesamiento de resultados SIMCE de Matemática de 4.º Básico 2025.

La lógica reutilizable se mantiene en `src/`, mientras que `F3/F3_Nucleo_Algoritmico.ipynb` funciona como capa de orquestación, ejecución, medición y evidencia.

El objetivo de esta organización es mejorar la mantenibilidad, trazabilidad y extensibilidad del proyecto sin modificar arbitrariamente el comportamiento validado en F2.

---

## 2. Estructura del proyecto

```text
proyecto/
├── F1/
├── F2/
│   └── F2_Preprocesamiento.ipynb
├── F3/
│   ├── F3_Nucleo_Algoritmico.ipynb
│   └── NucleoF3.md
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
├── tests/
│   ├── __init__.py
│   └── test_regla_efectividad.py
├── docs/
│   └── arquitectura_f3.md
└── data/
    ├── raw/
    └── processed/