# Atributo de classe (Cria um valor na classe para todas as instancias)
class Pessoa:
    ano_atual = 2023


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
        

p1 = Pessoa('Jeová', 19)
p2 = Pessoa('samuel', 14)
print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
