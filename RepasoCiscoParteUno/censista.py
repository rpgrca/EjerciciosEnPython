# Representa el modelado del censista, la persona que va casa por casa realizando
# el censo en sí. El censista lleva consigo un formulario de planillas, arranca
# una planilla nueva de dicho formulario por cada casa que va a censar y censa
# siempre y cuando la respuesta a la primer pregunta sea distinta de cero. Al
# finalizar cada censo archiva la planilla en una carpeta antes de dirigirse a
# la siguiente casa.

class Censista(object):
  def __init__(self, formulario):
    self.__formulario = formulario
    self.__carpeta = []

  def visitarCasa(self):
    self.__planilla = self.__formulario()

  def leerPregunta(self, indice):
     return input(f" {self.__planilla.obtenerPregunta(indice)} ")

  def anotarRespuesta(self, respuesta):
    self.__planilla.anotarRespuesta(respuesta)

  def esPosibleEncuestar(self):
    respuesta = self.leerPregunta(0)
    self.anotarRespuesta(respuesta)
    return respuesta != "0"

  def realizarPreguntas(self):
    for numero in range(1, self.__planilla.contarPreguntas()):
      respuesta = self.leerPregunta(numero)
      self.anotarRespuesta(respuesta)

  def archivarPlanilla(self):
    self.__carpeta.append(self.__planilla)

  def entregarPlanillas(self):
    return self.__carpeta
