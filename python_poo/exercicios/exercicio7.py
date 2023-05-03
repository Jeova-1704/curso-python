"""
Implemente a classe Disciplina no módulo escola.py
e crie um módulo de teste para ela. Um objeto é iniciado 
com o nome e as duas notas do aluno (entre 0,0 e 10,0) na 
disciplina em questão. O método calcularMedia() retorna 
a média aritmética do aluno na disciplina, enquanto o método 
exibirSituacao() retorna se o aluno está Aprovado, Em 
Recuperação ou Reprovado, considerando a média 6,0.
"""
class Diciplina():
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcularMedia(self):
        print(f'Disciplina: {self.nome}')
        self.media = sum(self.notas) / len(self.notas)

    def exibirSituacao(self):
        if self.media < 6.0:
            print('Situcção: REPROVADO') 
        else:
            print('Situcção: APROVADO') 



mat = Diciplina('Matemática', [0,10.0])
mat.calcularMedia()
mat.exibirSituacao()
print('Média:', mat.media)

