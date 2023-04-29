# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum = 10):
    while True:
        yield n
    
        n += 1
        if n > maximum:
            return
        
        
    # yield 1 #pausar 
    # print("Continuando...") # Continua a partir daqui só se chamar next de novo
    # yield 2
    # print("Mais uma vez")


gen = generator()
# print(next(gen))
# print() # Penas para separar os codigos para uma melhor analise
# print(next(gen))

for n in gen: # for que retorna os valores de acordo com os yield da função generete
    print(n)



# =====================================================================



# def generator(n=0, maximum = 10):
#     yield 1 #pausar 
#     print("Continuando...") # Continua a partir daqui só se chamar next de novo
#     yield 2
#     print("Mais uma vez")


# gen = generator()
# print(next(gen))
# print() # Penas para separar os codigos para uma melhor analise
# print(next(gen))