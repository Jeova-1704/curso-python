"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento

# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


def soma(*args): # Empacota os dados com os *
    total = 0
    for num in args:
        total += num
    return total


soma_1_2__3 = soma(1, 2, 3)
# print(soma_1_2__3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10

outra_soma = soma(*numeros) # Desenpacota os dados antes de serem mandados para as funções e outros metodos
print(outra_soma)

# print(sum(numeros))
print(numeros)