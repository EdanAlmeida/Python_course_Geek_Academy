"""
FORÇANDO TIPOS DE DADOS COM DECORATOR:

    - Em Python não determinamos o tipo de dado.

#Java ==
    - int numero = 10;
    - String nome = "Edan";

"""

def forca_tipo(*tipos): #*args
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor)) #casting para string.
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)
def repete_mensagem(msg, vezes):
    for vez in range(vezes):
        print(msg)


@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)


repete_mensagem('Edan', 3)
dividir('1', 5)
