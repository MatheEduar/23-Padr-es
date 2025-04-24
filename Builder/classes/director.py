from Classes.lanche_builder import LancheBuilder

class DiretorDeLanches:
    def __init__(self, builder: LancheBuilder):
        self.builder = builder

    def montar_combo_classico(self):
        return (
            self.builder
            .com_pao("pão francês")
            .com_carne("hambúrguer de carne")
            .com_queijo("prato")
            .com_saladas("alface", "tomate")
            .construir()
        )

    def montar_combo_vegetariano(self):
        return (
            self.builder
            .com_pao("pão integral")
            .com_queijo("mussarela")
            .com_saladas("rúcula", "cenoura", "tomate")
            .construir()
        )
