"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ["João", "Maria", "Pedro", "Ana", "Lucas", "Luiza", "Fernanda", "Rafael", "Carla", "Gabriel"]

for i, nome in enumerate(lista):
    print(f'Nome ⇒ {nome} / Indice ⇒ {i}')
    
    
 # Ou pode ser feito assim:   

    # indice = 0

# for nome in lista:
#     print(f'Nome ⇒ {nome} indice ⇒ {indice}')
#     indice += 1