from Classes.controle_remoto import ControleRemoto
from Classes.projetor import Projetor
from Classes.televisão import Televisão

controle1 = ControleRemoto(Televisão())
controle1.ligar_dispositivo()

controle2 = ControleRemoto(Projetor())
controle2.ligar_dispositivo()
