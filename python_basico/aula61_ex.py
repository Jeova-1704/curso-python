"""
Calculo do primeiro dígito do CPF:

CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado anterior por 10
301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0

contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7



# https://www.macoratti.net/alg_cpf.htm
"""

cpf = input('CPF: ')
if len(cpf) > 9: 
    nove_digitos = cpf[:11].replace('.', '')
else:
    nove_digitos = cpf[:8]

soma_digitos = 0
contador = 10
penultimo_digito = 0

for num in nove_digitos:
    soma_digitos += int(num) * contador
    contador -= 1

resto_divisao = soma_digitos % 11

if resto_divisao < 2:
    penultimo_digito = 0

else:
    penultimo_digito = 11 - resto_divisao

print(f'CPF: {cpf}')
print(f'Nove digitos: {nove_digitos}')
print(f'A soma dos valores multiplicados: {soma_digitos}')
print(f'Resto do contador: começou com 10... => {contador}')
print(f'O resto da divisão: {resto_divisao}')
print(f'O primeiro dos dois digitos verificadores: {penultimo_digito}')



