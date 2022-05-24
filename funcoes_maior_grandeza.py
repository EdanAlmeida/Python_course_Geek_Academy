"""
FUNÇÕES DE MAIOR GRANDEZA - HIGHER ORDER FUNCTIONS (HOF):

    - Quando uma linguagem aceita suporta HOF, isso significa que podemos ter funções que retornam outras funções;
    - Ou até mesmo podemos passar funções como argumentos e criar variáveis do tipo de funções nos programas;

OBS = Na seção de funções, isso foi estudado superficialmente.
#Em Python, as funções são cidadãos de primeira classe (First Class Citizen);

#Exemplo


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


#Teste

print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))


#Nested Functions:
from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai,', 'Suma daqui,', 'Gosto muito de você,'))
    return humor() + pessoa


print(cumprimento('Thomas Turbando'))
print(cumprimento('Paula Tejando'))
print(cumprimento('Jacinto Pinto'))


#Retornando funções de outras funções:

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahaha', 'kkkkkkkkkkk', 'hehehehehe'))
    return rir

rindo = faz_me_rir()
print(rindo())

"""

#Inner Functions: podem acessar o escopo de funções externas:

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahaha', 'kkkkkkkkkkk', 'lololololololo', 'hehehehehe'))
        return f'{risada} {pessoa}'
    return dando_risada #retorna sem executar


rindo = faz_me_rir_novamente('Fernanda')

print(rindo())
print(rindo())
print(rindo())
