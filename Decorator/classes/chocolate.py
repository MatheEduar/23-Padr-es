from Interfaces.complemento import Complemento

class Chocolate(Complemento):
    def custo(self):
        return self.bebida.custo() + 2
    
    def descrição(self):
        return self.bebida.descrição() + ", com chocolate"