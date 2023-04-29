def executa(funcao, *args):
    return funcao(*args)


# def soma(x, y):
#     return x + y 


def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return (numero * multiplicador)
    return(multiplica)



#criar a função soma como lambada (uma linha)
print(
    executa(
    lambda x, y:x + y, 
    2, 3
    )
)


#Criando a função multiplicador em lambda

# duplica = criar_multiplicador(2) #Por qual numerro ira ser multiplicado
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(5))