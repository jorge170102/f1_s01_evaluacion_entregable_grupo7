"""Funciones reutilizables del análisis F4 SIMCE 2025."""
from __future__ import annotations
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.oneway import anova_oneway, effectsize_oneway

from pathlib import Path
import hashlib
import timeit
import tracemalloc
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

REGION = ['cod_reg_rbd', 'region']
COMUNA = REGION + ['cod_com_rbd', 'comuna']
AZUL, ROJO, GRIS = '#176B87', '#B64045', '#9CAEBB'
FUENTE = 'Fuente: Agencia de Calidad de la Educación, SIMCE Matemática 4.º básico 2025. Base efectiva F2/F3; elaboración propia.'

def validar_entrada(df: pd.DataFrame) -> pd.DataFrame:
    """Rechaza errores sin imputar, eliminar observaciones ni redondear conteos."""
    cols = ['rbd', 'nombre_establecimiento', *COMUNA, 'n_alumnos', 'puntaje_promedio',
            'efectividad', 'anio', 'asignatura', 'grado']
    faltan = sorted(set(cols) - set(df.columns))
    if faltan:
        raise ValueError(f'Faltan columnas: {faltan}')
    if df.empty or df.columns.duplicated().any():
        raise ValueError('Base vacía o columnas duplicadas.')
    out = df.copy()
    if out[cols].isna().any().any():
        raise ValueError('Hay valores faltantes en las variables analíticas.')
    for c in ['rbd', 'cod_reg_rbd', 'cod_com_rbd', 'n_alumnos', 'puntaje_promedio', 'anio']:
        out[c] = pd.to_numeric(out[c], errors='raise')
        if not np.isfinite(out[c].to_numpy(dtype=float)).all():
            raise ValueError(f'Valores no finitos en {c}.')
    for c in ['rbd', 'cod_reg_rbd', 'cod_com_rbd', 'n_alumnos', 'anio']:
        if (out[c] % 1 != 0).any() or out[c].le(0).any():
            raise ValueError(f'{c} debe contener enteros positivos.')
        out[c] = out[c].astype('int64')
    if not out.rbd.is_unique:
        raise ValueError('RBD duplicado: el ranking requiere un registro por establecimiento.')
    if not (out.efectividad.eq('Efectiva').all() and out.anio.eq(2025).all()
            and out.asignatura.eq('Matematica').all() and out.grado.eq('4b').all()):
        raise ValueError('Se requiere el producto efectivo de Matemática 4b 2025.')
    for c in ['region', 'comuna', 'nombre_establecimiento']:
        if out[c].astype(str).str.strip().eq('').any():
            raise ValueError(f'Textos vacíos en {c}.')
    if out.groupby('cod_reg_rbd').region.nunique().max() != 1:
        raise ValueError('Un código regional tiene más de un nombre.')
    if (out.groupby('cod_com_rbd')[['cod_reg_rbd', 'comuna']].nunique() > 1).any().any():
        raise ValueError('Código de comuna inconsistente con su región o nombre.')
    return out

def promedio_ponderado(df, valor="puntaje_promedio", peso="n_alumnos"):
    return float(np.average(df[valor], weights=df[peso]))

def percentil(serie, significance=3):
    s = pd.Series(serie, index=serie.index, dtype=float)
    orden = np.sort(s.dropna().to_numpy())
    if len(orden) <= 1:
        return pd.Series(0.0, index=s.index)
    unicos, primeros = np.unique(orden, return_index=True)
    percentiles = primeros / (len(orden)-1)
    valores = np.interp(s.to_numpy(), unicos, percentiles)
    return pd.Series(np.round(valores, significance), index=s.index)

def resumen_criticidad(df, geo_cols, referencia):
    x=df.copy()
    x["bajo_desempeno_f4"]=(x["puntaje_promedio"]<referencia).astype(int)
    x["exposicion_f4"]=np.where(x["bajo_desempeno_f4"].eq(1),x["n_alumnos"],0)
    x["n_x_puntaje"]=x["n_alumnos"]*x["puntaje_promedio"]
    g=x.groupby(geo_cols,dropna=False).agg(
        N_EE=("rbd","count"), EE_bajo=("bajo_desempeno_f4","sum"),
        N_estudiantes=("n_alumnos","sum"), Suma_n_puntaje=("n_x_puntaje","sum"),
        Exposicion=("exposicion_f4","sum")).reset_index()
    g["Puntaje_ponderado"]=g["Suma_n_puntaje"]/g["N_estudiantes"]
    g["Brecha"]=(referencia-g["Puntaje_ponderado"]).clip(lower=0)
    g["Concentracion"]=g["EE_bajo"]/g["N_EE"]
    return g

def calcular_ict(comunas):
    x=comunas.copy()
    x["Perc_Brecha"]=percentil(x["Brecha"])
    x["Perc_Concentracion"]=percentil(x["Concentracion"])
    x["Perc_Exposicion"]=percentil(x["Exposicion"])
    x["ICT"]=.50*x["Perc_Brecha"]+.30*x["Perc_Concentracion"]+.20*x["Perc_Exposicion"]
    x["Perc_ICT"]=percentil(x["ICT"])
    x["P90"]=(x["Perc_ICT"]>=.90).astype(int)
    return x

def prueba_territorial(df, geo):
    grupos=[g["puntaje_promedio"].dropna().astype(float) for _,g in df.groupby(geo)
            if g["puntaje_promedio"].notna().sum()>=2]
    _,p_lev=stats.levene(*grupos,center="median")
    tipo="equal" if p_lev>=.05 else "unequal"
    nombre="ANOVA clásico" if tipo=="equal" else "ANOVA de Welch"
    res=anova_oneway(grupos,use_var=tipo,welch_correction=True)
    medias=np.array([g.mean() for g in grupos])
    vars_=np.array([g.var(ddof=1) for g in grupos])
    ns=np.array([len(g) for g in grupos])
    f2=float(effectsize_oneway(medias,vars_,ns,use_var=tipo))
    return {"nivel":geo,"prueba":nombre,"p":float(res.pvalue),
            "eta2_equiv":f2/(1+f2),"p_levene":float(p_lev)}
