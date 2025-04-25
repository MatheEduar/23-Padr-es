from Classes.carregador_usb import CarregadorUSB

class AdaptadorDeTomada(CarregadorUSB):
    def __init__(self, carregador_antigo):
        self.carregador_antigo = carregador_antigo

    def conectar(self):
        return self.carregador_antigo.plugar_na_tomada()