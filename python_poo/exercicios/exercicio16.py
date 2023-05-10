"""Crie uma classe Pessoa com os métodos andar, falar e comer. Em seguida, crie uma classe Aluno que herda de Pessoa e adicione um método estudar que permite ao aluno estudar uma determinada disciplina."""

class Pessoa():
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print('andando...')

    def falar(self):
        print(f'Oi o meu nome é {self.nome}')
    
    def comer(self, comida):
        print(f'Estou comendo {comida}')


class Aluno(Pessoa):
    def comer(self, comida):
        print('Estou comendo macarrão')
    
    def estudar(self, disciplina):
        print(f'Estou estudando {disciplina}')

aluno1 = Aluno('Jeová')
aluno1.andar()
aluno1.falar()
aluno1.comer('pizza')
aluno1.estudar('matematica')