import json

# Tranformando e salvando arquivos em json
# pessoa = {
#     'nome': 'Jeova ',
#     'sobrenome': 'Leite',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.73,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('aula117.json', 'w', encoding=utf8) as file:
#     json.dump(
#         pessoa, file,
#         # ensure_ascii=False,
#         indent=2
#         )


#Para trazer de volta e abrir o json
with open('aula117.json', 'r', encoding='utf8') as file:
    pessoas = json.load(file)
    print(pessoas['nome'])
