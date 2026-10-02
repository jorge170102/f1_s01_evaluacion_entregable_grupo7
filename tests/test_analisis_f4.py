import unittest
import pandas as pd
from src.analisis_f4 import promedio_ponderado, percentrank_inc_excel, calcular_ict

class TestAnalisisF4(unittest.TestCase):
    def test_promedio_ponderado(self):
        df=pd.DataFrame({"puntaje_promedio":[200,300],"n_alumnos":[1,3]})
        self.assertAlmostEqual(promedio_ponderado(df),275.0)

    def test_percentrank_extremos(self):
        p=percentrank_inc_excel(pd.Series([10,20,30]))
        self.assertEqual(float(p.iloc[0]),0.0)
        self.assertEqual(float(p.iloc[-1]),1.0)

    def test_ict_rango_y_maximo(self):
        df=pd.DataFrame({"Brecha":[1,2,3],"Concentracion":[.1,.2,.3],"Exposicion":[10,20,30]})
        r=calcular_ict(df)
        self.assertTrue(r["ICT"].between(0,1).all())
        self.assertEqual(int(r.loc[r["ICT"].idxmax(),"P90"]),1)

if __name__=="__main__":
    unittest.main()
