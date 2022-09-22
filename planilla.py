# Representa el modelado de copia de la planilla a completar con las preguntas
# que se le leerán al censado y un espacio para escribir cada respuesta. Las
# preguntas se responden en orden y luego se interpretan como números enteros
# o decimales por índice de pregunta.

class Planilla(object):
  def __init__(self, preguntas):
    self.__preguntas = preguntas
    self.__respuestas = []

  def contarPreguntas(self):
    return len(self.__preguntas)
  
  def obtenerPregunta(self, numero):
    return self.__preguntas[numero]

  def anotarRespuesta(self, respuesta):
    self.__respuestas.append(float(respuesta))

  def respuestaComoEntero(self, numero):
    return int(self.__respuestas[numero])

  def respuestaComoDecimal(self, numero):
    return float(self.__respuestas[numero])
