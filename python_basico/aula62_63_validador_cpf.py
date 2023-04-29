# https://www.macoratti.net/alg_cpf.htm
# Codigo do primeiro digito:

import sys

cpf_enviado_usuario = input('CPF: ').strip()
if len(cpf_enviado_usuario) == 14: 
    nove_digitos = cpf_enviado_usuario[:11].replace('.', '')
elif len(cpf_enviado_usuario) == 11:
    nove_digitos = cpf_enviado_usuario[:9]
    cpf_enviado_usuario = nove_digitos[:3] + '.' + nove_digitos[3:6] + '.' + nove_digitos[6:] + '-' + cpf_enviado_usuario[9:]

entrada_e_sequencial = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()


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

#codigo de verificação do segundo digito

dez_digitos = nove_digitos + str(penultimo_digito)
contador_2 = 11
soma_digitos_2 = 0

for num in dez_digitos:
    soma_digitos_2 += int(num) * contador_2
    contador_2 -= 1

resto_divisao_2 = soma_digitos_2 % 11

if resto_divisao_2 < 2 :
    ultimo_digito = 0
else:
    ultimo_digito = 11 - resto_divisao_2

cpf_final = nove_digitos[:3] + '.' + nove_digitos[3:6] + '.' + nove_digitos[6:] + '-' + str(penultimo_digito) + str(ultimo_digito)

if cpf_enviado_usuario == cpf_final:
    print(f'O seu CPF {cpf_enviado_usuario} é válido')
else:
    print(f'O seu CPF {cpf_enviado_usuario} NÃO é válido')