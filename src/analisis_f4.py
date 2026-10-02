"""Funciones reutilizables del análisis F4 SIMCE 2025."""
from __future__ import annotations
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.oneway import anova_oneway, effectsize_oneway

def promedio_ponderado(df, valor="puntaje_promedio", peso="n_alumnos"):
    return float(np.average(df[valor], weights=df[peso]))

def percentrank_inc_excel(serie, significance=3):
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
    x["Perc_Brecha"]=percentrank_inc_excel(x["Brecha"])
    x["Perc_Concentracion"]=percentrank_inc_excel(x["Concentracion"])
    x["Perc_Exposicion"]=percentrank_inc_excel(x["Exposicion"])
    x["ICT"]=.50*x["Perc_Brecha"]+.30*x["Perc_Concentracion"]+.20*x["Perc_Exposicion"]
    x["Perc_ICT"]=percentrank_inc_excel(x["ICT"])
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
