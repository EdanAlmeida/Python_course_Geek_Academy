""""
LIST COMPREEHENSION - 1:

 - Utilizando list comprehension, nós podemos gerar novas listas com dados processados a partir de outro iterável;
SYNTAX:
 - [dado for dado in iterável]



#Exemplos:

numeros = [1, 2, 3, 4, 5,]
res = [i * 10 for i in numeros]

print(res)


def funcao(valor):
    return valor * valor


res = [funcao(i) for i in numeros]
print(res)


# List comprehension VS loop:
#Loop

numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for i in numeros:
    numeros_dobrado = i * 2
    numeros_dobrados.append(numeros_dobrado)

print(numeros_dobrados)


#List Comprehension:
print([i * 2 for i in [1, 2, 3, 4, 5]])

"""

nome = 'Edan Almeida'
print([letra.upper() for letra in nome])

amigos = ['maria', 'julia', 'lucas', 'vanessa', 'pedro']
print([amigo.title() for amigo in amigos])
print([amigo[0].upper() for amigo in amigos])


def nome_maiusculo(nome):
    return nome.title()


amigos = ['maria', 'julia', 'lucas', 'vanessa', 'pedro']
print([nome_maiusculo(amigo) for amigo in amigos])

print([i * 3 for i in range(0, 10)])

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

print([str(numero) for numero in[1, 2, 3, 4, 5]])
