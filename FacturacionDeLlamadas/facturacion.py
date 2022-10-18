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
