# numero_str = input("Dobrar o numero: ")

# try:
#     print("STR:", numero_str)
#     numero_float = float(numero_str) #Se o usuario digitar uma letra o codigo já é cortado aqui e já é desativado e pula para o except
#     print(f'FLOAT: {numero_float:.2f}')
#     print(f"O dobro de {numero_str} é {numero_float * 2:.2f}")
# except:
#     print("Isso não é um número.")


numero = input("num: ")

try:
    print(f"STR: {numero}")
    numero_float = float(numero) #Se o usuario digitar uma letra o codigo já é cortado aqui e já é desativado e pula para o except
    print(f"Float: {numero_float}")
    print(f"O dobro de {numero} é {numero_float * 2}")
except:
    print("Isso não é um número")