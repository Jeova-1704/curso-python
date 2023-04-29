"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

#Definição:
def soma(x, y, z):
    print(f'{x=} + y={y} z={z} | x + y + z = {x + y +z}')


soma(3, 4, 3)
soma(y=4, z=3, x=3)