"""
MIN - MAX:

 - max() = retorna o maior valor de um iterável;
     - retorna o maior de dois ou mais elementos.


#Exemplos MAX:
lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario)) #chave == 'f'

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values())) #chave

print(max(3, 34))

#Programa receber 2 valores e mostrar o maior:

val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))
print(max(val1, val2))




 - min() = retorna o menor valor de um iterável;
    - retorna o menor de dois ou mais elementos.

#Exemplos MIN:
lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario)) #chave == 'f'

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values())) #chave

print(min(3, 34))

#Programa receber 2 valores e mostrar o maior:

val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))
print(min(val1, val2))


#Outros exemplos
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(min(nomes))
print(max(nomes))
print()

print(max(nomes, key=lambda x: len(x)))
print(min(nomes, key=lambda y: len(y)))

"""

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Sweet Child O'mine", "tocou": 5},
    {"titulo": "Fear of the Dark", "tocou": 2},
    {"titulo": "Little Wings", "tocou": 6}
]

print(max(musicas, key=lambda musica: musica["tocou"]))
print(min(musicas, key=lambda musica: musica["tocou"]))

#DESAFIO:

print(max(musicas, key=lambda musica: musica["tocou"])["titulo"])
print(min(musicas, key=lambda musica: musica["tocou"])["titulo"])

#DESAFIO2: Encontrar a música + tocada e - tocada sem usar min() max() ou lambda?
max = 0
for musica in musicas:
    if musica["tocou"] > max:
        max = musica["tocou"]

for musica in musicas:
    if musica["tocou"] == max:
        print(musica["titulo"])

min = 999
for musica in musicas:
    if musica["tocou"] < min:
        min = musica["tocou"]

for musica in musicas:
    if musica["tocou"] == min:
        print(musica["titulo"])
