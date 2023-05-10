"""
Crie uma classe Loja com os métodos adicionar_produto, listar_produtos e comprar_produto. Em seguida, crie uma classe CarrinhoDeCompras que permita adicionar produtos ao carrinho e calcular o valor
"""
class Loja:
    def __init__(self):
        self.produtos = {}

    def adicionarProdutos(self, nome, preco):
        self.produtos[nome] =  preco
    
    def listarProdutos(self):
        for nome, preco in self.produtos.items():
            print(f'{nome}: R{preco:.2f}')
    
    def comprarProduto(self, nome):
        if nome in self.produtos:
            print(f'O produto {nome} foi comprado pelo seu valor de R${self.produtos[nome]:.2f}')
            del self.produtos[nome]
        else:
            print(f'O produto {nome} não existe em nossa loja')

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = {}

    def adicionarProduto(self, nome, preco):
        self.produtos[nome] = preco

    def calcularValor(self):
        return sum(self.produtos.values())


loja = Loja()
loja.adicionarProdutos('joia', 1500)
loja.adicionarProdutos('abacate', 15)
loja.listarProdutos()
loja.comprarProduto('abacate')
loja.listarProdutos()
carrinho = CarrinhoDeCompras()