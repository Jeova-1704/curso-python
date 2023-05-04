"""
. Crie uma classe chamada Ingresso, que possua o nome do 
evento e o valor do ingresso. Crie o método exibirValor(), 
que apenas retorne o valor do ingresso. Crie o método __str__ 
que retorne o nome do evento seguido do valor do ingresso. 
Crie um programa para testar sua classe.
"""

class Ingresso:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def exibirValor(self):
        return self.valor
    
    def __str__(self) -> str:
        return f' NOME DO EVENTO: {self.nome}\n VALOR DO INGRSSO R${self.valor:.2f}'
    

evento1 = Ingresso('Programação', 100) 
print(evento1.exibirValor())
print(evento1.__str__())
print()
evento2 = Ingresso('Show do Nirvana', 350) 
print(evento2.exibirValor())
print(evento2.__str__())