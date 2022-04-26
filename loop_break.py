"""
SAINDO DE LOOP COM BREAK EM PYTHON

- Utilizamos o break para sair de loops de maneira projetada;

for num in range(1, 11):
    if num == 6:
        break
    else:
        print(num)
print('Sai do loop! ')

"""

while True:
    comando = input('Digite "sair" para sair: ')
    if comando == 'sair':
        break
