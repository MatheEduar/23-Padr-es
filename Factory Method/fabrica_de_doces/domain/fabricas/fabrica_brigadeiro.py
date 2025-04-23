from domain.doces.brigadeiro import Brigadeiro
from domain.fabricas.fabrica_base import FabricaDeDoces

class FabricaDeBrigadeiro(FabricaDeDoces):
    def criar_doce(self):
        return Brigadeiro()
