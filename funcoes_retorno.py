"""
Funções com retorno:

numeros = [1, 2, 3]
ret = numeros.pop()

ret_print = print(numeros) #A função print não retorna nada
print(ret)
print(ret_print)

OBS = quando um função não retorna nenhum valor == none;
OBS = POdemos passar a execução da função para outras funções;


def quadrado_de_sete():
    print(7 * 7)
ret = quadrado_de_sete()
quadrado_de_sete() #O valor não é retorno e sim impressão
print(ret)

#Refatoração da função == redefinir/ reescrever;
def quadrado_de_seis():
    return 6 * 6
#Variável para receber o retorno;
ret = quadrado_de_seis()
print(ret)

print(f'Retorno: {quadrado_de_seis()}')
print(f'Retorno: {quadrado_de_seis() + 4}') #é possível fazer operações


#Refatorando a primeira função:
def diz_oi():
    return 'Oi, '

alguem = 'Pedro!'
print(diz_oi() + alguem) #com o retorno é possível fazer operações.

OBS = palavra reservada = 'return'.
    1 - Ela finaliza a função, ou seja, sai da execução da função;
    2 - Podemos ter em uma função, diferentes returns;
    3 - Podemos em uma função, retornar quaisquer tipos de dados, até mesmo multiplo valores;

#EX 1:


def diz_oi():
    print("Estou sendo executado antes do retorno!")
    return "Oi! " # a função é finalizada aqui;
    print("Estou sendo executado após o retorno.")


print(diz_oi())


#Ex 2:


def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    else:
        return 'b'


print(nova_funcao())


#Ex 3:


def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4) #desempacotamento

print(outra_funcao()) #Em forma de tuple


# Função para jogar a moeda (cara ou coroa):


from random import random

def joga_moeda():
    #Gera um numero pseudorandômico entre 0 e 1;
    valor = random()
    if valor > 0.5:
        return "Cara"
    else:
        return "Coroa"


print(joga_moeda())


# Função refatorada:


from random import random

def joga_moeda():
    iff random() > 0.5:
        return "Cara"
    else:
        return "Coroa"


print(joga_moeda())

"""

#Erros comuns na utilização do retorno, nem é erro, mas sim codificação desnecessária:


def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    return False          #Else é desnecessário aqui. Evitar.


print(eh_impar())
