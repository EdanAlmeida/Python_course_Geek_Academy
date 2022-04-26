"""
FUNÇÕES PARÂMETRO PADRÃO (Default Parameters):

- Funções em que a passagem de parâmetro seja opcional;
    print('Edan Almeida') #com parâmetro opcional
    print()

#Passagem de parametro obrigatoria:
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) #falta o parâmetro (Type Error)



def exponencial(numero=4, potencia=2): # ao colocar um valor esse parâmetro se torna opcional;
    return numero ** potencia

print(exponencial(2, 3)) #2 ** 2 ** 2

print(exponencial(3)) # Por padrão eleve ao quadrado
print(exponencial(3, 5)) #eleva a potencia informada
print(exponencial())
# Em funções Python, os parâmetros com valores default devem sempre estar no final da declaração;


# Outros exemplos:
def soma(num1=1, num2=3):
    return num1 + num2

print(soma(4, 3))
print(soma())


def mostra_informacao(nome='Edan', instrutor=False):
    if nome == 'Edan' and instrutor:
        return "Bem vindo instrutor, Edan!"
    elif nome == 'Edan':
        return "Eu pensei que voce era o instrutor."
    return f'Ola {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))

# Por que usar parâmetros com valor default?
# Flexibilidade, evitar erros, exemplos mais legiveis de código;
# Podemos usar quaisquer tipos de dados (funões, numeros inteiros, etc.);

def diz_oi():
    print('Oi!')

variável = diz_oi()
variável


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - evitar problema e confusões:
#Variaveis globais;
#Variáveis locais;

instrutor = 'Edan' #Global

def diz_oi(): #Usa a variável local;
    instrutor = 'Python'
    return f'Oi {instrutor}'


print(diz_oi())

# sempre que possível, evitar variável global;


total = 0

def incrementa():
    global total #Chama a variável global

    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())

"""

# Podemos ter funções que são delcaradas dentro de funções e também uma forma de especial de escopo de variável;


def fora():
    contador = 0

    def dentro():
        nonlocal contador #não global e nem local, ela é não local localizada na função anterior;
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora()) # Toda vez inicializa o contador;
