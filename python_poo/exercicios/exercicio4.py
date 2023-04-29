"""
Implemente uma classe Aluno,	que deve ter os
seguintes atributos:	nome,	curso,	tempoSemDormir
(em horas).		Essa classe deverá ter os seguintes
métodos:	
- estudar	(que recebe como parâmetro	a	qtd	de	horas	de	
estudo	e	acrescenta tempoSemDormir	)	
- Dormir	(que recebe como parâmetro	a	qtd	de	horas	de	
sono	e	reduz tempoSemDormir	)	
Crie	um	código	de	teste	da	classe,	criando	um	objeto
da	classe aluno	e	usando os métodos estudar	e	dormir.	 Ao	final	imprima quanto	tempo	o	aluno está sem
dormir
"""
class Aluno():
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir
    
    def estudar(self, qtdDeHorasDeEstudo):
        self.tempoSemDormir += qtdDeHorasDeEstudo
    
    def dormir(self, horasDeSono):
        self.tempoSemDormir -= horasDeSono


aluno = Aluno("Jeová", "Engenharia de Software", 10) # Cria um objeto aluno
aluno.estudar(5) # O aluno estudou por 5 horas
aluno.dormir(3) # O aluno dormiu por 3 horas
print("O aluno está sem dormir há", aluno.tempoSemDormir, "horas") # Imprime o tempo sem dormir do aluno
