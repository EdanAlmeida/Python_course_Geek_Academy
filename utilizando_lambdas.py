"""
FUNÇÕES LAMBDAS:

 - funções sem nome == anônimas;

#Função em Python:
    def soma(a, b):
        return a + b


def funcao(x):
    return 3 * x + 1


print(funcao(4))

#Expessão lambda:


lambda x: 3 * x + 1


#Para utilizar essa expessão é preciso dar um nome;
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))
# Forma não muito utilizável;


#Podemos ter expressõe lambdas com multiplas entradas;


nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('edan', '  ALMEIDA'))
print(nome_completo('  Helena', '  machado '))

#Strip == remove espaços no inicio e no fim da variável; Somente espaço de início e fim, não entre palavras;


#Exemplo:
python = lambda: 'Como nao amar o Python?'

print(python())

# Número de argumentos e parametros precisam ser iguais, a não ser com *arg e *kwargs;


#Exemplo 2: Forma que comumente se usa uma expressão 'lambda';


autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

"""

#Função Quadratica = f(x) = a * x ** 2 + b * x + c
#Definindo a função:


def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x **2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste =  geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(2, 3, -5)(0))
print(geradora_funcao_quadratica(2, 3, -5)(1))
print(geradora_funcao_quadratica(2, 3, -5)(2))

# As lambdas são usadas para filtragem de ordenação de dados;
