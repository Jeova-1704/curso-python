texto = 'Jeova'
interador = iter(texto)

while True:
    try:
        print(next(interador))
    except StopIteration:
        break



# Esse mesmo while que executa acima e é assim que funciona que no for, exemplo


for letra in interador:
    print(letra)