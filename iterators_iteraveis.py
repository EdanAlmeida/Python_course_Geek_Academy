"""
Iterators and Iterables:

    - Iterators <> Iterable
        - Iterator -> elemento da programação que pode ser iterado.
            - retorna um dado por vez (função next()) for chamada;
        Iterable -> Um objeto que irá retornar um iterator quando a (função iter()) for chamada.

EX:
nome = 'Edan' #Iterable
numeros = [1, 2, 3, 4, 5, 6] #Iterable

#print(nome)
#print(numeros)

iter1 = iter(nome)
iter2 = iter(numeros)

#print(next(nome)) #Erro
#print(next(numeros)) #Erro
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print()

print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))
print(next(iter2))

"""

nome = 'Edan'

for i in nome:
    print(i)
