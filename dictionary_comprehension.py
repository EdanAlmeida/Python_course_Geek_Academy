""""
DICTIONARY COMPREHENSION:

 - Se quisermor criar fazemos:
    - lista = [1, 2, 3, 4]
    - tupla = (1, 2, 3, 4)
    - set = {1, 2, 3, 4}

    - dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

Syntax =
    {chave: valor para valor for in iterável}


#Exemplos:

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {i:j ** 2 for i, j in numeros.items()}
print(quadrado)


numeros = [1, 2, 3, 4, 5]
quadrado = {i: i ** 2 for i in numeros}

print(quadrado)
# POssível fazer com tuplas e sets;
# Em dicionários não pode ter repetição de chave;



chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]:valores[i] for i in range(0, len(chaves))}
print(mistura)

#Uma string e uma lista;

"""

#Lógica condicional:

numeros = [1, 2, 3, 4, 5]
res = {i:('par' if i % 2 == 0 else 'impar') for i in numeros} #() vira o valor do dicionário;
print(res)
