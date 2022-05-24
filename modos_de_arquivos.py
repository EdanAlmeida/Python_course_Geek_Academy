"""
MODOS DE ABERTURA ARQUIVOS:

    - r -> abre para leitura;
    - w -> abre para escrita - sobreescreve caso o arquivo já exista;
    - x -> abre para escrita somente se o arquivo não existir;
        - caso o arquivo já exista há um erro (FileExistsError);
            with open("University.txt", 'x') as arquivo:
                arquivo.write("Texte de conteúdo. \n")
    - a -> abre para escrita e adiciona ao final da escrita;
        - se o arquivo não existir, será criado, do contrário adicionado ao FINAL do arquivo;
    - + -> reading and writing (att).

"""

with open("Frutas.txt", "a") as file:
    while True:
        fruta = input("Informe uma fruta ou 'sair': ")
        if fruta != 'sair':
            file.write(f'{fruta} \n')
        else:
            break


"""with open("Frutas.txt", "a+") as file2:
    file2.seek(0)
    while True:
        fruta = input("Informe uma fruta ou 'sair': ")
        if fruta != 'sair':
            file2.write(f'{fruta} \n')
        else:
            break"""


"""with open("Frutas.txt", "w+") as file2:
    file2.seek(0)
    while True:
        fruta = input("Informe uma fruta ou 'sair': ")
        if fruta != 'sair':
            file2.write(f'{fruta} \n')
        else:
            break"""

