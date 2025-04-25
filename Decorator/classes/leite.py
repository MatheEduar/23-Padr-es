from Interfaces.complemento import Complemento

class Leite(Complemento):
    def custo(self):
        return self.bebida.custo() + 1
    
    def descrição(self):
        return self.bebida.descrição() + ", com leite"