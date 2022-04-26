"""
TIPO NUMERICO EM PYTHON

- Em Java, o maior numero inteiro possível é 2**63 (1 byte fica responsável pelo sinal do número);
- Em python o máximo fica restrito a memória disponível no computador, ou seja, números maiores (2**1000);

- terminal = num += / -= / *=
- type(num)

"""

x = 5 + 4
y = 9 // 5
z = int(9/2)  #Não é lá muito pythonico - cast
a = 4 % 2
b = 5 % 2
c = 3 ** 3

print(x)
print(y)
print(z)

# Even or odd
print(a)
print(b)

print(c)

num = 1_000_000 #facilita a leitura humana.
print(num)

num2 = 41
print(num2 + 1)

print(type(num))
