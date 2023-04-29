# try except, else e finally

try:
    a = 18
    b = 7
    print('Linha 1')
    c = a / b 
    print('linha 2')

except ZeroDivisionError as e:
    print(e)
    print(e.__class__.__name__)
    print('Dividiu por zero')
except NameError as n:
    print(n)
    print(n.__class__.__name__)
    print('O "b" não está definido')
except TypeError as error:
    print('TypeErro')
    print('MSG: ', error)
    print('nome:', error.__class__.__name__)
except Exception: #Trata o erro de todas as classes
    print('Erro desconhecido')

print('FIM')