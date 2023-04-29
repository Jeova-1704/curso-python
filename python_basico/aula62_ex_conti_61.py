# https://www.macoratti.net/alg_cpf.htm
# Codigo do primeiro digito:

cpf = input('CPF: ').strip()
if len(cpf) == 14: 
    nove_digitos = cpf[:11].replace('.', '')
elif len(cpf) == 11:
    nove_digitos = cpf[:9]

soma_digitos = 0
contador = 10

for num in nove_digitos:
    soma_digitos += int(num) * contador
    contador -= 1

resto_divisao = soma_digitos % 11

if resto_divisao < 2:
    penultimo_digito = 0

else:
    penultimo_digito = 11 - resto_divisao

print(f'O primeiro dos dois digitos verificadores: {penultimo_digito}')



"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

#Codigo do segundo digito:

novo_cpf = nove_digitos + str(penultimo_digito)
print(novo_cpf)
contador_2 = 11
soma_digitos_2 = 0

for num in novo_cpf:
    soma_digitos_2 += int(num) * contador_2
    contador_2 -= 1

resto_divisao_2 = soma_digitos_2 % 11

if resto_divisao_2 < 2 :
    ultimo_digito = 0
else:
    ultimo_digito = 11 - resto_divisao_2
print(ultimo_digito)
