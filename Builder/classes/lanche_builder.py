from Classes.lanche import Lanche

class LancheBuilder:
    def __init__(self):
        self.lanche = Lanche()

    def com_pao(self, tipo):
        self.lanche.pao = tipo
        return self

    def com_carne(self, tipo):
        self.lanche.carne = tipo
        return self

    def com_queijo(self, tipo):
        self.lanche.queijo = tipo
        return self

    def com_saladas(self, *saladas):
        self.lanche.saladas.extend(saladas)
        return self

    def construir(self):
        return self.lanche
