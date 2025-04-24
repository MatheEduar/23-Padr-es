from Classes.lanche_builder import LancheBuilder
from Classes.director import DiretorDeLanches

builder = LancheBuilder()
diretor = DiretorDeLanches(builder)

lanche1 = diretor.montar_combo_classico()
print("Combo clássico:", lanche1)

builder = LancheBuilder()  # Novo builder, lanche novo!
diretor = DiretorDeLanches(builder)

lanche2 = diretor.montar_combo_vegetariano()
print("Combo vegetariano:", lanche2)
