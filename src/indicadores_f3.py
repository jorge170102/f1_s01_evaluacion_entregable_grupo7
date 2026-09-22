import pandas as pd

# Función reutilizable para calcular el promedio regional con Pandas

def promedio_por_region_pandas(datos):

    resultado = (
        datos.groupby("region")["puntaje_promedio"]
        .mean()
        .reset_index()
    )

    return resultado


# Método 2: calcular el promedio regional mediante un bucle for

def promedio_por_region_bucle(datos):

    sumas = {}
    cantidades = {}

    for region, puntaje in zip(
        datos["region"],
        datos["puntaje_promedio"]
    ):

        if region not in sumas:
            sumas[region] = 0
            cantidades[region] = 0

        sumas[region] += puntaje
        cantidades[region] += 1

    resultado = []

    for region in sorted(sumas):

        promedio = sumas[region] / cantidades[region]

        resultado.append({
            "region": region,
            "puntaje_promedio": promedio
        })

    return pd.DataFrame(resultado)