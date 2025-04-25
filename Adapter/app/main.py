from Classes.carregador_antigo import CarregadorAntigo
from Classes.adaptador_de_tomada import AdaptadorDeTomada

carregador_antigo = CarregadorAntigo()
adaptador = AdaptadorDeTomada(carregador_antigo)

print(adaptador.conectar())  # "Conectado na tomada de 2 pinos"
