from Interfaces.dispositivo import Dispositivo

class Projetor(Dispositivo):
    def ligar(self):
        print("Projetor ligado.")

    def desligar(self):
        print("Projetor desligado.")
