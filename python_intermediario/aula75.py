# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def dobro(num):
#     return f'O número {num} x 2 = {num * 2}'


# def triplo(num):
#     return f'O número {num} x 3 = {num * 3}'


# def quadruplo(num):
#     return f'O número {num} x 4 = {num * 4}'


# num = int(input('Digite qual número você deseja ver o seu dobro, triplo e quádruplos: '))

# num_1 = dobro(num)
# num_2 = triplo(num)
# num_3 = quadruplo(num)

# print(num_1)
# print(num_2)
# print(num_3)

#=======================================================================#
# Outra forma de fazer mais eficaz

def calculos_multiplicacao(multiplicador):
    def multiplicar(numero):
        return f'O númerro {numero} x {multiplicador} = {numero * multiplicador}'
    return multiplicar

num_1 = calculos_multiplicacao(2) #Escolhe o multiplicador 
num_2 = calculos_multiplicacao(3) #Escolhe o multiplicador
num_3 = calculos_multiplicacao(4) #Escolhe o multiplicador

print(num_1(5)) #Qual número você deseja multiplicar
print(num_2(5)) #Qual número você deseja multiplicar
print(num_3(5)) #Qual número você deseja multiplicar
