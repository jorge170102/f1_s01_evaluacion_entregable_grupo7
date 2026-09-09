# Validación del dataset — MCDI500

**Archivo:** `simce4b2025_rbd_final.csv` · 7143 filas × 42 columnas

## Perfil de variables

| variable | dtype | rol | unicos | pct_nulos |
| --- | --- | --- | --- | --- |
| rbd | int64 | identificador | 7143 | 0.0 |
| dvrbd | int64 | discreta | 10 | 0.0 |
| nom_rbd | str | alta cardinalidad | 6563 | 0.0 |
| cod_reg_rbd | int64 | discreta | 16 | 0.0 |
| nom_reg_rbd | str | alta cardinalidad | 16 | 0.0 |
| cod_pro_rbd | int64 | discreta | 56 | 0.0 |
| nom_pro_rbd | str | alta cardinalidad | 56 | 0.0 |
| cod_com_rbd | int64 | discreta | 344 | 0.0 |
| nom_com_rbd | str | alta cardinalidad | 344 | 0.0 |
| cod_deprov_rbd | int64 | discreta | 44 | 0.0 |
| nom_deprov_rbd | str | alta cardinalidad | 44 | 0.0 |
| cod_depe1 | int64 | discreta | 6 | 0.0 |
| cod_depe2 | int64 | discreta | 4 | 0.0 |
| cod_grupo | float64 | discreta | 5 | 1.6 |
| cod_rural_rbd | int64 | binaria | 2 | 0.0 |
| nalu_lect4b_rbd | int64 | discreta | 173 | 0.0 |
| nalu_mate4b_rbd | int64 | discreta | 181 | 0.0 |
| prom_lect4b_rbd | float64 | discreta | 171 | 7.9 |
| prom_mate4b_rbd | float64 | discreta | 172 | 7.9 |
| dif_lect4b_rbd | float64 | discreta | 148 | 25.4 |
| dif_mate4b_rbd | float64 | discreta | 137 | 25.1 |
| difgru_lect4b_rbd | float64 | discreta | 131 | 22.1 |
| difgru_mate4b_rbd | float64 | discreta | 135 | 21.7 |
| sigdif_lect4b_rbd | float64 | discreta | 3 | 25.4 |
| sigdif_mate4b_rbd | float64 | discreta | 3 | 25.1 |
| siggru_lect4b_rbd | float64 | discreta | 3 | 22.1 |
| siggru_mate4b_rbd | float64 | discreta | 3 | 21.7 |
| marca_lect4b_rbd | float64 | binaria | 2 | 92.6 |
| marca_mate4b_rbd | float64 | binaria | 2 | 92.9 |
| marcadif_lect4b_rbd | float64 | binaria | 2 | 76.2 |
| marcadif_mate4b_rbd | float64 | binaria | 2 | 76.5 |
| palu_eda_ins_lect4b_rbd | float64 | continua | 569 | 28.4 |
| palu_eda_ele_lect4b_rbd | float64 | continua | 376 | 28.4 |
| palu_eda_ade_lect4b_rbd | float64 | continua | 661 | 28.4 |
| palu_eda_ins_mate4b_rbd | float64 | continua | 695 | 28.4 |
| palu_eda_ele_mate4b_rbd | float64 | continua | 458 | 28.4 |
| palu_eda_ade_mate4b_rbd | float64 | continua | 650 | 28.4 |
| noaplica | int64 | discreta | 4 | 0.0 |
| codigo_bbdd | str | nominal | 1 | 0.0 |
| fecha_bbdd | int64 | discreta | 1 | 0.0 |
| grado | str | nominal | 1 | 0.0 |
| agno | int64 | discreta | 1 | 0.0 |

## Requisitos del curso

| estado | requisito | detalle |
| --- | --- | --- |
| OK | Al menos 2000 filas | 7143 filas |
| OK | Al menos 12 columnas | 42 columnas |
| OK | Combina al menos 3 roles analíticos | discreta, continua, alta cardinalidad, binaria, nominal |
| OK | Al menos una variable numérica | 29 numéricas (continuas o discretas) |
| OK | Al menos una variable categórica | 7 categóricas (nominales, binarias u ordinales) |
| OK | Presencia de valores faltantes | máximo 92.9% en una variable |
| AVISO | Ninguna variable sobre 60% de faltantes | máximo 92.9% |
| AVISO | Incluye alguna variable de fecha | 0 detectadas |
| OK | Incluye texto o categórica de alta cardinalidad | 5 detectadas |
| OK | Archivo bajo 100 MB | 1.3 MB |
| OK | Sin filas duplicadas exactas | ninguna |

## Resultado

El conjunto **cumple** los requisitos mínimos.