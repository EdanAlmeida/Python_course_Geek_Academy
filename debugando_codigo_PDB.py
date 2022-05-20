"""
DEBUGANDO O CÓDICO COM PDB: Python Debugger

    - Bug = inseto;
    - Debug = tirar o bug;


#Prática RUIM
def dividir(a, b):
    print(a, b)
    try:
        return int(a) / int(b)
    except ValueError:
        return ("Valor invalido! ")
    except ZeroDivisionError:
        return ("Divisao por '0' eh impossivel! ")

print(dividir(4, 7))

#Debug manual:
    import pdb; pdb.set_trace()

    COmandos Python Debug:
        - l (listar onde estamos no código)
        - n (próxima linha)
        - p (imprime variável)
        - c (continua a execução - finaliza o debugging)
        OBS = cuidar com os nomes das variáveis;

"""

#Existe formas mais profissionais de se fazer o 'debug':
#Python == podemos usar o pycharm ou o PDB:

#Exemplo Pycharm: (FORMA RECOMENDADA!)


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return ("Valor invalido! ")
    except ZeroDivisionError:
        return ("Divisao por '0' eh impossivel! ")

print(dividir(4, 0))

#Sempre usar nomes representativos nas variáveis.
