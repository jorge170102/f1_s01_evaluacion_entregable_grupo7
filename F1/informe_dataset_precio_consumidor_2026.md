# Validación del dataset — MCDI500

**Archivo:** `precio_consumidor_2026.csv` · 221432 filas × 15 columnas

## Perfil de variables

| variable | dtype | rol | unicos | pct_nulos |
| --- | --- | --- | --- | --- |
| ﻿"Anio" | int64 | discreta | 1 | 0.0 |
| Mes | int64 | discreta | 9 | 0.0 |
| Semana | int64 | discreta | 36 | 0.0 |
| Fecha inicio | str | fecha | 36 | 0.0 |
| Fecha termino | str | fecha | 36 | 0.0 |
| ID region | int64 | discreta | 9 | 0.0 |
| Region | str | nominal | 9 | 0.0 |
| Sector | str | alta cardinalidad | 41 | 0.0 |
| Tipo de punto monitoreo | str | nominal | 7 | 0.0 |
| Grupo | str | nominal | 7 | 0.0 |
| Producto | str | alta cardinalidad | 266 | 0.0 |
| Unidad | str | alta cardinalidad | 19 | 0.0 |
| Precio minimo | int64 | discreta | 2417 | 0.0 |
| Precio maximo | int64 | discreta | 2525 | 0.0 |
| Precio promedio | str | alta cardinalidad | 39787 | 0.0 |

## Requisitos del curso

| estado | requisito | detalle |
| --- | --- | --- |
| OK | Al menos 2000 filas | 221432 filas |
| OK | Al menos 12 columnas | 15 columnas |
| OK | Combina al menos 3 roles analíticos | discreta, alta cardinalidad, nominal, fecha |
| OK | Al menos una variable numérica | 6 numéricas (continuas o discretas) |
| OK | Al menos una variable categórica | 3 categóricas (nominales, binarias u ordinales) |
| AVISO | Presencia de valores faltantes | máximo 0.0% en una variable |
| OK | Ninguna variable sobre 60% de faltantes | máximo 0.0% |
| OK | Incluye alguna variable de fecha | 2 detectadas |
| OK | Incluye texto o categórica de alta cardinalidad | 4 detectadas |
| OK | Archivo bajo 100 MB | 38.3 MB |
| OK | Sin filas duplicadas exactas | ninguna |

## Resultado

El conjunto **cumple** los requisitos mínimos.