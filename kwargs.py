"""
**KWARGS:

 - definido pela comunidade;
 - parametro, mas diferente do *args que coloca os valores em uma tupla,
 - o **kwargs exige parametro nomeados e transforma esses parametros em um dicionário;

EX:
def cores_favoritas(**kwargs):
    print(kwargs)


cores_favoritas(Marcos='verde', Julia='amarelo', Fernanda='azul', Vanessa='branco')


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items(): #como é um dicionário é possível usar o items;
        print(f'A cor favorita de {pessoa.title()} eh {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# Os parametros *args e **kwargs não são obrigatórios.

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um cumprimento Pythonico, Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return "Nao tenho certeza quem voce eh."


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))



#Nas nossa funções, podemos ter NESTA ORDEM:
#Parametros obrigatórios, *args, parametros default (não obrigatórios) e **kwargs.
#Função com todos eles precisa seguir essa ordem.


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos.')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)


#Função ordem correta de parâmetros:
def motra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(motra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


a = 1
b = 2
args = (3, )
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}
"""

"""

#Ordem incorreta de parâmetros:
def motra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(motra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))



# Desempacotar com **kwargs:


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostra_nomes(**nomes))

"""

#Desempacotamento usando *args e **kwargs sem usá-los LOL;


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

list = [1, 2, 3]
tuple = (1, 2, 3)
set = {1, 2, 3}
dictionary = dict(a=1, b=2, c=3)

soma_multiplos_numeros(*list)
soma_multiplos_numeros(*tuple)
soma_multiplos_numeros(*set)
soma_multiplos_numeros(**dictionary)

#OBS = os nomes da chave em um dicionário devem ser os mesmo dos parametros da função;
