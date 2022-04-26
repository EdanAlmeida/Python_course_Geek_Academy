"""
ENTENDENDO E EXPLORANDO RANGES EM PYTHON

- Precisamos conhecer o loop for para usar os ranges;
- Precisamos conhecer os ranges para trabalhar melhor com o for;
- sequências numéricas de forma especificada;

Formas gerais:
    Forma1:
    - range(valor_de_parada)
OBS = valor de parada não inclusive (início padrão 0, e passo de 1 em 1);
#Forma1: (começa em 0 e vai até o valor_final [11 -1])
for num in range(11):
    print(num)

    Forma2:
    - range(valor_de_inicio, valor_de_parada)
OBS = valor de parada não inclusive (início especificado, e passo de 1 em 1);
#Forma2: (começa no valor especificado e vai até o valor final não inclusive)
for num in range(3, 11):
    print(num)

    Forma3:
    - range(valor_de_inicio, valor_de_parada, passo)
OBS = valor de parada não inclusive (início padrão 0, passo especificado);
#Forma3: (valor de passo especificado)
for num in range(0, 51, 5):
    print(num)


    Forma4: (igual a três, mas inversa)
    - range(valor_inicio, valor_de_parada, passo)
OBS = valor de parada não inclusive (valor_inicio especificado, passo especificado [-]);
"""

for num in range(10, 0, -1):
    print(num)
#Isso é feito em listas para imprimi-la inversamente;

#Não é possível ver o range direto no console do terminal, precisa atribui-lo a uma lista:
lista = list(range(10))
print(lista)
