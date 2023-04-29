"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome >= 2:
    try:
        nome_str = str(nome)
        print(nome_str)
        
        if len(nome) <= 4:
            print('O seu nome é pequeno.')
        elif 5 >= len(nome) <= 6:
            print('O seu nome é normal.')
        else:
            print('O seu nome é muito grande.') 

    except:
        print('Digite um nome válido.')
else:
    print(f'"{nome}" não pode ser considerado um nome, digite um nome válido.')