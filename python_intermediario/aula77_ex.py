# Exercício - sistema de perguntas e respostas

linha = '\033[1;31m=\033[m'


def formatacao(num, acertos=0):
    print(linha * 50)

    print('Pergunta:', perguntas[num]['Pergunta'])
    # print()

    print('Opções: ')
    for i, opcao in enumerate(perguntas[num]['Opções']):
        print(i, ')', opcao)
        
    escolha = input('Escolha uma resposta de acordo com indices das alternativas: ') 

    try:    
        escolha = int(escolha)
        if perguntas[num]['Resposta'] == perguntas[num]['Opções'][escolha]: 
            print('Você acertou, parabéns! ✅')
            acertos += 1
        else:
            print('\033[1;31mERRO!\033[m resposta incorreta ❌') 
    except TypeError:
        print('\033[1;31mERRO!\033[m Valor digitado não reconhecido pelo sistema ❌')
    except Exception:
        print('\033[1;31mERRO!\033[m Valor digitado não reconhecido pelo sistema ❌')

    return acertos

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5x5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Qual é o resultado da expressão 4^3?',
        'Opções': ['12', '64', '36', '16'],
        'Resposta': '64',
    },
    {
        'Pergunta': 'Qual é o valor de x na equação 3x + 5 = 20?',
        'Opções': ['5', '7', '6', '8'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Qual é o resultado da multiplicação de dois números primos?',
        'Opções': ['um número par', 'um número ímpar', 'um número primo', 'um número composto'],
        'Resposta': 'um número composto',
    },
    {
        'Pergunta': 'Qual é o valor de x na equação 2x - 3 = 7x + 1?',
        'Opções': ['-0.67', '0.67', '0.5', '-0.5'],
        'Resposta': '-0.67',
    },
    {
        'Pergunta': 'Qual é a raiz quadrada de 121?',
        'Opções': ['11', '12', '13', '14'],
        'Resposta': '11',
    },
    {
        'Pergunta': 'Qual é o resultado da expressão (5x6)/(3+2)?',
        'Opções': ['3', '5', '6', '7'],
        'Resposta': '6',
    },
    {
        'Pergunta': 'Qual é o maior país do mundo em área territorial?',
        'Opções': ['Canadá', 'China', 'Rússia', 'Estados Unidos'],
        'Resposta': 'Rússia',
    },
    {
        'Pergunta': 'Em que país fica a Torre Eiffel?',
        'Opções': ['Itália', 'França', 'Espanha', 'Alemanha'],
        'Resposta': 'França',
    },
    {
        'Pergunta': 'Qual é o país mais populoso do mundo?',
        'Opções': ['Índia', 'Estados Unidos', 'China', 'Brasil'],
        'Resposta': 'China',
    },
    {
        'Pergunta': 'Qual é o nome da capital do Japão?',
        'Opções': ['Tóquio', 'Osaka', 'Kyoto', 'Nagasaki'],
        'Resposta': 'Tóquio',
    },
    {
        'Pergunta': 'Quem foi o primeiro presidente do Brasil?',
        'Opções': ['Getúlio Vargas', 'Juscelino Kubitschek', 'Dilma Rousseff', 'Deodoro da Fonseca',],
        'Resposta': 'Deodoro da Fonseca',
    },
    {
        'Pergunta': 'Qual é a maior cordilheira do mundo?',
        'Opções': ['Andes', 'Alpes', 'Himalaias', 'Cordilheira dos Apalaches'],
        'Resposta': 'Himalaias'
    }
]

pontuacao = 0
quantas_vezes_perguntar = len(perguntas)

for cont in range(0, quantas_vezes_perguntar):
    pontuacao += formatacao(cont)

print(f'Jogo encerrado. Você acertou um total de {pontuacao} de {quantas_vezes_perguntar} perguntas.')