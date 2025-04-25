from Classes.item_sistema import ItemSistema

class Pasta(ItemSistema):
    def __init__(self, nome):
        self.nome = nome
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def exibir(self, indent=0):
        print(" " * indent + f"Pasta: {self.nome}")
        for item in self.itens:
            item.exibir(indent + 2)    