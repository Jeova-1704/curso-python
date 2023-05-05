# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         return super(MinhaString, self).upper()
#         # super() retorna o metodo com o nome da classe


# string = MinhaString('Jeova')
# print(string.upper())


class A:
    atributo_a = 'valor de A'
    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor de B'
    def metodo(self):
        super().metodo()
        print('B')
    

class C(B):
    atributo_c = 'valor de C'
    def metodo(self):
        super().metodo() #prita o valor do metodo B (Ou seja print('B'))
        print('C')
    

a = A()
print(a.atributo_a)
a.metodo()

print()
b = B()

print(b.atributo_a)
print(b.atributo_b)
b.metodo()

print()

c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()
