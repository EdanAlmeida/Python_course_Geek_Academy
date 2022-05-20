"""
INSTALANDO E UTILIZANDO MODULOS EXTERNOS:

    - para instalar um pactore externo, usamos um gerenciador chamado Pip (Python Installer Package)
    - Pacotes disponíveis:
        - https://pypi.org

colorama -> é utilizado para permitir impressão de textos coloridos no terminal;
# O python package serve para tornar a linguagem mais poderosa;


from colorama import init
init()

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

print('\033[31m' + 'some red text')
print('\033[39m') # and reset to default color

"""

#Geração de PDF em Python:
import pydf
pdf = pydf.generate_pdf('<h1>Edan Almeida</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
