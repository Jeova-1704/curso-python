# Qual letra apareceu mais na frase

frase = 'Seu sorriso é tão resplandecente Que deixou meu coração alegre Me dê a mão Pra fugir desta terrível Escuridão'
mais_apareceu = 0
letra_apareceu_mais = ''

i= 0
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if mais_apareceu < quantas_vezes_letra_apareceu_atual:
        mais_apareceu = quantas_vezes_letra_apareceu_atual
        letra_apareceu_mais = letra_atual
    i += 1    

print(f'A letra que apareceu mais vezes foi a "{letra_apareceu_mais}" e ela apareceu "{mais_apareceu}"')