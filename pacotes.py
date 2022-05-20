"""
PACOTES:

    - Modulo -> É  um arquivo Python com diversas funções para utilizarmos;
    - Pacotes -> diretorio contendo uma coleção de módulos;
        MODULO <> PACOTE
    - Nossa pasta com os arquivos é um PACOTE;

OBS = versões 2.x do Python, um pacote deveria conter dentro dele um arquivo chamado __init__.py (dunder init dunder)
OBS = VErsões 3.x, não é mais obrigatória a utilização desse arquivo, mas ainda é utilizado por compatibilidade.

    - __init__.py -> serve para versões anteriores entenderem que se trata de um pacote.

"""

from geek import(
    geek1,
    geek2
)

from geek.university import(
    geek3,
    geek4
)

print(geek1.pi)
print(geek1.funcao1(4, 6))
print()
print(geek2.curso)
print(geek2.funcao2())
print()
print(geek3.funcao3())
print()
print(geek4.funcao4())
print()
print(geek3.funcao3() + ' ' + geek4.funcao4())
print()

from geek.university.geek4 import funcao4

print(funcao4())
