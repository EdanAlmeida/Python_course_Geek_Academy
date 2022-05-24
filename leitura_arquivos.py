"""
LEITURA DE ARQUIVOS:

    - para ler o conteúdo de um arquivo em Python, usamos a função integrada 'open()';
    - open() -> passa um parametro de entrada que é o nome do arquivo a ser lido.
        - essa função retorna um _io.TextIOWrapper e é com esse retorno que trabalhamos;

        - https://docs.python.org/3/library/functions.html#open

    OBS = por padrão, a função open() abre o arquivo para leitura; (FileNotFoundError)

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'> == mode 'r' = read()
UTF8 = tipo de codificação de caracteres (UTF8 == 98% dos programas)

"""

#Exemplo:

arquivo = open('texto.txt')

print(arquivo)
print(type(arquivo))

#Para ler o conteúdo do arquivo, após sua abertura devemos usar a função 'read()';

print(arquivo.read())

#O python utiliza um recurso para arquivos (cursor);
#Esse cursor funciona como um cursor quando escrevemos

#Todo o conteúdo é convertido em uma string;
