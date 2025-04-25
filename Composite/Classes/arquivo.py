from Classes.item_sistema import ItemSistema

class Arquivo(ItemSistema):
    def __init__(self, nome):
        self.nome = nome

    def exibir(self, indent=0):
        print(" " * indent + f"Arquivo: {self.nome}")
