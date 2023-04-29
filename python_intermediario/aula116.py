# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita mas não salva e apaga), x (para criação)
# a (escreve ao final e cotinua o arquivo), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'C:\\Users\\jeova\\OneDrive\\Área de Trabalho\\curso_python_udemy\\'
caminho_arquivo += 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# # Sempre que abrir fecha o aquivo
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     print(type(arquivo))
#     arquivo.write("Ola mundo, estou escrevendo no arquivo, linha 1\n")
#     arquivo.write("Linha 2\n")
#     arquivo.writelines(
#         ('Linha 3 \n', '123456789\n', 'Linha final')
#     )
#     arquivo.seek(0,0)
#     # print(arquivo.read())
#     print()
#     print("Lendo:")
#     arquivo.seek(0,0)
#     print(arquivo.readline())
#     print(arquivo.readline())
#     print(arquivo.readline())
#     print(arquivo.readline())
#     print(arquivo.readline())

# print("#" * 40)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())


with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    print(type(arquivo))
    arquivo.write("Ateanção\n")
    arquivo.write("linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.writelines(
        ('Linha 3 \n', 'Linha 4')
    )

import os
#Remover e apaga os arquivos:
# os.remove(caminho_arquivo)
#Renomeia o arquivo:
# os.rename()