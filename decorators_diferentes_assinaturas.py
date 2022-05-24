"""
DECORATORS COM DIFERENTES ASSINATURAS:

    - Assinatura -> é representada pelo seu retorno, nome, e parâmetros de entrada.
    - Podemos usar parametros nomeados;
        - acompanhamento='Batata Frita', principal='Picanha'


#Relembrando:
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f"Ola, eu sou o/a {nome}"


@gritar
def ordenar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor!'


#Testando:

print(saudacao('Angelina'))

#Para resolver, usamos um padrão de projeto (decorator pattern)
print(ordenar('Lasanha', 'Ceasar Salad'))



#Refatorando

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f"Ola, eu sou o/a {nome}"


@gritar
def ordenar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor!'


#Teste:

print(saudacao('Angelina'))
print(ordenar('Lasanha', 'Ceasar Salad'))

"""

#Decorator com parâmetro de entrada:

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto. Primeiro argumento precisa ser {valor}. '
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


#Teste
print(soma_dez(10, 12))
print(soma_dez(12, 12))
print()

print(comida_favorita('pizza', 'camarao', 'lasanha'))
print(comida_favorita('maionese', 'camarao', 'lasanha'))

