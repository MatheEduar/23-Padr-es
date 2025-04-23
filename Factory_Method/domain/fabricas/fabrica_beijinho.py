from domain.doces.beijinho import Beijinho
from domain.fabricas.fabrica_base import FabricaDeDoces

class FabricaDeBeijinho(FabricaDeDoces):
    def criar_doce(self):
        return Beijinho()
