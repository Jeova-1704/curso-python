"""
Crie uma classe Animal com os métodos dormir, comer e emitir_som.
 Em seguida, crie uma classe Cachorro que herda de Animal e adicione um método latir que emite um som específico de latido.
"""

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     def __init__(self, nome) -> None:
#         self.nome = nome
    
#     @abstractmethod
#     def comer(self):
#         ...

#     @abstractmethod
#     def dormi(self):
#         ...

#     @abstractmethod
#     def emitirSom(self):
#         ...
    

# class Cachorro(Animal):
#     def comer(self):
#         print('Cachorro está comendo')
#     def dormi(self):
#         return super().dormi()
#     def emitirSom(self):
#         return super().emitirSom()
    
# a1 = Cachorro('Toby')




class Animal():
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def comer(self):
        print('nhock, nhock')

    def dormi(self):
        print('ZZZzzzzz')

    def emitirSom(self):
        print('bru, bru')
    

class Cachorro(Animal):
    def latir(self):
        print('Au au')

    def comer(self):
        print(f'Seu cachorro {self.nome} está dorminfo')

a1 = Cachorro('Toby')
a1.latir()
a1.comer()

