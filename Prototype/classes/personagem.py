import copy

class Personagem:
    def __init__(self, nome, classe, nivel, equipamentos=None):
        self.nome = nome
        self.classe = classe
        self.nivel = nivel
        self.equipamentos = equipamentos or []
        
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        eqs = ', '.join(self.equipamentos)
        return f"{self.nome} - Classe: {self.classe}, Nível: {self.nivel}, Equipamentos {eqs}"