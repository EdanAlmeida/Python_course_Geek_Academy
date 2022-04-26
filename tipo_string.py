"""
TIPO STRING EM PYTHON

- Um dado é considerado string ['', ''' ''', " ", """ """];

- nome = 'Edan' == ['E', 'd', 'a', 'n'] -- isso que o python faz com as strings, na verdade
-                  [ 0 ,  1,   2,   3] == um vetor
- o espaço entre palavras conta como um caractere 

>>> nome = 'Edan Almeida'
>>> nome[::-1]
'adiemlA nadE'
>>> nome[0:15

"""

print('Edan Almeida')
print(type('Edan Almeida'))
# O mais comum é usar aspas simples

nome = ("Gina's Bar")
print(nome)
print(type(nome))

#Quebra de linha;
nome2 = 'Edan \nLuis de \nAlmeida'
print(nome2)

print()
nome3 = """O porquinho foi na escola
com a calça rasgadinha
e o bumbum de fora!"""
print(nome3)

# Caractere de escape
nome4 = "Edan \" Almeida"
print(nome4)


nome5 = 'edan luis de almeida'
print(nome5.upper())
print(nome5.lower())
print(nome5.title())

list = nome5.split()
print(nome5.split()) #converteu a string para 'lista' de strings;
print(list[1]) #luis - acessa o vetor normalmente pelo índice;
print(nome5[0:2])  #vai até o anterior [1] / slice de string

x = 'Luis Inácio Lula da Silva'
list2 = x.split()
print(list2[0])
print(list2[4])

print(list2[::-1]) #Pythonico
list2.reverse()
print(list2)

nome6 = 'Julia Roberts'
nome7 = nome6.replace('b', 'v')
print(nome7.replace('R', 'P'))

texto = 'socorram me subino onibus em marrocos'
print(texto)
print(texto[::-1])

texto2 = ' a m e o p o e m a'
print(texto2)
print(texto2[::-1])
