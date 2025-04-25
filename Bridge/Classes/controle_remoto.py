class ControleRemoto:
    def __init__(self, dispositivo):
        self.dispositivo = dispositivo

    def ligar_dispositivo(self):
        self.dispositivo.ligar()

    def desligar_dispositivo(self):
        self.dispositivo.desligar()
