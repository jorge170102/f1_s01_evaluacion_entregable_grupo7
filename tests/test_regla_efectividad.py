"""Pruebas reejecutables de las reglas críticas de F2."""

import unittest
import pandas as pd

from src.transformacion import clasificar_efectividad
from src.validacion import validar_codigos_catalogo


class TestReglaEfectividad(unittest.TestCase):
    def setUp(self):
        self.prueba = pd.DataFrame({
            "rbd": [1, 2, 3, 4],
            "nalu_mate4b_rbd": [20, 0, 15, 12],
            "prom_mate4b_rbd": [250, pd.NA, pd.NA, 260],
            "marca_mate4b_rbd": [pd.NA, pd.NA, 1, 2],
        })

    def test_caso_normal(self):
        resultado = clasificar_efectividad(self.prueba)
        self.assertEqual(resultado.loc[0, "efectividad"], "Efectiva")

    def test_caso_limite(self):
        resultado = clasificar_efectividad(self.prueba)
        self.assertEqual(resultado.loc[1, "efectividad"], "No Efectiva")

    def test_caso_con_observacion(self):
        resultado = clasificar_efectividad(self.prueba)
        self.assertEqual(resultado.loc[2, "efectividad"], "No Efectiva")

    def test_marca_2_con_puntaje(self):
        resultado = clasificar_efectividad(self.prueba)
        self.assertEqual(resultado.loc[3, "efectividad"], "No Efectiva")

    def test_codigo_desconocido(self):
        prueba_error = pd.DataFrame({
            "cod_depe1": [1], "cod_depe2": [1], "cod_grupo": [1],
            "cod_rural_rbd": [1], "marca_mate4b_rbd": [99],
        })
        with self.assertRaises(ValueError):
            validar_codigos_catalogo(prueba_error)


if __name__ == "__main__":
    unittest.main()
