"""
ESTRUTURAS CONDICIONAIS E LÓGICAS EM PYTHON (if, else, elif)

- C =
    - if (idade >= 18){
        printf("Menor de idade!")
    }

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Acesso permitido! Bem vindo, meu chapa! ')
else:
    print('Acesso negado! Caia fora daqui, Zé ruela!')

"""

idade = int(input('Digite sua idade, jovem padawan: '))

while idade < 0:
    print('Você é retardado? ')
    idade = int(input('Digite sua idade corretamente, otário: '))

if (idade > 0) and (idade < 12):
    print('Sai fora, bebezinho!')
elif (idade >= 12) and (idade < 18):\
    print('Adolescentes são um porre!')
elif (idade >= 18) and (idade < 60):\
    print('Bem vindo, camarada! ')
else:
    print('Lugar de velho é no asilo! ')
