from domain.produtos.Classes.botao_claro import BotaoClaro
from domain.produtos.Classes.caixa_de_texto_clara import CaixaDeTextoClara
from domain.fabricas.Interfaces.fabrica_de_widgets import FabricaDeWidgets

class FabricaClara(FabricaDeWidgets):
    def criar_botao(self):
        return BotaoClaro()
    def criar_caixa_de_texto(self):
        return CaixaDeTextoClara()
