from domain.produtos.Classes.botao_escuro import BotaoEscuro
from domain.produtos.Classes.caixa_de_texto_escuro import CaixaDeTextoEscuro
from domain.fabricas.Interfaces.fabrica_de_widgets import FabricaDeWidgets

class FabricaEscura(FabricaDeWidgets):
    def criar_botao(self):
        return BotaoEscuro()
    def criar_caixa_de_texto(self):
        return CaixaDeTextoEscuro()
