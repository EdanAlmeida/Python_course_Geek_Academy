"""
TESTE DE VELOCIDADE COM EXPRESSÕES GERADORAS:

#GEnerators:
def nums():
    for num in range(1, 10):
        yield num

ge1 = nums()
print(ge1) #generator


#Generator Expression
ge2 = (num for num in range(1, 10))

print(ge2)

"""

#Realizandoo teste de velocidade:
import time

#GEnerator Expression: (100 milhões)
gen_inicio = time.time()
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio


#List comprehension: (100 milhões)
list_inicio = time.time()
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou = {gen_tempo} segundos')
print(f'List Comprehension levou = {list_tempo} segundos')

#Pycache == memória interna para otimizar o uso da IDE;

#Além de ser melhor em termos de memória, o generator expression também é melhor em questão de velocidade de process.
