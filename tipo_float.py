"""
TIPO FLOAT EM PYTHON (real/decimal)

- usar ponto e não vírgula

"""

x = float(input('Digite um numero: '))
print(f'{x:.4f}')

valor = 1, 44 # isso é lido como uma tupla pelo Python e não como float
print(valor)
print(type(valor))

# É possivel - dupla atribuição
valor1, valor2 = 1, 44
#cada variável recebe um valor (1) (44)
print(valor1)
print(valor2)

#Podemos fazer cast de float para outros tipos
n = 1.44
res = int(n)
print(res)
#No entanto, ao fazer isso perdemos precisão e parte do dado;

# Podemos trabalhar com números complexos?
complex = 5j
print(type(complex))   #número complexo
i = complex ** 2
print(i)

# Tomar cuidado com a conversão de dados para não perder informação.
