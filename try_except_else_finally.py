"""
TRY / EXCEPT / ELSE / FINALLY

     - Dica de quando e onde tratar código:
        - TODA entrada DEVE ser tratada.

OBS = A FUNÇÃO DO USUÁRIO É DESTRUIR O SEU PROGRAMA!

    ERRO:
    num = int(input("Informe um número: ")) [O desgraçado vai e digita  uma str]
    print(f"Voce digitou: {num}")


#Forma não muito adequada, mas trata o erro, de certa forma;
num = 0
try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor incorreto")

print(f"Voce digitou: {num}")


#Else (não muito comum!)
#É executado somente se não ocorrer o erro.

try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor incorreto")
else:
    print(f"Voce digitou: {num}")


#Finally:

try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor invalido")
else:
    print(f"Voce digitou o numero: {num}")
finally:
    print("Executando o Finally")

print("Depois do bloco try/except")

#O bloco finally é sempre executado. Independente se houve exceção ou não;
#É geralmente usado para fechar ou desalocar recursos;


#Exemplo ERRADO de tratamento


def dividir(a, b):
    return a / b


num1 = int(input("Informe o primeiro numero: "))

try:
    num2 = int(input("Informe o segundo numero: "))
except ValueError:
    print("O valor precisa ser numerico")

try:
    print(dividir(num1, num2))
except NameError:
    print("Valor incorreto")
"""

#Exemplo CORRETO == SEU CÓDIGO É SUA RESPONSABILIDADE:


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return ("Valor invalido! ")
    except ZeroDivisionError:
        return ("Divisao por '0' eh impossivel! ")


num1 = input("Informe o primeiro numero: ")
num2 = input("Informe o segundo numero: ")

print(dividir(num1, num2))
