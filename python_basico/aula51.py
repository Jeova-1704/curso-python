"""
Introdução ao empacotamento e desempacotamento
"""
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)

nome1, nome2, nome3 = [0, 1, 2]

nome, *resto = ['Maca', 'uva', 'banana']
print(resto)