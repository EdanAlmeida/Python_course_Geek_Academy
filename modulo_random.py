"""
MODULO RANDOM:

    - O que é um módulo?
        - Módulos são outros arquivos Python.
        - Eles servem para deixar os programas mais simples e para que possamos reutilizá-los.
        - Não tente inventar a roda nunca!

    - Modulo random:
        - gerar números pseudoaleatórios;
        OBS = existe duas formas de se utilizar um módulo ou função random;


#Forma 1 - importando tudo (todas as classes, funções e atributos são importados) [ficam em memória]
#Não recomendado
# random() == gera um numero pseudo-aleatório enre 0 e 1; (função <> pacote)
import random

print(random.random())



#Forma 2 - importando uma função específica do módulo:
#O random é usado em redes neurais artificiais; (emular um cérebro humano) [Inteligência Artificial]
from random import random

for i in range(10):
    print(random())



# uniform() -> gerar um número pseudo-aleatório entre os valores estabelecidos (numeros reais);
from random import uniform

for i in range(5):
    print(int(uniform(1, 100))) #100 não incluso



#randint() -> gera valores pseudo-aleatórios entre os valores estabelecidos (inteiros);
from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')


#choice() -> mostra um valor aleatório entre um iterável:

from random import choice

jogada = ['pedra', 'papel', 'tesoura']
print(choice(jogada))

"""

#shuffle() -> tem a função de embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
shuffle(cartas)
print(cartas)
