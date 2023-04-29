"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escorpos externos.
A palavra global faz uma varivel do escopo  externo ser a mesma da interna.
Tenho acesso as coisas dos escopos externos no interno 
"""

x = 3 #variale global


def escopo():
    global x #muda a variavel x para ser global com o valor mudado abaixo na funçao
    x = 7 #escorpo interno / local
    def outrafuncao():
        y = 2 #escorpo interno / local
        print(x, y)
    
    
    outrafuncao()
    print(x)



print(x)
escopo()
print(x)
