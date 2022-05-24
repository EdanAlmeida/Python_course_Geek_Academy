"""
SISTEMA DE ARQUIVOS DE - NAVEGAÇÃO:

    - como os arquivos são estruturados dentro de diretórios;
        - doc, vídeo, texto, planilha;
        - nome e extensão;
    - Os computadores reconhecem os arquivos pelos metadados inseridos neles;
    - Os diretorios são organizados de forma hierárquica;
    - Árvore hierárquica;
    - Diretório raiz -> root directory

    Windows ( C:\ ) <> Posix ( / ) [mac OS and Linux]

    - cd -> change directory; (cd /)
    - ls -> list

    - Path -> caminho completo do arquivo até o diretório;
        - Paths:
            Absolute -> da raiz até o arquivo.
            Relative -> da raiz até o diretório.
    .. -> move um diretório antes;

    - cp -> copia

- Para fazer uso de manipulação de arquivos do sistema operacional, precisamos do módulo 'os'.
    - os -> Operating System.



#Fazer o import

import os

# getcwd -> current word directory - retorna o caminho absoluto

print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())

os.chdir('..')
print(os.getcwd())



#Absoluto ou Relativo?
print(os.path.isabs('/home/edan/')) #True
print(os.path.isabs('home/edan/')) #False

\ - unicodescape;
import os
# Windows == cuidado ao verificar diretórios
print(os.path.isabs('C:\\Users\\Edan')) #BURROS, como diz o Seu Madruga


#saber o tipo de sistema
print(os.name)
print(os.uname())

#Juntar diretórios
os.path.join() -> recebe dois parametros, pirmeiro == diretório atual; segundo == o que será juntado

#Listar diretórios
print(os.listdir()) #Pode passar um path (len() também)
print(os.scandir()) #Mais detalhado(iterator), precisa converter [DirEntry]
os.scandir().close()
OBS = Ao usar a scandir, é preciso fechá-lo;

    - cada arquivo da árvore de diretórios recebe uma identificação (nº) == inode

"""

import os

print(os.getcwd())

