# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = copy.deepcopy(produtos)

for produto in novos_produtos:
    novo_preco = produto['preco'] + produto['preco'] * 0.10
    produto['preco'] = round(novo_preco, 2)

# novos_produtos = [
#     {**p, 'preco': round(p['preco'] * 1.1, 2)}      outro metodo de fazerr é tb por list comprehension (comprenssão de listas)
#     for p in copy.deepcopy(produtos)]




# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted( #ordena os valores de acordo com o nome em forma decrescente e aida faz uma copia profunda dos valores
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)





print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')