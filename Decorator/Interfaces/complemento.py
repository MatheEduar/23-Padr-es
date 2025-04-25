from Interfaces.bebida import Bebida

class Complemento(Bebida):
    def __init__(self, bebida):
        self.bebida = bebida