"""
Crie uma classe Livro que possui os
atributos nome,	qtdPaginas,	autor	e	preço.	
- Crie os métodos getPreco para obter	o	valor	
do	preco	e	o	método setPreco para setar
um	novo	valor	do	preco.	
Crie	um	codigo	de	teste
"""

class Livro:
    def __init__(self, nome, qtdPaginas, autor):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor

    def getPreco(self):
        self.preco = float(input(f"Qual o valor do livro {self.nome}: "))

    def setPreco(self, preco):
        self.novo_preco = preco - (10/100 * preco)


livro = Livro("O dia do amanhã", 450, "Jeová")
livro.getPreco()
livro.setPreco(livro.preco)

print(livro.nome)
print(livro.preco)
print(livro.novo_preco)
print(livro.qtdPaginas)
print(livro.autor)
print(livro.preco)
