# Calculadora com while

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operacao = input('Qual a operação que deseja fazer (+ - / *)? ')

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)

    except:
        print('\033[1;31mERRO! Um ou mais dos valores estão incorretos.\033[m')
        continue

    operacao_validas = '+-/*'

    if operacao not in operacao_validas:
        print('\033[1;31mERRO! Por favor digitar uma operação válida.\033[m')
        continue

    if len(operacao) > 1:
        print('\033[1;31mERRO! Por favor digite apenas um dos operadoes válidos.\033[m')
        continue

    print('Calculando a sua conta...')

    if operacao == '+':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
    elif operacao == '-':
        print(f'{num_1_float} - {num_2_float} = {num_1_float - num_2_float}')
    elif operacao == '*':
        print(f'{num_1_float} * {num_2_float} = {num_1_float * num_2_float}')
    elif operacao == '/':
        print(f'{num_1_float} / {num_2_float} = {num_1_float / num_2_float}')

    sair = input('Você deseja fechar o programa sim[S] ou não[N]?').lower() [0]
    while sair not in 'sn':
        sair = input('\033[1;31mErro!!\033[m Por favor digite corretamente. Você deseja fechar o programa? sim[S] ou não[N]: ')

    if sair == 's':
        break
    
print('Programa encerrado com sucesso.')