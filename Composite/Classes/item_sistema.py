from abc import ABC, abstractmethod

class ItemSistema(ABC):
    @abstractmethod
    def exibir(self, indent=0):
        pass