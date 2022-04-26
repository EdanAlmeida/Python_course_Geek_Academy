"""
MAP:

 - <> dictionary.
 - mapear de valores para função.
 -


import math

def area(r):
    #Calcula a área de um círculo com raio 'r'
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))
raios = [2, 5, 7.1, 0.3, 10, 44]

#Forma comum de calcular
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)
print()
print()


#Forma MAP:
#Função que recebe dois parâmetros: o Primeiro a função (area) e o segundo um iterável (raios).
areas = map(area, raios)

print(areas)
print(type(areas))
print(list(areas)) #convertendo para lista;
print(tuple(areas)) #convertendo para tupla;

print(list(map(area, raios)))

#O map mapeia uma função para um iterável.
#Geralmente não se usa o map com uma função comum, mas sim com uma função lambda;


import math

#MAP com lambda: reduz o numero de linhas consideravelmente.

raios = [2, 5, 7.1, 0.3, 10, 44]
print(list(map(lambda r: math.pi * (r ** 2), raios)))

#Após utilizar a função mpa, após o resultado e ele zera.
# Limpa a memória.

"""

# Para fixar o MAP:
# Temos dados iteráveis:
#dados: a1, a2, a3, ..., an
# Temos uma função:
# Função: f(x)
#Utilizamos a função map(f, dados) one map inrá mapear cada elemento dos dados e aplicar a função
# O map object: f(a1), f(a2), f(a3), f(an)...


# Lista contendo tuplas:

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]

print(cidades)

#Em fahrenheit = f = 9/5 * c + 32

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))

#MAP = função e o iterável;

# print(list(map((lambda dado: (dado[0], (9/5) * dado[1] + 32), cidades)))) #ver como ajeitar
