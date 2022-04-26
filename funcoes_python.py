"""
FUNÇÕES == dividir uma tarefa complexa em várias tarefas simples;

1 - DEFININDO FUNÇÕES:
    - Parte de extrema importância na programação;
    - Pequenos trechos de código que realizam tarefas específicas;
    EX de funções:
        - print()
        - min()
        - max()
        - len()
        - count()
    - Pode ou não receber entrada de dados e retornar uma saída de dados;
    - Uteis para executar procedimentos similares que são repetidos várias vezes;
    - Se voce escrever uma função que realiza várias tarefas, é preciso reavaliar;
    - A função precisa ser simples e objetiva;


# EX:
cores = ['verde', 'amarelo', 'azul', 'branco']

#Função integrada: (built-in) [print()];
print(cores)
cores.append('roxo') #o append é uma função que está dentro da lista;
print(cores)

#Diferente do print, o append não aceita todos os tipos de dados;
# Ambas recebem dados de entrada;

cores.clear()
#A função clear não recebe dados de entrada.

print(help(print))

#DRY = Don't repeat yourself;

"""

#Como definir funções?
"""
Em geral, a forma de definir uma função é:

    -def nome_da_funcao(parametro_entrada):
        bloco_da_funcao

Onde: 
    - nome da função sempre em letras minúsculas e se nome composto, separa por _ (snake_case);
    - parametros de entrada são opcionais, quando mais de um, a sepação se dá por vírgula (,);
    - O bloco da funcao também é chamado de 'corpo da funcao' ou 'implementacao';
    - pode haver ou não retorno da funcao;
    
OBS: para definir uma funcao usamos a palavra reservada (def). Também abrimos o bloco de códigos com (:).


#Definindo a primeira função:
def diz_oi():
    print('Oi!')

#Dentro das funções, podemos utilizar outras funções;
#A função só executa uma tarefa (dizer oi);
#Essa função não recebe nenhum parametro de entrada;
#Essa função não retorna nada;

#Chamada de execução;
diz_oi()

#Forma2:
if __name__=="__main__":
    diz_oi()
    
"""

def cantar_parabens():
    print('Parabens pra voce')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')

cantar_parabens()
for i in range(5):
    cantar_parabens()

"""
#Em python, podemos inclusive criar variáveis do tipo de uma função e executar a função por meio da variável:

canta = cantar_parabens
canta()
#Não é muito comum, mas numa dessa pode ser útil;
"""


