# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 900,
# }

# print(len(pessoa))
# print(pessoa.keys())
# print(pessoa.values())
# print(pessoa.items())

# for chaves, valores in pessoa.items():
#     print(chaves,':', valores)

# print(pessoa.setdefault('pesso', 60))


# import copy #copia profunda e que consegue copiar profudamente os valores

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0,1 ,2]
# }

# d2 = copy.deepcopy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 999999999

# print(d1)
# print(d2)




p1 = {
    'nome': 'Jeová',
    'sobrenome': 'Bezerra'
}
# # print(p1.get('nome'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# p1.update({
#     'nome': 'novo valor'

# })
# print(p1)

