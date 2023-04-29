# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

# pode começar abrindo chaves ou escrevendo dict
# pessoa = {
#     'nome': 'Jeová Bezerra',
#     'sobrenome': 'Leite',
#     'idade': 18,
#     'altura': 1.73,
#     'endereco': [
#         {'rua': 'Cordeiro', 'numero': 123},
#         {'rua': 'bezerro', 'numero': 321}
#     ]
# }

# print(type(pessoa))
# print(pessoa['nome'])
# print(pessoa['idade'])
# print(pessoa['endereco'])

# for chave in pessoa:
#     print(f'{chave=}')

# for chave in pessoa:
#     print(chave, pessoa[chave])


#=======================================================================#

'''
Manimpulando chaves'''
pessoas = {}

chave = 'nome'

pessoas[chave] = 'Jeová Bezerra'

print(pessoas)

print(pessoas[chave])

del pessoas[chave]

print(pessoas)

if pessoas.get('sobrenome'):
    print('existe')

print('isso não existe')