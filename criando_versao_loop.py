"""
CRIANDO LOOPS:

    - criando sua própria versão de loop;


for num in [1, 2, 3, 4, 5]:
    print(num)

#Por baixo dos panos:
iter([1, 2, 3, 4, 5])

"""

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('Edan Almeida')
lista = [1, 2, 3, 4, 5.5, 6.7]

meu_for(lista)
