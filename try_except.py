"""
BLOCO TRY/ EXCEPT:

    - Tratar erros que podem ocorrer no nosso código, evitando que o programa pare de funcionar.
    - CRACKERS = prejudicam outros;

    #FOrma mais simples:
        try:
            //execução problemática
        except:
            //o que deve ser feito em caso de problemas


#Exemplo

try:
    geek()
except:
    print("Deu algum problema! ")

#Há um erro, mas o programa continua a execução.


try:
    len()
except:
    print("Deu algum problema! ")

OBS = tratar um erro de forma genérica, não é o melhor jeito. O melhor é tratar de forma específica.


#Tratando erro específico:
try:
    geek()
except NameError:
    print("Voce esta utilizando uma funcao inexistente!")


#Não trata o erro, pois a exceção foi definida para NameError e aqui temos um TypeError;
try:
    len(5)
except NameError: #Se mudar para TypeError, ele será tratado.
    print("Voce esta utilizando uma funcao inexistente!")


try:
    len(5)
except TypeError as err: #GEralmente esse tipo de info não é passada ao usuário, mas sim registrada no log.
    print(f"A aplicação gerou o seguinte erro: {err}")

#LOG = banco de dados ou memória.


#Podemos efetuar diversos tratamentos de erro de uma vez:
try:
    len(5)
except NameError as erra:
    print(f"Deu NameError: {erra}")
except TypeError as errb:
    print(f"Deu TypeError: {errb}")

try:
    geek()
except NameError as erra:
    print(f"Deu NameError: {erra}")
except TypeError as errb:
    print(f"Deu TypeError: {errb}")

try:
    print("Edan"[9])
except NameError as erra:
    print(f"Deu NameError: {erra}")
except TypeError as errb:
    print(f"Deu TypeError: {errb}")
except:
    print("DEu um erro diferente") #IndexError

"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None

dic = {"nome": "Edan"}
print(pega_valor(dic, "nome"))
print(pega_valor(dic, "game")) #exception



