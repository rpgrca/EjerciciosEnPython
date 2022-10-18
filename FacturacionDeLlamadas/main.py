import unittest

class Facturadora:
    def __init__(self, duracion):
        self.__total = duracion * 3
        
    def obtenerTotal(self):
        return self.__total

class FacturacionDeLlamadasUnitTests(unittest.TestCase):
    def test_si_llamada_dura_menos_de_5_minutos_entonces_se_cobra_3_centavos_por_segundo(self):
        sut = Facturadora(3)
        self.assertEqual(9, sut.obtenerTotal())
    
    
if __name__ == "__main__":
    unittest.main()
