"""
REDUCE:

 - A partir do Python3+, função reduce não é mais função integrada;
 - Precisamos importar e utilizar essa função a partir do módulo 'functools';

 Guido Van Rossum: utilize a função reduce se vc realmente precise dela, mas em 99% das vezes um loop for é melhor;

 - Para entender o reduce()
     - vc tem uma coleção de dados:
     dados = [a1, a2, a3, ..., an]
     - e vc tem uma função que recebe dois parâmetros:
         def funcao(x, y):
             return x * y

- Assim como map() e filter(), a função reuce recebe [função e iterável]
- reduce(funcao, dados)

     # A função reduce() funciona da seguinte forma:
         passo 1: res1 = f(a1, a2) #Aplica a função nos dois primeiros elementos da função e guarda o resultado)
         passo 2: res2 = f(res1, a3) #REsultado anterior e aplica o próximo elemento e guarda o resultado);

     # Isso é repetido até o final.
         passo 3: res3 = f(res2, a4) # até o 'an';

Ou seja, em cada passo, aplica-se a função passando como primeiro argumento o resultado da aplicação anterior;
No final reduce() retorna o resultado final;

"""

#Exemplo:

from _functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

#Precisamos de uma função que receba dois parâmetros
multi = lambda x, y: x * y        #pode ser uma função comum 'def'

res = reduce(multi, dados)

print(res)

#Não precisa converter para lista ou tupla;


res = 1
for n in dados:
    res = res * n

print(res)
