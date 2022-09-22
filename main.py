# Entrada del programa. Es posible cear otros censos simplemente creando una
# nueva lista de preguntas y una lista de informes a generar sin necesidad
# de tocar ningún otro archivo excepto el main, cambiando el import y las
# lambdas que generan las planillas y los informes.

from censo import Censo
from censoArgentino import PlanillaCensoArgentina, InformeCensoArgentina

if __name__ == "__main__":
  censo = Censo(lambda: PlanillaCensoArgentina().obtenerPlanilla(), lambda: InformeCensoArgentina().generar())
  censo.realizarCenso()
  censo.realizarInforme()
