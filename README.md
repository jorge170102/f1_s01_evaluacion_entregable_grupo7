# Caracterización e Inequidad en los Resultados Académicos del SIMCE 4º Básico en Chile

**Grupo:** Grupo 7

## Integrantes
- Felipe Palma Barrientos
- Vicente Aguilar Rojas
- Cristian Grandon Grandon
- Jorge Gutierrez Jaramillo

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
- `F1/`: definición del proyecto.
- `F2/`: preparación y procesamiento de datos.
- `F3/` y `F4/`: fases posteriores.

## Requisitos

Python: 3.10.8

### Dependencias
- ipykernel
- jupyterlab
- matplotlib==3.10.9
- notebook
- numpy==2.2.6
- pandas==2.3.3
- seaborn==0.13.2

## Reproducibilidad

La semilla utilizada durante el proyecto es `42`.

Los datos originales no se modifican durante la Fase 1.
