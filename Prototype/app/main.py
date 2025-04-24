from Classes.personagem import Personagem

# Cria um personagem base
guerreiro_base = Personagem("Modelo Guerreiro", "Guerreiro", 1, ["Espada", "Escudo"])

# Cria cópias com personalizações
guerreiro1 = guerreiro_base.clone()
guerreiro1.nome = "Thoran"

guerreiro2 = guerreiro_base.clone()
guerreiro2.nome = "Brakka"
guerreiro2.equipamentos.append("Elmo de Ferro")

print(guerreiro_base)
print(guerreiro1)
print(guerreiro2)
