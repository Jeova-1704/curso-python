"""Classe	Triangulo:	Crie	uma	classe	que	modele	
um	triangulo:		
- Atributos:	LadoA,	LadoB,	LadoC
- Métodos:	calcular	Perímetro,	getMaiorLado;		
Crie	um	programa	que	uFlize	esta	classe.	Ele	deve	
pedir	ao	usuário	que	informe	as	medidas	de	um	
triangulo.	Depois,	deve	criar	um	objeto	com	as	
medidas	e	imprimir	sua	área	e	maior	lado.
"""


class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcular_perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC
    
    def getMaiorLado(self):
        return max(self.ladoA, self.ladoB, self.ladoC)
    

ladoA = float(input("digite o valor de um dos lados de um triângulo: "))
ladoB = float(input("digite o valor de outro lados de um triângulo: "))
ladoC = float(input("digite o valor do ultimo lado de um triângulo: "))

triangulo = Triangulo(ladoA, ladoB, ladoC)

print(f"O perimetro do triângulo de lados {ladoA}, {ladoB} e {ladoC} é de {triangulo.calcular_perimetro()}")
print(f'O maior lado, desse mesmo tiângulo, é de {triangulo.getMaiorLado()}')
