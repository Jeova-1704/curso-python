# """
# Iterando strings com while
# """
# #       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
# #      1110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

# nova_string = ''
# nova_string += '*L*u*i*z* *O*t*á*v*i*o'


nome = input("Digite algo que você deseja separar entre '_': ")
quantidade_letras = len(nome)
nome_novo = ''
contador = 0

while contador < quantidade_letras:
    print(f'*{nome[contador]}*')
    nome_novo += f'_{nome[contador]}'
    contador += 1

nome_novo += '*'
print(nome_novo)
print(f'O seu nome tem {quantidade_letras} caracteres')