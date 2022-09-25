# Representa el modelado de un informe a realizar con la información existente
# en las planillas. Cada informe tiene un título y una fórmula a aplicar a las
# planillas.

class Informe(object):
  def __init__(self, texto, formula):
    self.__texto = texto
    self.__formula = formula
    self.__valor = 0

  def calcularSobre(self, planillas):
    self.__valor = self.__formula(planillas)
  
  def mostrar(self):
    print(f"{self.__texto}: {self.__valor}")
