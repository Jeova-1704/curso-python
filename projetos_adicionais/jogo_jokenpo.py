#Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
from time import sleep


linha = "\033[1;31m-=-\033[m"
titulo = '\033[1;32mJOGO DE JOKENPÔ\033[m'
pontos_pc = 0
pontos_jogador = 0
empate = 0

print(linha * 20)
print(f"{titulo:^60}")
print(linha * 20)

while True:

      print('Escolha a sua jogada:\n [1] PEDRA\n [2] PAPEL\n [3] TESOURA')
      player = int(input('Qual o número de sua jogada? '))

      pc = [1, 2, 3]#1=pedra #2=papel #3=tesoura
      escolha = choice(pc)
      #print('JO...'), sleep(2), print('KEN...'), sleep(2), print('Pô!!!')
      if player == 1 and escolha == 1:#se player escolher PEDRA e pc escolher pedra
            print('-=-'*10)
            print('JOGADOR = PEDRA')
            print('  PC    = PEDRA')
            print('-=-' * 10)
            print('O JOGO DEU EMPATE!')
            empate += 1
      elif player == 1 and escolha == 2:  # se player escolher PEDRA e pc escolher papel
            print('-=-' * 10)
            print('JOGADOR = PEDRA')
            print('  PC    = PAPEL')
            print('-=-' * 10)
            print('O PC GANHOU!')
            pontos_pc +=1
      elif player == 1 and escolha == 3:  # se player escolher PEDRA e pc escolher tesoura
            print('-=-' * 10)
            print('JOGADOR =  PEDRA')
            print('  PC    = TESOURA')
            print('-=-' * 10)
            print('O JOGADOR VENCEU!')
            pontos_jogador += 1
      elif player == 2 and escolha == 1:#se player escolher PAPEL e pc escolher PEDRA
            print('-=-' * 10)
            print('JOGADOR = PAPEL')
            print('  PC    = PEDRA')
            print('-=-' * 10)
            print('O JOGADOR VENCEU!')
            pontos_jogador += 1
      elif player == 2 and escolha == 2:#se player escolher PAPEL e pc escolher PAPEL
            print('-=-' * 10)
            print('JOGADOR = PAPEL')
            print('  PC    = PAPEL')
            print('-=-' * 10)
            print('O JOGO DE EMPATE!')
            empate += 1
      elif player == 2 and escolha == 3:  # se player escolher PAPEL e pc escolhe tesoura
            print('-=-' * 10)
            print('JOGADOR =  PAPEL')
            print('  PC    = TESOURA')
            print('-=-' * 10)
            print('O PC GANHOU!')
            pontos_pc += 1
      elif player == 3 and escolha == 1:#se player escolher TESOURA e pc escolhe PEDRA
            print('-=-' * 10)
            print('JOGADOR = TESOURA')
            print('  PC    = PEDRA')
            print('-=-' * 10)
            print('O PC GANHOU!')
            pontos_pc += 1
      elif player == 3 and escolha == 2:  # se player escolher TESOURA e pc escolhe PAPEL
            print('-=-' * 10)
            print('JOGADOR = TESOURA')
            print('  PC    = PAPEL')
            print('-=-' * 10)
            print('O JOGADOR GANHOU!')
            pontos_jogador += 1
      elif player == 3 and escolha == 3:  # se player escolher TESOURA e pc escolhe TESOURA
            print('-=-' * 10)
            print('JOGADOR =  TESOURA')
            print('  PC    = TESOURA')
            print('-=-' * 10)
            print('O JOGO DEU EMPATE!')
            empate += 1
      else:
            print('Por favor insira uma opção válida!')
      jogar_novamente = input("Deseja jogar novamente? (S/N) ")
      if jogar_novamente.lower() == "n":
        break
print()
print("PONTUAçÃO FINAL:")
print(f'\033[1;32m{pontos_pc=}')
print(f'{pontos_jogador=}')
print(f'{empate=}\033[m')
