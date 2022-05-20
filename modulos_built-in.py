"""
MODULOS BUILT-IN:

    - módulos integrados no python;
      ____________________________
    - |Python|Módulos Built-in|;
    ------------------------------

#Utilizando 'alias' (apelidos) para módulos/funções:
import random as rdm

print(rdm.random())


#Podemos importar todas as funções de um módulo usando o '*';
from random import *
print(random())


#Alias para funções:
from random import randint as rdi

print(rdi(1, 5))


#Alias para funções:
from random import randint as rdi,  random as rdm

print(rdi(1, 5))
print(rdm())


#Costumamos usar tuple para muitos imports do mesmo módulo:
from random import (
    randint,
    random,
    choice,
    shuffle,
    uniform
)

print(random())

"""


