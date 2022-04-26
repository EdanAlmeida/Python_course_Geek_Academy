"""
ESTRUTURAS LÓGICAS EM ṔYTHON [and, or, not, is]

- Operadores unários = not
- Operadores binários = and / or / is

>>> nome = 'edan'
>>> nome.isTitle()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'isTitle'
>>> nome.istitle()
False
>>> nome.islower()
True
>>>

"""

ativo = False
logado = True

if ativo or logado:
    print('Usuário ativo no sistema! ')
else:
    print('Você precisa ativar sua conta! Por favor, cheque seu e-mail. ')

print()
if ativo and logado:
    print('Usuário ativo no sistema! ')
else:
    print('Você precisa ativar sua conta! Por favor, cheque seu e-mail. ')

print()                         #Maneira Pythonica
if not ativo:
    print('Ative sua conta')
else:
    print('Bem vindo!')

print()
if ativo is True:
    print('Ative sua conta')
else:
    print('Bem vindo!')

print()                           #Mais limpo do que usar o 'not'
if ativo:
    print('Tamo aí loco véio!')
else:
    print('Sai fora!')

nome = 'Edan'
print(nome.istitle())
