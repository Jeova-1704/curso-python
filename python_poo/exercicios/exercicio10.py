"""
Crie uma classe Lista que receba um atributo do tipo list
e que tenha um método o qual retorne os elementos da lista 
sem repetição. Crie o programa de teste.
"""


class Lista:
    def __init__(self, lista) -> None:
        self.lista = lista

    def semRepeticoes(self):
        return list(set(self.lista))
    

lista1 = Lista([1, 4, 5, 6, 2, 1, 4, 5, 7, 8, 3, 8, 12, 11, 11, 11])
print(lista1.semRepeticoes())