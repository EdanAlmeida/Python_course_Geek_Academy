"""
SET COMPREHENSION:

 - O princípio é o mesmo;
    set = {1, 2, 3, 4, 5}

"""

numeros = {i for i in range(1, 7)}
print(numeros)

num = {x ** 2 for x in range(10)}
print(num)

#DESAFIO = faça uma alteração na estrutura acima para gerar um dicionário;

num = {x: x ** 2 for x in range(10)}
print(num)

#String

letras = {letra for letra in 'Edan Almeida'}
print(letras)

#Lembrando que conjuntos não mantém ordenaão e nem repetição;
