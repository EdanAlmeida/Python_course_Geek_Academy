"""
LISTAS EM PYTHON:

 - Listas funcionam como vetores/matrizes (arrays);
 - Com diferença de serem "DINÂMICO" e aceitar "QUALQUER" tipo de dado;
    - Dinâmicos:
        - C/Java = tamanho e tipo de dados fixos;
        - Em Python é diferente == não há tamanho fixo e nem tipo estático de dados;
        - Enquanto houver memória suficiente é possível aumentar a lista;
        - Qualquer tipo de dado: as listas aceitam todos os tipos de dados;
        - AS listas são representadas por colchetes: [].

EX: print(type([]))
    print(type([1, 2, 3, 'a', 1.56]))

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['E', 'd', 'a', 'n', '', 'A', 'l', 'm', 'e', 'i', 'd', 'a']
lista3 = []
lista4 = list(range(11))
lista5 = list('Edan Almeida')

#Podemos facilmente checar valores na lista

if 8 in lista4:
    print('Encontrei o numero 8!')
else:
    print('Nao encontrei o numero 8!')


num = int(input('Digite um número inteiro: '))
if num in lista4:
    print(f'Encontrei o numero {num}!')
else:
    print(f'Nao encontrei o numero {num}!')


if 'a' in lista2:
    print('Encontrei a letra "a"!')
else:
    print('Nao encontrei a letra "a"!')

- dir(lista5) #Métodos e propriedades que dá pra usar com a lista;


#Podemos facilmente ordenar uma lista:
lista1.sort()
print(lista1)

#Podemos facilmente contar o nº de ocorrências:
print(lista1.count(1))
print(lista5.count('a'))

#Adicionar elementos em uma lista:
#Append == 1 elemento por vez
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1])
print(lista1) #Lista dentro de lista == qualquer tipo de dado

#Extend == mais de um elemento por vez na mesma lista
lista1.extend([123, 45, 66, 69, 77, 88])
print(lista1)


#Podemos facilmente ordenar uma lista:
lista1.sort()
print(lista1)

#Podemos facilmente contar o nº de ocorrências:
print(lista1.count(1))
print(lista5.count('a'))

#Adicionar elementos em uma lista:
#Append == 1 elemento por vez
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1])
print(lista1) #Lista dentro de lista == qualquer tipo de dado

#Extend == mais de um elemento por vez na mesma lista
lista1.extend([123, 45, 66, 69, 77, 88])
lista1.extend('Edan Almeida') #cada letra vira um elemento da lista;
print(lista1)


#Podemos inserir um novo elemento na lista pela posição do índice;
#Esse procedimento não substitui o valor que está na posição, este é movido para a direita;
lista1.insert(2, 'Novo Valor')
lista1.insert(0, 21)
print(lista1)

#Podemos juntar duas listas;
lista6 = lista1 + lista2
print(lista6)
lista1.extend(lista2)
print(lista1)
lista1.reverse()
print(lista1)
print(lista1[::-1]) #slice de lista


#Copiar lista:
lista6 = lista2.copy()
print(lista6)


#Saber o numero de elementos de uma lista:
print(len(lista2))

#Podemos remover o último elemento de uma lista:
print(lista5)
lista5.pop()
print(lista5)
print(lista5.pop()) #exibe o retorno do elemento removido.

#Podemos remover um elemento pelo índice: (Os elementos são deslocados, não deixando espaço vazio;)
lista5.pop(2)
print(lista5)

#É possível fazer operações com listas (+ - * /);


#Podemos remover todos os elementos:
print(lista5)
lista5.clear()
print(lista5)


#Podemos converter strings em listas:
#EX 1:
curso = 'Programacao em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

#Por padrão o split separa os elementos da lista pelo espaço enre elas;

#EX 2:

curso = 'Programacao, em, Python:, Essencial'
print(curso)
curso = curso.split(',') #especifica que o separador é a ',';
print(curso)


#Converter lista em string:
print(lista6)
curso = ' '.join(lista6) #Coloca espaço entre os elementos e converte em string;
print(curso)
curso = '$'.join(lista6)
print(curso) #separador diferente

#Podemos usar quaisquer tipos de dados em listas, inclusive misturando os dados;
print(lista7)


#Iterando sobre listas:
#EX 1: utilizando for
soma = 0
for i in lista1:
    soma = soma + i
    print(i)
print(soma)

#EX 2: Utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


#Utilizando variáveis em listas:
numeros = [1, 2, 3, 4, 5]
print(numeros)


lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['E', 'd', 'a', 'n', '', 'A', 'l', 'm', 'e', 'i', 'd', 'a']
lista3 = []
lista4 = list(range(11))
lista5 = list('Edan Almeida')
lista6 = ['Programacao', 'em', 'Python:', 'Essencial']
lista7 = [1, 2.75, True, 'd', [1, 2, 3,], 34763475]


#Fazemos acesso aos elementos de forma indexada:
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])

# Podemos acessar os elementos de forma indexada inversa:
print(cores[-1]) #sentido antihorário;
print(cores[-3])


for i in cores:
    print(i)

print()
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

#O 'for' é mais apropriado pq já sabemos o nº de elementos, eu acho, pelo menos;


#Fazemos acesso aos elementos de forma indexada:
cores = ['verde', 'amarelo', 'azul', 'branco']

# Gerar índice em um for;
for indice, cor in enumerate(cores):
    print(indice, cor)

#Enumerate = gera pares chave (indice) e valor (cor);

# Listas aceitam valores repetidos <> algumas coleções em Python não aceitam;



# Outros métodos:
#Encontrar o indice de um elemento na lista:

numeros = [5, 6, 7, 8, 5, 9, 10]
print(numeros.index(6))
print(numeros.index(9))

#Se houver repetição de valores, essa busca pegará o primeiro disponível na lista;

#Podemos fazer busca dentro de um range:
print(numeros.index(5, 2))


#Revisão de slicing

# lista[inicio:fim:passo]
#range[inicio:fim:passo]

#Parametro inicio;

lista = [1, 2, 3, 4]
print(lista[1:]) #iniciando no pindice 1 e pegando todos os elementos restantes
print(lista[:]) #Todos os elementos
print(lista[-1:])

#Parametro fim;
print(lista[:2]) #índice (2 - 1) - não incluso
print(lista[:-1])

#Parametro passo;
print(lista[1::2]) #começa no 1 e vai até o final de dois em dois
print(lista[::-1])


#Invertendo valores em uma lista;
nomes = ['Edan', 'Almeida']
nomes.reverse()
print(nomes)


#Soma*, valor máximo*, valor mínimo*, tamanho:
# *valores inteiros ou reais:

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

#Transformar lista em tupla:
print(lista)
print(type(lista))

tuple = tuple(lista)
print(tuple)
print(type(tuple))

#desempacotamento de lista:
list = [1, 2, 3]
num1, num2, num3 = list
print(num1)
print(num2)
print(num3)

"""

#SHALLOW COPY AND DEEP COPY:

#Deep copy = listas independentes;
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)
nova.append(4)
print(lista)
print(nova)
print()

#Shallow copy = listas dependentes;
lista2 = [9, 8, 7]
print(lista2)

nova2 = lista2
nova2.append(6)
print()
print(lista2)
print(nova2)
#Ambas as listas recebem o valor 6, ou seja, se alterar uma, a outra também sofre alterações.
