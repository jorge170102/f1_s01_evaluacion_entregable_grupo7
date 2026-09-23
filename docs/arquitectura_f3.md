# Arquitectura del proyecto — Fase 3

## 1. Descripción general

Durante la Fase 3, el pipeline desarrollado y validado en la Fase 2
evoluciona hacia una arquitectura modular orientada a objetos.

La lógica reutilizable del proyecto se mantiene dentro de `src/`,
mientras que el notebook de Fase 3 se utiliza para integrar los
componentes, ejecutar el procesamiento, realizar mediciones de
eficiencia y documentar los resultados.

Esta separación permite evitar duplicación de código y mantener una
estructura más organizada, mantenible y extensible.

## 2. Estructura del proyecto

```text
proyecto/
├── F1/
├── F2/
│   └── F2_Preprocesamiento.ipynb
├── F3/
│   └── F3_Nucleo_Algoritmico.ipynb
├── src/
│   ├── configuracion.py
│   ├── carga.py
│   ├── diagnostico.py
│   ├── transformacion.py
│   ├── auditoria.py
│   ├── validacion.py
│   ├── exportacion.py
│   ├── poo.py
│   └── algoritmos.py
├── tests/
└── docs/
    └── arquitectura_f3.md