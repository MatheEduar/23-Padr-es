from classes.cafe import Cafe
from classes.chocolate import Chocolate
from classes.leite import Leite


bebida = Cafe()
bebida = Leite(bebida)
bebida = Chocolate(bebida)

print(bebida.descrição())  # "Café, com leite, com chocolate"
print("Total: R$", bebida.custo())  # Total: R$ 8
