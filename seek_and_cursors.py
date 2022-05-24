"""
SEEK AND CURSORS:

    - seek() -> usada para movimentar o cursor em um arquivo;

arquivo = open("texto.txt")
print(arquivo.read())

#Movimentando o cursor pelo arquivo: seek()

arquivo.seek(0) #como se fosse indexado no indice '0' e aí começa de novo;
print(arquivo.read())


#Leitura linha a linha = readline();

arquivo = open("texto.txt")
arquivo.seek(150)
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

ret = arquivo.readline(100)
print(ret)
print(ret.split(' '))


# readlines() -> bom para saber a quantidade de linhas;
arquivo = open("texto.txt")

linhas = (arquivo.readlines())
print(len(linhas))

print(arquivo.readlines())
"""

#OBS = QUando abrimos um arquivo com a função 'open()', é criada uma conexão entre o arquivo no disco do computador e
# o programa, essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo, devemos fechar essa conexão.
#Para isso, usamos a função 'close()'

#Passo 1 = Abrir o arquivo;
arquivo = (open("texto.txt"))
#Passo 2 = Trabalhar com o arquivo;
print(arquivo.read()) #Sedeterminar um numero dentro do () do read, ele lê o número de chars.

#Passo 3 = Fechar o arquivo;
arquivo.close()

print(arquivo.closed) #VErifica se o arquivo tá fechado
