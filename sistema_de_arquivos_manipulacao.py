"""
SISTEMA DE ARQUIVOS - MANIPUALAÇÃO:

import os

#Descobrindo se um arquivo ou diretório existe
print(os.path.exists('Frutas.txt')) #True
print(os.path.exists('arquivo.txt')) #False
print(os.path.exists('geek'))
print(os.path.exists('geek/university'))

#Paths absolutos
print(os.path.exists('/home/edan/Pictures'))
print(os.path.exists('/home/edan/Pictures/83978.jpg'))

#FORMAS NÃO PYTHONICAS
#Criando arquivo forma 1:
open('arquivo-teste.txt', 'w').close()

#Criando arquivo forma 2:
open('arquivo-teste.txt', 'a').close()


#forma 3:
with open('arquivo-teste.txt', 'a') as arquivo:
    pass



# Forma mais adequada;
os.mknod('arquivo-test.txt')
os.mknod('/home/edan/arquivo-test.txt')

#MAC OS (mknod == PermissionError) [precisa de poderes adm]
#Se o arquivo já existir, vai dar erro de FileExistsError

#Criando diretórios - um de cada vez
os.mkdir(('templates')) #path relativo
os.mkdir(('/home/edan/templates')) #path absoluto
#Se o diretorio já existir, vai dar erro de FileExistsError
#Se não tive permissão para criar == PermissionError


#Criar mais de um diretório de cada vez - árvore de diretórios
os.makedirs('templates/edan/university')
#Se já existir, teremos erro novamente;
#Se algum já existir, ele será ignorado
os.makedirs('templates2/novo2/outro/2', exist_ok=True) #se eles já existirem, ele ignora e não dá erro;


#Renomear diretórios
os.rename('templates2', 'geek2') #só renomeia o principal, se existir subtemplate, segue igual;
#caso não exista, teremos um FileNotFoundError;
#Se o diretório não estive vazio, teremos um OSError;


#Renomear arquivos:
os.rename('geek2/novo2/outro2/teste.txt', 'eek2/novo2/outro2/geek.txt')
#PRecisa determinar todo o caminho;



#Deletar arquivos - Tomar cuidado com os comandos; É  permanente.
os.remove('geek.txt')
#Se estiver no windows e o arquivo estiver em uso, terá um erro.
# Se informar um diretório == IsADirectoryError.


#Removendo Diretórios:
os.rmdir('templates')
#DirectoryNotEmpty == comando para diretório vazio;
#Se não existir == FIleNotFoundError


#Removendo árvore de diretórios:
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)
    if not arquivo.is_file():
        os.rmdir(arquivo.path)


#Removendo árvore de diretórios vazios:
os.removedirs('geek2/outro/mais')
#Se algum dos diretórios conter arquivos ou outros diretórios, o processo para.


#Mandar arquivos para a lixeira - precisei baixar essa biblioteca;
from send2trash import send2trash
send2trash('cesta2.txt')
#Caso o arquivo não exista, teremos o OSError;
#Aplicável para diretórios;


import os
#Trabalhando com arquivos e diretórios temporários;
import tempfile
with tempfile.TemporaryDirectory() as tmp:
    print('Criei um diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()
#Não funciona no windows;

https://docs.python.org/3/library/os.html?highlight=os#module-os
    OS - operating System Interfaces.

"""

import os
import tempfile

#Arquivo temporário
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n') #b de binário (bits) somente bits.
    tmp.seek(0)
    print(tmp.read())

