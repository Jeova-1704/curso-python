"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
linha = '\033[1;31m=\033[m'
nome = 'Lista de compras'
listas_compras = list() #Ou pode se usar []

print(linha * 20)
print(nome.center(20))
print(linha * 20)

while True:
    escolha = input('Qual ação você deseja realizar - inserir[i], apagar[a] ou listar[l]: ').strip().lower()
    while escolha not in 'ial':
        escolha = input('ERRO! Por favor digite uma alternativa válida - inserir[i], apagar[a] ou listar[l]: ')

    if escolha == 'i': #Adicionar itens na lista
        os.system('cls')
        listas_compras.append(input('valor: ').strip())
        continue

    if escolha == 'l':
        if len(listas_compras) >= 1:
            os.system('cls')
            for i, v in enumerate(listas_compras):
                print(f'{i} → {v}')
        else:
            print('Nenhum item cadastrado na lista')

    if escolha == 'a':
        if len(listas_compras) >= 1:
            while True:
                delet = input('Indice do valor que deseja deletar: ').strip()[0]
                try:
                    delet = int(delet)
                    del listas_compras[delet]
                    os.system('cls')
                    break
                
                except ValueError:
                    print('Por favor digite número int.')
                    continue
                except IndexError:
                    print('Índice não existe na lista')
                    continue
                except Exception:
                    print('Erro desconhecido')
                    continue
        else:
            print('Não há valores na lista para ser deletada')