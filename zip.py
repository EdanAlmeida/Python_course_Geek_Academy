"""
ZIP

 - zip() = Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares.


#Exemplos:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1)
print(type(zip1))

#Sempre podemos gerar uma lista, tupla ou set:
print(list(zip1))

zip1 = zip(lista1, lista2) # tem que repetir, só usa uma vez;
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

#Ele usa a mesma quantidade de elementos de cada lista, caso uma tenha mais elementos, eles serão ignorados;
# A ordem das listas é importante;


#Podemos usar diferentes iteráveis com zip:
lista = [1, 2, 3, 4, 5]
tupla = (6, 7, 8, 9, 10)
dict = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(lista, tupla, dict.values())
print(list(zt))

#Lista de Tuplas: (*desempacotamento)
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))

"""

# Exemplos mais complexos:

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

print(list(zip(alunos, prova1, prova2)))

final = {i[0]: max(i[1], i[2]) for i in zip(alunos, prova1, prova2)} #dict comprehension;

print(final)

#Utilizando o map:
final2 = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final2))
