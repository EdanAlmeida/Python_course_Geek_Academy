"""
RAISE:

    - lança exceções, ele não é uma função.
    - Uma paavra reservada.
    - Podemos criar nossa próprias exceções e mensagens de erro.
        - raise TipoDoErro("Mensagem de erro")

EX: raise ValueError("Valor incorreto!")

#Exemplo real:


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("Cor precisa ser uma string")
    else:
        print(f"O texto {texto} sera impresso na cor {cor}!")

colore("Edan Luis de Almeida", "Amarelo")

colore(1, 2)

"""

#Exemplo real refatorado:


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("Cor precisa ser uma string")
    if cor not in cores:
        raise ValueError(f"A cor precisa ser uma entre: {cores}")
    else:
        print(f"O texto {texto} sera impresso na cor {cor}!")

colore("Edan Almeida", "azul")
colore("Edan Almeida", "vermelho")


OBS = Após o raise a funçao finaliza. Assim como o return
