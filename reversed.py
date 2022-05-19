"""
REVERSED:

 - Não é a função 'reverse()'.
 - A função reversed() funciona em qualquer iterável;
 - Sua função é inverter o iterável;
 - reversed() = retorna um iterável chamado 'List Reverse Iterator'
"""

lista = [1, 2, 3, 4, 5]

res = reversed(lista)
print(res)
print(type(res))

# Podemos converter esse elemento retornando para uma lista, tupla, ou conjunto

#List
print(list(reversed(lista)))

#Tuple
print(tuple(reversed(lista)))

#Set (não define ordem)
print(set(reversed(lista)))

#Podemos iterar sobre o reversed
for i in reversed("Edan Almeida"):
    print(i, end='')

print('\n')
#Mesma coisa sem o for;
print(''.join(list(reversed('Edan Almeida'))))

#Podemos utilizar o 'reversed()' para fazer um loop for reverso:
for n in reversed(range(0, 10)):
    print(n)
print()

for i in range(9, -1, -1):
    print(i)
