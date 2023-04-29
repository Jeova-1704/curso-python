"""
Exercício
Peça ao usuário para digitar seu nome 
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input("Nome: ")
idade = input("Idade: ")

if nome and idade:
    print(f"Seu nome é {nome}.")
    print(f"O seu nome invertido é {nome[::-1]}.")

    if " " in nome:
        print("O seu nome tem espaços entre as palavra.")
    else:
        print("O seu nome NÃO contém espaços e você digitou apenas o seu primeiro nome.")
    
    print(f"O seu nome tem {len(nome)} caracteres.")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é '{nome[-1]}'")
else:
    print("Desculpe, você deixou campos vazios.")