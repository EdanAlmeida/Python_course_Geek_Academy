"""
GENERATORS:

    - são iterators;
OBS = Nem todo iterator é um generator;

    - Generator podem ser criados com funções geradoras;
    - Funções geradoras utilizam a palavra reservada 'yield';
    - Generators podem ser criados com Expressões Geradoras;

    #Diferenças entre funções e generator functions:
    ________________________________________________________________________________________________________________
    | Funções                                          | Generator Functions                                       |
    ________________________________________________________________________________________________________________
    | utilizam return                                  | utilizam yield                                            |
    ________________________________________________________________________________________________________________
    | retorna uma vez                                 | yield multiplas vezes                                      |
    ________________________________________________________________________________________________________________
    | quando executada retorna um valor               | quando executada retorna um generator                      |
    ________________________________________________________________________________________________________________

#Exemplo de generator function:


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


#GEnerator Function <> GEnerator (ela gera um generator):
gen = conta_ate(5)
#print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#print(next(gen))


gen = conta_ate(10)

for i in gen:
    print(i)

"""


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


gen = list(conta_ate(10))
print(gen)
