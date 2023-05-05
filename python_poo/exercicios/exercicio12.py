class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self, porcentagem):
        return f'{self.nome} com um salario de {self.salario} teve um aumento de {porcentagem}% ficando com um salario de R${self.salario + (self.salario * (porcentagem/100))}'
    

f1 = Funcionario('Jeová', 1000)
print(f1.aumentarSalario(20))
print()
f2 = Funcionario('Jeová', 1000)
print(f2.aumentarSalario(50))

