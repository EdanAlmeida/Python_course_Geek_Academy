"""
ESCOPO DE VARIÁVEIS EM PYTHON

- /                        /     (escopo começa na primeira barra e termina na segunda)
- Dois casos de escopo de variáveis;
    - variáveis globais = seu escopo compreende todo o programa.
    - variáveis locais = apenas no bloco em que foram declaradas.
        - nome_variavel = valor_variavel

- Python == linguagem de tipagem dinâmica == não coloca-se o tipo de dado, a ide infere pelo valor atribuido.
    - C = int num = 42;
    - Java = int num = 42;

"""

#Variável global:
num = 42
print(num)
print(type(num))
print()
name = 'Edan'
print(name)
print(type(name))
# EM outras linguagens não é possível fazer reatribuição;

#Variavel local
if num > 10:
    novo = num + 10
    print(novo)

print(num)
