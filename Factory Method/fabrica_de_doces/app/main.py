from domain.fabricas.fabrica_brigadeiro import FabricaDeBrigadeiro
from domain.fabricas.fabrica_beijinho import FabricaDeBeijinho

fabrica1 = FabricaDeBeijinho()
doce1 = fabrica1.criar_doce()
print(doce1.preparar())

fabrica2 = FabricaDeBrigadeiro()
doce2 = fabrica2.criar_doce()
print(doce2.preparar())