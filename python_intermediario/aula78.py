# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# l1 = [1, 3, 3, 2, 3, 1, 2, 1] #Remove os valores duplicados das listas, tuplas, diciionarios e etc
# s1 = set(l1)
# l2 = list(s1)
# print(l2) #agora temos uma lista apenas com valores unicos, sem repetição
# s1 = {1, 2, 3}
# print(s1[0]) # não tem indice para saber o valor exato
# for c in s1:
#     print(c)


# Métodos úteis
# add-adiciona um valor, update-adiciona varios valores, clear-limpa 0 set, discard-descarta um valor exato
# s1 = set()
# s1.add('Luiz')
# s1.add(1)
# s1.update(('ola mundo', 1,2,3,4))
# # s1.clear()
# s1.discard('Luiz')
# s1.discard('ola mundo')
# print(s1)


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 = s1 | s2 #une os sets
# print(s3)
# s3 = s1 & s2 #itens que estão em ambos 
# print(s3)
# s3 = s1 - s2 #item unico que esta apenas e um unico set
# print(s3)
# s3 = s1 ^ s2
# print(s3) #itens unicios nos dois e que não se repetem  



#======================================================================
# Exemplo do uso de sets

letras = set()
while True:
    letra = input('letra: ')
    letras.add(letra)

    if 'l' in letras:
        print('Parabéns.')
        break

    print(letras)