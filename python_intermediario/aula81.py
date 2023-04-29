# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [1, 3, 5 ,4, 2, 6, 9, 6, 8, 15, 10]
# lista.sort() #ordena listas
# sorted(lista) #odena também listass
# lista.sort(reverse=True) #ordena inversamnete






lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda', 'idade': 18},
    {'nome': 'Maria', 'sobrenome': 'Oliveira', 'idade': 23},
    {'nome': 'Daniel', 'sobrenome': 'Silva', 'idade': 19},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira', 'idade': 17},
    {'nome': 'Aline', 'sobrenome': 'Souza', 'idade': 24},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome']) #ordenar por nome
l2 = sorted(lista, key=lambda item: item['sobrenome']) #ordenar por sobrenome
l3 = sorted(lista, key=lambda item: item['idade']) #ordenar por idade

exibir(l1)
exibir(l2)
exibir(l3)