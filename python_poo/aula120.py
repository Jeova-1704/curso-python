# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = "Jeová" #str
# print(string.upper())
# print(isinstance(string, str))
# print(str) #Print o tipo de classe da str

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Jeová', 'Bezerra')
# p1.nome = "Jeová"
# p1.sobrenome = "Bezerra Leite"

p2 = Pessoa('Isadora', 'Vasconcelo Silvestre')
# p2.nome = "Isadora"
# p2.sobrenome = "Vasconcelo Silvestre"

print(p1.nome)
print(p1.sobrenome)
print()
print(p2.nome)
print(p2.sobrenome)
