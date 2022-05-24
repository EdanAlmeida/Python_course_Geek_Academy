"""
COMANDO WITH:

    - Passos para trabalhar com arquivos:
        - 1 -> abrir o arquivo;
        - 2 -> trabalhar com  o arquivo;
        - 3 -> fechar o arquivo;

    - O bloco 'with' é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados em seguida.

"""

#O bloco with: Forma Pythonica.

with open("texto.txt") as arquivo:
    print(arquivo.readlines())

print(arquivo.closed)
