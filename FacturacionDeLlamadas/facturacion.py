import unittest
from ddt import ddt, data

class ConsumoPorLlamada:
    def __init__(self, minutos, segundos):
        self.__duracion = minutos * 60 + segundos

        if (minutos < 5):
            self.__costo = self.__duracion * 3
        else:
            self.__costo = (minutos + (1 if segundos > 0 else 0)) * 150

    def obtener_duracion(self):
        return self.__duracion

    def obtener_costo(self):
        return self.__costo

class ConsumoPorLlamadas:
    def __init__(self, llamadas):
        self.__consumo = 0
        self.__duracion = 0

        for (m, s) in llamadas:
            compr = ConsumoPorLlamada(m, s)
            self.__consumo += compr.obtener_costo()
            self.__duracion += compr.obtener_duracion()

    def obtener_duracion(self):
        return self.__duracion

    def obtener_total(self):
        return self.__consumo
    
class FacturacionDeLlamadas:
    def __init__(self, consumos):
        llamadas = [ConsumoPorLlamadas(l) for n, l in consumos.items()]
        self.__consumo = sum(l[1] for l in sorted((l.obtener_duracion(), l.obtener_total()) for l in llamadas)[:-1])

    def obtener_total(self):
        return self.__consumo

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
