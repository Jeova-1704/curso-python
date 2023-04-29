# try except, else e finally
try:
    print('Abrir arquivo')
    print(8/0)
except ZeroDivisionError:
    print('Dividindo por zero')
else: # Quando o codigo não deu erro
    print('Não deu erro')
finally:
    print('Fechar arquivo')
