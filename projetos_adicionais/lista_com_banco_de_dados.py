# Exercício - salvar as listas em arquivos json


import os
import json

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
    refazer.append(desfazer[-1])
    desfazer.pop(-1)
    tudo.append(refazer[-1])
    refazer.pop(-1)

    lista()


def adiciona():
    global tudo, desfazer, refazer
    item = input("O qeu deseja adicionar na lista: ").strip()
    tudo.append(item)


def salva():
    # global tudo, desfazer, refazer
    # with open("aula119.json", 'w') as file:
    #     json.dump(
    #         tudo, file,
    #         indent=2
    #         )
    global tudo, desfazer, refazer
    with open("aula119.json", 'w') as file:
        json.dump(
            {"tudo": tudo, "desfazer": desfazer, "refazer": refazer},
            file,
            indent=2
        )
    print("Listas salvas com sucesso!")


def carrega():
        global tudo, desfazer, refazer
        with open("aula119.json", 'r', encoding='utf-8') as file:
        # Carrega as listas do arquivo JSON
            listas = json.load(file)
        
        # Atribui os valores das listas do arquivo JSON às variáveis globais
            tudo = listas["tudo"]
            desfazer = listas["desfazer"]
            refazer = listas["refazer"]
        
            lista()
 

def apaga():
    global tudo, desfazer, refazer
    with open("aula119.json", 'w') as file:
        file.truncate()
    tudo = []
    desfazer = []
    refazer = []
    print("Banco de dados da lista apagado com sucesso")

while True:
    print()
    print("Comandos:\n 1: 'listar'--mostra toda a lista\n 2: 'desfazer'--apaga o ultimo item da lista\n 3: 'refazer'--volta o ultimo item da lista\n 4: 'Salvar'--salva a lista no banco de dados\n 5: 'carregar'--carrega a ultima lista feita do banco de dados\n 6: 'apagar'--apaga toda a lista do banco de dados\n 7: 'adicionar'--adiciona um item na lista\n 8: 'sair'--fecha o programa")
    tarefa = input(("Digite um comando: ")).strip().lower()
    
    if tarefa == '1':
        lista()
        continue

    if tarefa == 'clear':
        os.system("cls")
        continue

    if tarefa == '2':
        desfaz()
        continue

    if tarefa == '3':
        refaz()
        continue

    if tarefa == '4':
        salva()
        continue

    if tarefa == '5':
        carrega()
        continue

    if tarefa == '6':
        apaga()
        continue

    if tarefa == "7":
        resposta = 's'
        while resposta == 's':
            adiciona()
            resposta = input("Deseja digitar outro valor [S/N]? ").lower()
            if resposta == 'n':
                break
    
    if tarefa == "8":
        break
            

    else:
        print("Digite um dos itens válidos acima.")



