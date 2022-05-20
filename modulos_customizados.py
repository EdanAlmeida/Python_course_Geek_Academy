"""
MODULOS CUSTOMIZADOS:

    - Módulos Python são arquivos Python;
    - Os arquivos que eu tomo nostas são módulos;

"""

from funcoes_parametros import soma_impares

lista = [1, 2, 3, 4, 5, 6, 7]
tupla = 1, 2, 3, 4, 5, 6, 7, 8, 9

print(soma_impares(lista))
print(soma_impares(tupla))

#Posso importar todo o módulo ou apenas uma função;
#Não deve haver prints no pacote Python;
