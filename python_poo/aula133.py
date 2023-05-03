# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
class foo:
    def __init__(self):
        self.public = 'Isso é publico'
        self._protected = 'Isso é protegido'
        self.__private = "Isso é privado"

    def metodo_publico(self):
        return 'Metodo_publico'
    
    def _metodo_protected(self):
        return '_metodo_protected'
    
    def __metodo_private(self):
        return '__metodo_private'


f = foo()
# print(f.public)
# print(f.metodo_publico())
print(f._metodo_protected())
print(f.__metodo_private()) #Não se pode usar metodos fora de classe