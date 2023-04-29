# lista comprehension com mais de um for
lista = []
for x in range(3):
    for y in range(3):
        lista.append((f'{x=}, {y=}'))

#ou podemos fazer dessa outra forma 

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

lista = [
    [letra for letra in 'Jeová']
    for x in range(3)
]

print(lista)