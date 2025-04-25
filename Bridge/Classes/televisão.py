from Interfaces.dispositivo import Dispositivo

class Televisão(Dispositivo):
    def ligar(self):
        print("TV ligada.")

    def desligar(self):
        print("TV desligada.")