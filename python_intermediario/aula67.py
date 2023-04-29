"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""


def somar(x, y, z=None):
    if z is not None: 
        print(f'{x=} + {y=} + {z=}', x + y + z) 
    else:
        print(f'{x=} + {y=}', x + y ) 


somar(1, 2)
somar(3, 5)
somar(100, 200, 0)
somar(z=7, x =4, y=3)