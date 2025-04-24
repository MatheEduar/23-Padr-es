class Lanche:
    def __init__(self):
        self.pao = None 
        self.carne = None
        self.queijo = None
        self.saladas = []

    def __str__(self):
        return f"Lanche com {self.pao}, {self.carne}, {self.queijo}, saladas: {', '.join(self.saladas)}"
    