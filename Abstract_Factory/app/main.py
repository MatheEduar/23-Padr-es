from domain.fabricas.Classes.fabrica_escura import FabricaEscura
from domain.fabricas.Classes.fabrica_clara import FabricaClara

tema = FabricaEscura()  # ou FabricaClara()
botao = tema.criar_botao()
caixa = tema.criar_caixa_de_texto()

print(botao.render())
print(caixa.render())
