# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


import os

tudo = []
desfazer = []
refazer = [] 


def lista():
    print()
    print("Lista:")
    for valor in tudo:
        print(valor)


def desfaz():
    global tudo, desfazer, refazer

    if not tudo:
        print('lista está vazia')
        return
    
    desfazer.append(tudo.pop())
    print("desfazendo o ultimo valor da lista")
    lista()


def refaz():
    global tudo, desfazer, refazer
    if not refazer:
        print('Não tem valores para serem retornados.')
        return
    refazer.append(desfazer[-1])
    desfazer.pop(-1)
    tudo.append(refazer[-1])
    refazer.pop(-1)

    lista()


def adicionar(tarefa):
    global tudo, desfazer, refazer
    tudo.append(tarefa)


while True:
    print()
    print("Comandos:\n 1: 'listar'--mostra toda a lista\n 2: 'desfazer'--apaga o ultimo item da lista\n 3: 'refazer'--volta o ultimo item da lista")
    tarefa = input(("Digite uma tarefa ou comando: ")).strip().lower()
    
    if tarefa == 'listar':
        lista()
        continue

    if tarefa == 'clear':
        os.system("cls")
        continue

    if tarefa == 'desfazer':
        desfaz()
        continue

    if tarefa == 'refazer':
        refaz()
        continue

    else:
        adicionar(tarefa)




