'''
listas dentro de listas
'''


salas = [
    #0         #1       #2
    ['Maria', 'Helena', 'Joaquina'], #0
    #0
    ['Quimica'], #1
    #0         #1       #2   
    ['José', 'Jeová', 'Pedro'], #2

]

# print(salas[0])
# print(salas[2][2])
# print(salas[0][1])
# print(salas[2][3][2])

for sala in salas:
    print('A sala é ', sala)
    for aluno in sala:
        print(aluno)