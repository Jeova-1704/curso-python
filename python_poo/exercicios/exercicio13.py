class ContaInvestimento():
    def __init__(self, taxaDeJuros, saldoInicial):
        self.taxaDeJuros = taxaDeJuros
        self.saldoInicial = saldoInicial

    def adicionarJuros(self, tempo):
        self.tempoJuros = tempo
        self.montante = self.saldoInicial * (((1 + (self.taxaDeJuros/100)))** self.tempoJuros)
        print(f'R${self.montante:.2f}')

        
conta1 = ContaInvestimento(10, 1000)
conta1.adicionarJuros(0.5)
