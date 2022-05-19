"""
LEN / ABS / SUM / ROUND

#Len
    - len() = retorna o tamanho (nº de elementos de um iterável).
#Len
print(len("Ordem e Progresso"))
print(len([1, 2, 3, 4, 5]))
print(len({1, 2, 3, 4, 5}))
print(len({'a': 1, 'b': 2}))
print(len(range(0, 10)))

#Por baixo dos panos:

#Dunder len
print("Ordem e Progresso".__len__())


#Abs
    - abs() = retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o
    sinal.


#Abs
print(abs(.5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

print(abs("Edan Almeida"))# string = erro


#Sum
    - sum() = recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma dos elementos,
    incluindo o valor inicial.
    OBS = O valor inicial default == 0;


# Sum (2 arguments)
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))
print(sum([1, 2, 3, 4, 5], -5))

#print(sum([3.14, 2.45])) # não fununcia, hhehehe!
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 6}))


#Round (arredonda)
    - round() = retorna um numero arredondado para n digito de precisão após a casa decimal. Se a precisão não
    informada retorna o inteiro mais próximo da entrada.

"""

print(round(10.2))
print(round(1.213))
print(round(10.2213, 2))
print(round(10.9999, 2))
