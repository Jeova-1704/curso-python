"""
Implemente uma calculadora que receba dois operadores 
utilizando os conceitos de orientação a objetos aprendidos. Os 
atributos op1 e op2 (operadores) são iniciados no construtor e os 
métodos somar(), subtrair(), multiplicar(), dividir()
e calcularPotencia() realizam as respectivas ações nesses 
atributos. Crie o programa de teste para a classe Calculadora.
"""
class Calculadora:
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2 

    def somar(self):
        return(self.op1 + self.op2)

    def subtrair(self):
        return (self.op1 - self.op2)

    def multiplicar(self):
        return (self.op1 * self.op2)

    def dividir(self):
        if self.op2 == 0:
            return "Impossivel dividir por zero"
        return (self.op1 / self.op2)

    def calcularPotencia(self):
        return self.op1 ** self.op2

calcular = Calculadora(2, 2)
print(calcular.somar())
print(calcular.dividir())
print(calcular.multiplicar())
print(calcular.subtrair())
print(calcular.calcularPotencia())
