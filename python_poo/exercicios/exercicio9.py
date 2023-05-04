"""
rie uma classe chamada Retangulo, a qual possua os atributos largura e altura, e os métodos calcularPerimetro() e 
calcularArea(). No código de teste, crie um objeto e calcule, 
respectivamente, o perímetro e a área desse retângulo
"""

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcularPerimetro(self):
        return self.largura * 2 + self.altura * 2
    
    def calcularArea(self):
        return self.largura * self.altura
    
retangulo1 = Retangulo(4, 4)
print(retangulo1.calcularPerimetro())
print(retangulo1.calcularArea())
print()
retangulo1 = Retangulo(5, 6)
print(retangulo1.calcularPerimetro())
print(retangulo1.calcularArea())    
