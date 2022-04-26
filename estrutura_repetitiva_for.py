"""
ESTRUTURA DE REPETIÇÃO EM PYTHON

- Loop == estrutura de repetição;
- for == um tipo de loop;

- Python == for 'item' em 'interavel':
    //execução do loop;

- Usamos os loop para iterar sobre sequências ou sobre valores iteráveis;
    - nome = 'Edan'
    - print(nome[0]) == 'E'
    - Essa string é um exemplo de iterável em Python.
    - Range também é iterável 'range(1, 10)'.
"""

#Temos que transformar em uma lista;

"""# 01 - Exemplo de 'for' (iterando sobre uma string):
for letra in nome:
    print(letra)
"""

"""# 02 - Exemplo de 'for' (iterando sobre uma lista):
for i in lista:
    print(i)
"""

"""# 03 - Exemplo de 'for' (iterando sobre um range):
for i in range(1, 10):
    print(i)

# Range == valor_inicial, valor_final;
#OBS = O valor final não está incluso (10 == 9);
"""


"""#Enumerate == ele cria uma tupla da lista == ((0. 'E'), (1, 'd'), (2, 'a'))
for i, v in enumerate(nome):
    print(nome[i])

nome = 'Edan Luis de Almeida'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for indice, letra in enumerate(nome):
    print(f'{letra} {indice}')

for _, letra in enumerate(nome):
    print(letra)
# O _ descarta o valor.

for valor in enumerate(nome):
    print(valor)


qtd = int(input('Quantas vezes esse loop deve rodar? '))
for n in range(1, qtd+1):
    print(f'Imprimindo {n}')

# Ele itera sobre a quantidade + 1;

qtd2 = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd2} valor: '))
    soma = soma + num

print(f'A soma é: {soma}')

"""
#Imprimir sem pular linha
nome = 'Edan Almeida'
for letra in nome:
    print(letra, end='')

#CTRL + clicar em cima do 'print' == documentação do 'print'

nome2 = 'Edan'
nome3 = nome2 + 'Almeida'
print(nome3)

#Concatenação de strings;
# è possível fazer operações usando strings em Python

# unicode original == U+1F643
# EM python == U0001F643

emoji = '\U0001F643'

for _ in range(3):
    for num in range(1, 11):
        print(f'{emoji * num}')
