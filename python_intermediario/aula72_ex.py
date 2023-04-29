# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicacao(*args):
    total = 1
    for num in args:
        total *= num
    return total


numeros = multiplicacao(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
print(numeros)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(x):
    if x % 2 == 0:
        return f'O número {x} é par.'
    else:
        return f'O número {x} é impar.'
    

print(par_impar(1))
print(par_impar(4))
print(par_impar(6))
print(par_impar(7))

