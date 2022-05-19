"""
SORTED

- Não é a função 'sort' usado em listas;
- Podemos usar o 'sorted()' com qualquer iterável;
- Ordenar os elementos;

#Exemplo: o sorted é aplicavel em Tuplas e etc.
#Ele cria uma cópia e altera ela, o original continua o mesmo;
# O sorted sempre retorna uma lista com os elementos do iterável em ordem;

numeros = [6, 8, 2]
print(numeros)
print(sorted(numeros))
print(numeros)

numeros2 = {6, 8, 2}
print(numeros)
print(sorted(numeros))

#Adicionando parâmetros ao 'sorted()':
numeros = [6, 8, 2]

print(sorted(numeros, reverse=True)) #Ordena do maior para o menor;
print(tuple(sorted(numeros)))
print(set(sorted(numeros)))


#Sorted para coisas mais complexas:
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolo", "Eu adoro pizza"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"},
]

print(usuarios)
print(sorted(usuarios, key=len))
print()

#Ordem alfabética pelo username
print(sorted(usuarios, key=lambda usuario: usuario["username"]))
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))

print()
#Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

"""

# último exemplo:
musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Sweet Child O'mine", "tocou": 5},
    {"titulo": "Fear of the Dark", "tocou": 2},
    {"titulo": "Little Wings", "tocou": 6}
]

#Da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
