"""
Classe	carro:	Implemente	uma	classe	chamada	Carro	com	as	 seguintes	propriedades:		
•Um	veículo	tem	um	certo	consumo	de	combus}vel	(medidos	em	km	/	litro)	e	
uma	certa	quanFdade	de	combus}vel	no	tanque.		
•O	consumo	é	especificado	no	construtor	e	o	nível	de	combus}vel	inicial	é	0.		
•Forneça	um	método	andar(	)	que	simule	o	ato	de	dirigir	o	veículo	por	uma	
certa	distância,	reduzindo	o	nível	de	combus}vel	no	tanque	de	gasolina.		Esse	
método	recebe	como	parâmetro	a	distância	em	km.	
•Forneça	um	método	obterGasolina(	),	que	retorna	o	nível	atual	de	 combus}vel.		
•Forneça	um	método	adicionarGasolina(	),	para	abastecer	o	tanque.		
•Faça	um	programa	para	testar	a	classe	Carro.	Exemplo	de	uso:			
meuFusca	=	Carro(15);	#	15	quilômetros	por	litro	de	combus}vel.	 meuFusca.adicionarGasolina(20);	#	abastece	com	20	litros	de	 combus}vel.		
meuFusca.andar(100);	#	anda	100	quilômetros.	
meuFusca.obterGasolina()	#	Imprime	o	combus}vel	que	resta	no	
tanque.
"""

class Carro():
    def __init__(self, consumoKmL, qtdCombustivel=0):
        self.consumoKmL = consumoKmL
        self.qtdCombustivel = qtdCombustivel

    def andar(self, distanciaKm):
        if self.qtdCombustivel <= 0:
            print("O seu carro está sem combustivel, por favor adicione gasolina para poder percorrer o trajeto.")
            return
        
        litrosGastos = distanciaKm / self.consumoKmL
        self.qtdCombustivel -= litrosGastos
        if self.qtdCombustivel <= 0:
            print("A sua gasolina acabou durante trajato, por favor coloque gasolina no carro.")
            return
        print(f'Trajeto de {distanciaKm} foi percorrida com sucesso.')

    
    def obterGasolina(self):
        if self.qtdCombustivel <= 0:
            self.qtdCombustivel = 0
        print(f"A quantidade de gasolina do tanque é de {self.qtdCombustivel:.2f} litros")

    def adicionarGasolina(self, addGasolina):
        self.qtdCombustivel += addGasolina
        print(f'Foram adicinados uma quantidade de {addGasolina} litros, ficando com uma quantidade de {self.qtdCombustivel:.2f} de litros no tanque do carro.')


meuFusca = Carro(15, 10); #	15 quilômetros por litro de combustivel.	
meuFusca.obterGasolina()
meuFusca.adicionarGasolina(20);	 # abastece com 20 litros de combustivel.		
meuFusca.andar(100); # anda 100 quilômetros.	
meuFusca.obterGasolina() # Imprime o combustivel que resta no tanque
