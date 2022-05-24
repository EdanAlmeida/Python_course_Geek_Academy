"""
DECORATORS:

OBS = IMPORTANTE PERCEBER QUE O DECORATOR MUDA O COMPORTAMENTO DAS FUNÇÕES!

    - São funções;
    - envolvem outras funções e aprimoram seus comportamentos;

|_______________________________________________________________|
                  Function Decorator
|_______________________________________________________________|

                        Function
|_______________________________________________________________|

#A função é decorada pelos decorators;

    - Decorators == HOF
    - Sintaxe própria "@" (Syntatic Sugar) [perfumaria];




#Decorator como funções (NÃO RECOMENDADO!):
def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhecer voce!")
        funcao()
        print("Tenha um ótimo dia!")
    return sendo


def saudacao():
    print("Seja bem vindo(a) à Geek University!")


#Teste 1:
teste = seja_educado(saudacao)
teste()

print()

#Teste 2:
def raiva():
    print('EU TE ODEIO! ')


raiva_educada = seja_educado(raiva) #raiva() é decorada com a outra função;
raiva_educada()



#Decorator with Syntax Sugar (FORMA RECOMENDADA!)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print("Foi um prazer conhecer voce")
        funcao()
        print("Tenha um excelente dia!")
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print("Meu nome eh Edan!")


#Teste:
apresentando()


@seja_educado_mesmo
def dormir():
    print("Quero dormir...")


dormir()


#EX WEBSITE:

|_____________________________________________________________________|
|    Home    |    Serviços     |     Produtos     |         Adm       |
|_____________________________________________________________________|

http://www.suaempresa.com.br/home
http://www.suaempresa.com.br/servicos
http://www.suaempresa.com.br/produtos
http://www.suaempresa.com.br/admin

#Apenas exemplo
def checa_login():
    if not request.usuario:
        redirect ('http://www.suaempresa.com.br')


def home(request):
    return 'Pode acessar home'

def servicos(request):
    return 'Pode acessar servicos'

def produtos(request):
    return 'Pode acessar produtos'

@checa_login
def admin(request):
    return 'Pode acessar admin'


OBS = Não confunda decorator com decorator function!
    - DEcorator Function == função decoradora;
    - Decorator == chamada do decorator em outra função.

"""

#Decorator with Syntax Sugar (FORMA RECOMENDADA!)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print("Foi um prazer conhecer voce")
        funcao()
        print("Tenha um excelente dia!")
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print("Meu nome eh Edan!")


#Teste:
apresentando()


@seja_educado_mesmo
def dormir():
    print("Quero dormir...")


dormir()
