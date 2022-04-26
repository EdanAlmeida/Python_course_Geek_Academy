"""
LISTAS ANINHADAS: NESTED LISTS

 - Algumas linguagens possuem uma estrutura da dados chamdas de 'arrays';
    - unidimensionais (arrays/vetores) ou multidimensionais (matrizes);

Em Python nós temos listas:

numeros = [1, 2, 3, 4, 5] - posso misturar tipos de dados em Python;


listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #Matriz 3 X 3 em outras linguagens;

print(listas)
print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0]) #Imprime o índice [0] de cada lista;
print(listas[0][1])
print(listas[2][2])

#Iterando com loops em uma lista aninhada;
for i in listas:
    print(i)

for i in listas:
    for j in i:
        print(j)


#Iterando com loops em uma lista aninhada;
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #Matriz 3 X 3 em outras linguagens;

#List comprehension: Pythonico
[[print(valor) for valor in lista] for lista in listas]

"""

#Gerando um tabuleiro 3X3 (matriz):

tabuleiro = [[i for i in range(1, 4)] for j in range(1,4)]
print(tabuleiro)

#Gerando jogadas para o jogo da velha:
velha = [['X' if i % 2 == 0 else 'O' for i in range(1, 4)] for j in range(1, 4)]
print(velha)


#Gerando valores iniciais:
print([['*' for i in range(1, 4)] for j in range(1, 4)])
