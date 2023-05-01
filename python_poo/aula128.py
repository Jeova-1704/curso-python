# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod #Com isso posso chamar o metodo igual ao atributo acima, onde eu posso apenas digitar a classe ponto o que vou chamar
    def metodo_de_classe(cls):
        print("Hey")

    @classmethod 
    def criar_com_cinquenta_anos(cls, nome):
        return cls(nome, 50)

    @classmethod 
    def sem_nome(cls, idade):
        return cls("Anonima", idade)

p1 = Pessoa ("João", 21)
p2 = Pessoa.criar_com_cinquenta_anos('Helena')
p3 = Pessoa('Anonima', 34)
p4 = Pessoa.sem_nome(34)

print(Pessoa.ano)
p1.metodo_de_classe()
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
