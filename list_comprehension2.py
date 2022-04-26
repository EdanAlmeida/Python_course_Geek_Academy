"""
LIST COMPREHENSION - 2:

 - Adicionar estrutura condicionais lógicas às listas comprehension;

"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = [i for i in numeros if i % 2 == 0]
impares = [i for i in numeros if i % 2 != 0]

print(pares)
print(impares)

print([i for i in numeros if i % 2 == 0])
print([i for i in numeros if i % 2 != 0])

#Refatorando:
pares = [i for i in numeros if not i % 2] #Not False == True
impares = [i for i in numeros if i % 2]

print(pares)
print(impares)


res = [i * 2 if i % 2 == 0 else i / 2 for i in numeros]
print(res)
