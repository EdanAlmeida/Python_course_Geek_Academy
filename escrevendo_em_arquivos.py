"""
ESCREVENDO EM ARQUIVOS:

    - Ao abrir o arquivo para leitura, não podemos escrever e vice-versa;
    - Os agumentos da função write() tem que ser string.

"""

#Exemplo de escrita: modo 'w' (write)

with open("texto.txt", "w") as arquivo:
    arquivo.write("God of war! \n" * 3)
    arquivo.write("Prince of Persia! \n" * 3)
    arquivo.write("Diabo loiro war! \n" * 3)
    arquivo.write("Marco Loco Evil! \n" * 3)
    arquivo.write("Shadows of the Troço Gordo! \n" * 3)


with open("Frutas.txt", "w") as file:
    while True:
        fruta = input("Informe uma fruta ou digite 'sair': ")
        if fruta != 'sair':
            file.write(f'{fruta} \n')
        else:
            break
