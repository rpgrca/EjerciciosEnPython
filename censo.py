# Representa el modelado del censo en sí. Para realizar el censo se le pide a
# un censista que visite una por una varias casas, realice todas las preguntas
# del formulario y luego archive la planilla donde anotó las respuestas antes
# de dirigirse a la siguiente casa. Al final se le pide que entregue todas las
# planillas que utilizó para generar para generar cada uno de los informes a
# partir de ellas.

from censista import Censista

class Censo(object):
  def __init__(self, formulario, informe):
    self.__censista = Censista(formulario)
    self.__informe = informe

  def realizarCenso(self):
    self.__censista.visitarCasa()

    while self.__censista.esPosibleEncuestar():      
      self.__censista.realizarPreguntas()
      self.__censista.archivarPlanilla()
      self.__censista.visitarCasa()

  def realizarInforme(self):
    print("\n== Resultado del Censo ==\n")
    planillas = self.__censista.entregarPlanillas()

    if len(planillas) > 0:
      informes = self.__informe()

      for informe in informes:
        informe.calcularSobre(planillas)
        informe.mostrar()
    else:
      print("No se censó a nadie.")
      