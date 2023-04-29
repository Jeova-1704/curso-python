#Lista comprehensiom

numeros = [1, 2, 3, 4, 5]

# novos_numeros = numeros.copy()

# novos_numeros = []
# for numero in numeros:
#     novos_numeros.append(numero)

novos_numeros = [numero
                for numero in numeros]

print(novos_numeros)

#===================================================================#

# #utilização da lista comprehension 


# def divisaoFn(x, y):
#     return x / y


# def multiplicacaoFn(x, y):
#     return x * y


# def potenciacaoFn(x, y):
#     return x ** y 



# numeros = [1, 2, 3, 4, 5]

# divisao = [divisaoFn (numero , 2) for numero in numeros]
# multiplicacao = [multiplicacaoFn (numero , 2) for numero in numeros]
# quadrado = [potenciacaoFn (numero, 2) for numero in numeros]

# print(numeros)
# print(divisao)
# print(multiplicacao)
# print(quadrado)


#=====================================================================#

# # condicionais em lista comprehension

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# novos_numeros = [numero for numero in numeros if numero > 5]
# impares = [numero for numero in numeros if numero % 2 != 0]
# pares = [numero for numero in numeros if numero % 2 == 0]
# outro_if = [numero
#             if numero != 6 else 600
#             for numero in pares]

# print(novos_numeros)
# print(impares)
# print(pares)
# print(outro_if)






