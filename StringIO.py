"""
STRINGIO:

    - Para ler ou escrever dados em arquivos do sistema operacional, o software necessita de permissões;
        - permissão de leitura para ler;
        - permissão de escrita para escrever o arquivo;

StringIO -> utilizado para ler e utilizar arquivos em memória;

"""

#primeiro fazemos o import
from io import StringIO

mensagem = "Apenas uma string \n"

#Podemos criar um arquivo em memória já com um string inserida ou vazio para editar depois;

arquivo = StringIO(mensagem)

#Agora tendo o arquivo, podemos editá-lo;
print(arquivo.read())

#Escrever
arquivo.write("Outro texto")

#POdemos movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
