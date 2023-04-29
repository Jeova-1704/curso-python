#Empacotamento(adiconado coisas no dicionario) e desempacotamento(removendo coisas do dicionario) de dicionarios
a, b = 1, 2
a, b = b, a
# print(a, b)


# (a1, a2), (b1, b2) = pessoa.items() #desempacotamento de dicts 
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Jeová',
    'sobrenome': 'Leite',
}

dados_pessoa = {
    'idade': 17,
    'altura': 1.73,
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# #args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs): #função que recebe argumentos nomeador (dicionarios)
    print('não nomeado:', args)
    # print(kwargs)
    print('nomeados: ')
    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(1, 2, 3, nome='joana', num=123)
# mostro_argumentos_nomeados(**pessoa_completa)



configaracoes = {
    'arg1': 1, 
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configaracoes)




