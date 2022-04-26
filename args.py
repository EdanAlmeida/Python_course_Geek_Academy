"""
ENTENDENDO O *ARGS:

- parametro especial de funções. Isso significa que podera chamar de qualquer coisa desde que comece com *;
- Foi deter minado pela comunidade o nome *args;
- Definição = coloca valores extras infomrados com entrada em um 'Tupla'. Tuplas são imutáveis.


def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))


# Entendendo o *args:

def soma_todos_numeros(*args):
    print(args)


soma_todos_numeros()
soma_todos_numeros(1)
soma_todos_numeros(1, 2)
soma_todos_numeros(1, 2, 3)
soma_todos_numeros(1, 2, 3, 4)


def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2))
print(soma_todos_numeros(1, 2, 3))
print(soma_todos_numeros(1, 2, 3, 4))


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2))
print(soma_todos_numeros(1, 2, 3))
print(soma_todos_numeros(1, 2, 3, 4))


def soma_todos_numeros(nome, email, *args):
    return sum(args)


print(soma_todos_numeros('Edan Almeida', 'edluis@gmail.com'))
print(soma_todos_numeros('Edan Almeida', 'edluis@gmail.com', 1))
print(soma_todos_numeros('Edan Almeida', 'edluis@gmail.com', 1, 2))
print(soma_todos_numeros('Edan Almeida', 'edluis@gmail.com', 1, 2, 3))
print(soma_todos_numeros('Edan Almeida', 'edluis@gmail.com', 1, 2, 3, 4))

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo, Geek!'
    return 'Eu não tenho certeza de quem voce eh!'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info('University', 3.145))


#Forma não pythonica


def soma_todos_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6]

#Desempacotador
num1, num2, num3, num4, num5, num6 = numeros

print(soma_todos_numeros(num1, num2, num3, num4, num5, num6))

"""

#Forma pythonica


def soma_todos_numeros(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6]
numeros2 = {1, 2, 3, 4, 5, 6}

print(soma_todos_numeros(*numeros))
print(soma_todos_numeros(*numeros2)) #serve para sets também

# OBS = esse asterisco serve para informar que estamos passando como argumeto uma coleção de dados;
# O python entende que precisa desempacotar esses dados antes de atribuir aos argumentos;
# Isso NÃO funciona com 'dictionaries'.
