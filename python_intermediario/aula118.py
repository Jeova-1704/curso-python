# Problema dos parâmetros mutáveis em funções Python
def adiciona_cliente(nome, lista=[]):
     lista.append(nome)
     return lista

lista1 = []
cliente1 = adiciona_cliente("Jeová", lista1)
adiciona_cliente('Joana', lista1)
print(lista1)

lista2 = []
cliente2 = adiciona_cliente('a', lista2)
adiciona_cliente('b', lista2)
print(lista2)
