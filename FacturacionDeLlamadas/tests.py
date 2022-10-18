import unittest
from ddt import ddt, data
from facturacion import ConsumoPorLlamada, ConsumoPorLlamadas, FacturacionDeLlamadas

@ddt
class FacturacionDeLlamadasUnitTests(unittest.TestCase):

    @data((0, 0, 0), (3, 30, 630), (0, 30, 90), (0, 40, 120), (0, 50, 150), (0, 10, 30), (0, 20, 60))
    def test_si_llamada_dura_menos_de_5_minutos_entonces_se_cobra_3_centavos_por_segundo(self, values):
        sut = ConsumoPorLlamada(values[0], values[1])
        self.assertEqual(values[2], sut.obtener_costo())

    @data((6, 0, 900), (6, 30, 1050))
    def test_si_llamada_mayor_5_minutos_entonces_redondear_segundos_al_minuto_superior_y_cobrar_150_centavos_por_minuto(self, values):
        sut = ConsumoPorLlamada(values[0], values[1])
        self.assertEqual(values[2], sut.obtener_costo())

    def test_calcular_consumo_de_llamadas_en_una_lista(self):
        sut = ConsumoPorLlamadas([(0, 0), (3, 30)])
        self.assertEqual(630, sut.obtener_total())
    
    def test_calcular_consumo_de_llamadas_mayores_a_5_minutos_correctamente(self):
        sut = ConsumoPorLlamadas([(6, 0), (6, 30)])
        self.assertEqual(1950, sut.obtener_total())

    def test_calcular_consumo_excluyendo_mayor_llamada(self):
        sut = FacturacionDeLlamadas({
            "Federico": [(0, 30), (0, 40), (0, 50)],
            "Sabrina": [(0, 10), (0, 20), (0, 30)],
            "Pedro": [(0, 10), (0, 10), (0, 20)]
        })
        self.assertEqual(300, sut.obtener_total())

if __name__ == "__main__":
    unittest.main()
