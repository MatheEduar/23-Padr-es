class Singleton: 
    _instacia = None

    def __new__(cls):
        if cls._instacia is None:
            print("Criando nova instância!")
            cls._instacia = super(Singleton, cls).__new__(cls)
        else:
            print("Reutilizando instância existente.")
        return cls._instacia