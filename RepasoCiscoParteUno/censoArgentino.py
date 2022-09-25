from planilla import Planilla
from informe import Informe

# Representa el modelado de las preguntas que se van a realizar durante el
# censo. A partir de esas preguntas se generan las planillas que se entregan
# a los censistas.

class PlanillaCensoArgentina(object):
  preguntas = [
    "Cuántos integrantes hay en la familia?",
    "Cuántos son menores de 18 años?",
    "Cuántos años tiene la persona más anciana?",
    "Cuántos años tiene la persona más joven?",
    "Cuál es el ingreso salarial de la familia?",
    "Cuántos vehículos posee?"
  ]

  def obtenerPlanilla(self):
    return Planilla(PlanillaCensoArgentina.preguntas)

# Representa el modelado de los informes que se quieren generar a partir de
# las planillas. Está intimamente ligado a la planilla del censo, por eso se
# accede a índices de respuesta directamente y no a propiedades.

class InformeCensoArgentina(object):
  informes = {
    ( "Cantidad de habitantes censados", lambda p: sum(x.respuestaComoEntero(0) for x in p) ),
    ( "Promedio de habitantes por hogar censados", lambda p: sum(x.respuestaComoEntero(0) for x in p) / len(p) ),
    ( "Porcentaje de menores", lambda p: sum(x.respuestaComoDecimal(1) for x in p) / sum(x.respuestaComoDecimal(0) for x in p) ),
    ( "Edad de la persona más vieja", lambda p: max(x.respuestaComoEntero(2) for x in p) ),
    ( "Edad de la persona más joven", lambda p: min(x.respuestaComoEntero(3) for x in p) ),
    ( "Promedio de ingreso por hogar", lambda p: sum(x.respuestaComoDecimal(4) for x in p) / len(p) ),
    ( "Cantidad de vehículos", lambda p: sum(x.respuestaComoEntero(5) for x in p) ),
    ( "Porcentaje de vehículos por familia", lambda p: sum(x.respuestaComoEntero(5) for x in p) / len(p) )
  }

  def generar(self):
    return [Informe(texto, formula) for texto, formula in InformeCensoArgentina.informes]
