"""
RECEBENDO DADOS DE USUÁRIO - PYTHON

- builtins = recursos integrados da linguagem (input, por exemplo);
- Todo dado recebido via 'input' é reconhecido como string;

- Em python, string é tudo que estiver entre:
    - aspas simples; 'Angelina Jolie'
    - aspas duplas; "Algelina Jolie"
    - aspas simples triplas; '''Angelina Jolie'''
    - aspas duplas triplas;

"""

nome = input("Qual seu nome? ") #Entrada e processamento já lendo os dados e atribuindo à variável.
print(f'Bem vindo(a), {nome}! ') # o f'' substitui o 'format' da versão 2.x;

idade = int(input("Qual sua idade? "))
print(f'Legal {nome}. Entao vc tem {idade} anos de idade. ')

# Essa formatação está disponível a partir do Python 3.7;

print(f'O {nome} nasceu em {2022 - int(idade)}') # cast

# Cast == conversão de um tipo de dado para outro;
#{} dentro da chave é possível fazer processamento de dados;

x = int(input('Digite um numero: ')) #cast dentro do input.
