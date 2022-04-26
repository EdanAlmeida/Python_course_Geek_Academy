"""
LOOP WHILE EM PYTHON

- iterar sobre sequências;
    while 'expressão booleana':
        //execução do loop

- O bloco do while será repetido enquanto a expressão booleana for verdadeira;

EX 1:
num = 1
while num <= 10:
    print(num)
    num = num + 1

# Em um loop whule é importante o critério de parada senaõ ele roda infinitamente (loop infinito);

"""

#EX 2:

resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou, Jéssica? ')
#Em alguns casos é necessário que o loop seja infinito (jogos, por exemplo);
# Captura de tela e att. de tela é feito em loop infinito;
# Arduino também usa loop infinito, principalmente com sensores;
