"""
TESTE DE MEMÓRIA COM GENERATORS:

    - quando busca-se usar menos memória;

#Sequência de Fibonacci:
    - 1, 1, 2, 3, 5, 8, 13...[soma com o numero anterior]


#Função usando lista == 449MB - (100.000 cem mil)
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

#Lista
for n in fib_lista(100000):
    print(n)

"""

#Função usando geradores == 3MB - (100.000 cem mil)
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


for n in fib_gen(100):
    print(n)

#OBS = Geradores são muito mais eficientes em termos de uso de memória;
