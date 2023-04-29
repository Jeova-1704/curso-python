"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra = 'paralelepipado'
palavra_secreta = '*' * len(palavra)
tentativa, acertos, erros = [0, 0, 0]
linha = '\033[1;31m=\033[m'

while True:
    print(linha * len('palavra ' + palavra_secreta))
    print(f'palavra {palavra_secreta}')
    print(linha  * len('palavra ' + palavra_secreta))

    letra = input('Digite uma letra: ')
    while len(letra) > 1:
        letra = input('ERRO! Digite apenas uma letra: ')

    if letra in palavra:
        for i in range(len(palavra)):
            if letra == palavra[i]:
                palavra_secreta = palavra_secreta[:i] + letra + palavra_secreta[i+1:]
                acertos +=1
                tentativa +=1   
                continue

    else:
        print(f'A letra {letra} não está contida na palavra.')
        erros += 1
        tentativa +=1

    if palavra_secreta == palavra:
        os.system('cls')
        print('Parabéns! Você completou e acertou a palavra.')
        print('A palavra secreta era', palavra)
        print(f'Os seus dados sobre o jogo é são: {tentativa=}, {erros=} e {acertos=}')
        break

