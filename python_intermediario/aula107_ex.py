"""
# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
"""


# def zipper(cap, estad):
#     intervalo = min(len(cap), len(estad))
#     return [(cap[i], estad[i]) for i in range(intervalo)]

#ou

'''
capitais = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(capitais, estados)))
'''



# def zipper(capitals, states):
#     brasil = []
#     for valor in zip(capitals, states):
#         brasil.append(valor)
#     return brasil


# capitais = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# estados = ['BA', 'SP', 'MG', 'RJ']

# print(zipper(capitais, estados))




#================================================================================================================================================================

'''
"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
'''


# def somar_listas(lista1, lista2):
#     return[
#         lista1[i] + lista2[i] for i in range(min(len(lista1), len(lista2)))
#     ]


# lista_a = [1, 2, 3, 4, 5, 6, 7]
# lista_b = [1, 2, 3, 4]

# print(somar_listas(lista_a, lista_b))