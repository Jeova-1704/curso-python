# gerator expression, interables e interators em python 
import sys

inteble = ['Eu', 'Tenho', '__iter__']
interator = iter(inteble) #Tem __inter__ e __next__
# lista = [n for n in range(10000)]
generator = (n for n in range(101))

# print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)
