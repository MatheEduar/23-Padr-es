from Interfaces.bebida import Bebida

class Cafe(Bebida):
    def custo(self):
        return 5
    
    def descrição(self):
        return "Café"