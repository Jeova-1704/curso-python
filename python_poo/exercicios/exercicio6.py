"""
    Crie uma classe Aluno,	que possui como atributo	um	nome	e	
cpf.	Crie outra classe chamada Equipe,	que possui como
atributo uma lista	de	parFcipantes	do	Fpo Aluno	e	outro	
atributo chamado projeto.	
Crie uma terceira classe chamada GerenciadorEquipes.	Essa
classe possui como atributo uma lista	de	todas	as	equipes
formadas.	Ela deverá possuir	o	método criarEquipe,	que recebe
uma lista	de	alunos	de	uma equipe	e	diz	se	a	equipe pode ser
formada ou não.	Caso não haja nenhum aluno	da	equipe	a	ser
formada em uma outra equipe	com	o	mesmo projeto,	então	a	
equipe é criada	e	acrescentada à lista.	Caso contrário é
informada que	a	equipe não pode ser criada.
"""


class Aluno:
    def __init__(self, nome, cpf):
        self.nome = cpf
        self.cpf = cpf


class Equipe:
    def __init__(self, listaParticipantes, projeto):
        self.listaParticipantes = listaParticipantes
        self.projetos = projeto


class GerenciadorEquipes:
    def __init__(self, listaEquipesFormadas):
        self.listaEquipesFormadas = listaEquipesFormadas


    def criarEquipe(self, participantes, projeto):
        for equipe in self.equipes:
            if equipe.projeto == projeto:
                for aluno in equipe.participantes:
                    if aluno in participantes:
                        print("Não é possível criar a equipe, pois um dos alunos já está em outra equipe com o mesmo projeto.")
                        return
        nova_equipe = Equipe(participantes, projeto)
        self.equipes.append(nova_equipe)
        print("Equipe criada com sucesso!")
    