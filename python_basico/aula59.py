strings = 'ABCD'
lista = ['Maria', 'Helena',1, 2, 3, 4, 'Eduarda']
tuplas = 'Python', 'é', 'legal'

a, b, c, *_, at, u = lista

print(u, at)

print( *lista)
print(*strings)
print(*tuplas)