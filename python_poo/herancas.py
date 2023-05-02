class Pessoa:
    
    def __init__(self,nome, cpf, altura):
          self.cpf = cpf
          self.altura = altura
          self.nome = nome
          print('teste')


class Secretatia(Pessoa):
    def __init__(self, id_secretaria, nome, cpf, altura):
         super().__init__(nome, cpf, altura)
         self.idsecretaria = id_secretaria
         


class Vendedor(Pessoa):
     pass



s1 = Secretatia('123', 'Maria', '125.876.987-08', '1,68')
print(s1.__dict__)

