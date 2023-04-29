# Escopo da classe e de métodos da clasee
class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return (f'{self.nome} está comendo {alimento}')



leao = Animal("leão")
print(leao.nome)
print(leao.comendo('carne'))