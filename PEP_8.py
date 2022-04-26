"""
PEP 8 - BOAS PRÁTICAS - Python Enhancement Proposals

- console python funciona como o console do sistema;
- import this == poem (easter egg) "The Zen of Python"
- Documentation == https://peps.python.org/

- nano test.py == programar pelo terminal ubuntu;
- python3 test.py == to run the program;
- Embora seja possível programar direto pelo terminal, o ideal é usar a ide para ter mais auxílio.
- A PEP8 serve para a gente escrever códgos mais organizados (Pythonicos)

    [1] - camelCase para determinar nome de classes;
        ex:
            class Calculadora:
                pass

            class CalculadoraCientifica:
                pass


    [2] - é possível desativar a correção de spelling;


    [3] - lowercase para funções e variáveis;
        ex:
            def soma():
                pass

            def soma_dois():
                pass

            num = 4
            num_impar = 5


    [4] - Utilize 4 espaços para identação; (NÃO USAR TAB POR CONTA DA CONFIG.)
        ex:
            if 'a' in 'banana':
                print('TEM')


    [5] - Linhas em branco == tomar cuidado com as linhas em branco (PEP8)
        - separar funções e definições com duas linhas em branco;
        - Métodos dentro de uma classe devem ser separados com uma única linha em branco;


    [6] - imports devem ser sempre feitos em linhas separadas;
        #Import Errado:
            import sys, os

        #Import certo:
            import sys           #Pacotes completos
            import os

        #Não há problemas em utilizar:
            from types import StringType, ListType          #Classes dentro do pacote + leves

        #Casos muitos imports dentro de um pacote forma correta:
            from types import (
                StringType,
                ListType,
                SetType,
                OutroType,
            )

        #Imports devem estar no inicio do arquivo, logo depois dos comentários e docstrings.
        # Antes de constantes ou variáveis globais.


    [7] - Espaços em expressões e instruções: #Evitar espaços desnecessários.
        - não fazer:
            funcao( algo [ 1 ], { outro: 2 } )
        - faça:
            funcao(algo[1], {outro: 2})


    [8] - Termine sempre uma instrução com uma nova linha;

"""
