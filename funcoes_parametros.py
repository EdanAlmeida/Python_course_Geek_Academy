"""
Funções com parâmetro (de entrada):

- dados a serem processados dentro da mesma;
- geralmente temos entrada > processamento > saida;
- temos funções que não possuem entrada, saída, entrada sem saída, não possuem entrada, mas possuem saída, entrada e
saída;


# Refatorando uma função:


def quadrado(numero):
    return numero * numero


print(quadrado(5))
print(quadrado(7))



def cantar_parabens(aniversariante):
    print('Parabens pra voce')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}!')

cantar_parabens('Edan')

OBS = Funções podem ter 'n' parâmetros de entrada. Quantos parâmetros forem necessários;



def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


print(soma(2, 4))

OBS = número errado de parâmetro == TypeError


#Nomeando parâmetros:


#def nome_completo(string1, strin2): #<> Usar nome e sobrenome e não string1 e string2
def nome_completo(nome, sobrenome):
    return f'Seu nome completo eh {nome} {sobrenome}'


print(nome_completo("Angelina", "Jolie"))


#A diferença entre parametros e argumentos: parametros da definição da função [variáveis na decl. da função];
# Dados passados durante a execução de um programa.

# A ordem dos parâmetros é muito importante por conta da atribuição;

# Argumentos nomeados (keyword Arguments):
#Caso utilizemos os nomes dos parametros no argumento, podemos utilizar qualquer ordem.

print(nome_completo(sobrenome='Dicks', nome='Picarossauro'))

"""

#Erro comum na utilização do return:


def soma_impares(numeros):
    total = 0
    for i in numeros:
        if i % 2 != 0:
            total = total + i
    return total                     #cuidar da identação senão termina no primeiro for;


if __name__=="__main__":
    lista = [1, 2, 3, 4, 5, 6, 7]
    tupla = 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(soma_impares(lista))
    print(soma_impares(tupla))
