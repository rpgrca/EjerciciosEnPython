import unittest
from ddt import ddt, data

class Facturadora:
    def __init__(self, minutos, segundos):
        self.__total = (minutos * 60 + segundos) * 3
        
    def obtenerTotal(self):
        return self.__total

@ddt
class FacturacionDeLlamadasUnitTests(unittest.TestCase):
    
    @data((0, 0, 0), (3, 30, 630))
    def test_si_llamada_dura_menos_de_5_minutos_entonces_se_cobra_3_centavos_por_segundo(self, values):
        sut = Facturadora(values[0], values[1])
        self.assertEqual(values[2], sut.obtenerTotal())
    
    
if __name__ == "__main__":
    unittest.main()
