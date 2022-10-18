import unittest
from ddt import ddt, data

class ConsumoPorLlamada:
    def __init__(self, minutos, segundos):
        if (minutos < 5):
            self.__total = (minutos * 60 + segundos) * 3
        else:
            if segundos == 0:
                self.__total = minutos * 150
            else:
                self.__total = (minutos + 1) * 150

    def obtenerTotal(self):
        return self.__total

class ConsumoPorLlamadas:
    def __init__(self, llamadas):
        self.__consumo = sum(ConsumoPorLlamada(m, s).obtenerTotal() for m, s in llamadas)

    def obtenerTotal(self):
        return self.__consumo

@ddt
class FacturacionDeLlamadasUnitTests(unittest.TestCase):
    
    @data((0, 0, 0), (3, 30, 630))
    def test_si_llamada_dura_menos_de_5_minutos_entonces_se_cobra_3_centavos_por_segundo(self, values):
        sut = ConsumoPorLlamada(values[0], values[1])
        self.assertEqual(values[2], sut.obtenerTotal())

    @data((6, 0, 900), (6, 30, 1050))
    def test_si_llamada_mayor_5_minutos_entonces_redondear_segundos_al_minuto_superior_y_cobrar_150_centavos_por_minuto(self, values):
        sut = ConsumoPorLlamada(values[0], values[1])
        self.assertEqual(values[2], sut.obtenerTotal())

    def test_calcular_consumo_de_llamadas_en_una_lista(self):
        sut = ConsumoPorLlamadas([(0, 0), (3, 30)])
        self.assertEqual(630, sut.obtenerTotal())
    
    def test_calcular_consumo_de_llamadas_mayores_a_5_minutos_correctamente(self):
        sut = ConsumoPorLlamadas([(6, 0), (6, 30)])
        self.assertEqual(1950, sut.obtenerTotal())

if __name__ == "__main__":
    unittest.main()
