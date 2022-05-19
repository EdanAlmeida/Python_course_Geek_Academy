"""
GENERATORS:
GENERATOR EXPRESSION.

 - Tuple comprehension == generators;
 - O generator não ertorna TUpla e retorna o resultado apenas uma vez;


# Generators

nomes = ['Carlos', 'Cristina', 'Cassiano', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))

#List comprehension ==
print()
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# GEnerator
print()
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# O generator é mais performático, ocupa menos recursos e memória;
#No caso de precisar usar os dados, é preferível o uso de lista;

#Qual é a função de 'getsizeof'? retorna a quantidade de bytes do elemento passado como parâmetro;
from sys import getsizeof

print(getsizeof('Geek'))
print(getsizeof('Almeida'))
print(getsizeof(911))

from sys import getsizeof

#List comprehension:
print()
list_comp = getsizeof([x * 10 for x in range(1000)])

#Set comprehension:
print()
set_comp = getsizeof({x * 10 for x in range(1000)})

#Dictionary comprehension:
print()
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

#Generator:
print()
gen = getsizeof(x * x for x in range(1000))

print()
print("Para fazer a mesma tarefa, gastamos em memória: ")
print(f"List Comprehension: {list_comp} bytes")
print(f"Set Comprehension: {set_comp} bytes")
print(f"Dict. Comprehension: {dict_comp} bytes")
print(f"Generator: {gen} bytes")

#Posso iterar sobre o Generator expression? SIM!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for i in gen:
    print(i)

"""

from sys import getsizeof

#List comprehension:
list_comp = getsizeof([x * 10 for x in range(1000)])

#Set comprehension:
set_comp = getsizeof({x * 10 for x in range(1000)})

#Dictionary comprehension:
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

#Generator:
gen = getsizeof(x * x for x in range(1000))

print()
print("Para fazer a mesma tarefa, gastamos em memória: ")
print(f"List Comprehension: {list_comp} bytes")
print(f"Set Comprehension: {set_comp} bytes")
print(f"Dict. Comprehension: {dict_comp} bytes")
print(f"Generator: {gen} bytes")

gen1 = (x * x for x in range(1000))
print(gen1)