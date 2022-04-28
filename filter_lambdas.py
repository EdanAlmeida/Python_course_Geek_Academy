"""
FILTER:

 - serve para filtrar dados de uma determinada coleção;
#Forma manual:
    valores = 1, 2, 3, 4, 5, 6 # Tupla
    media = (sum(valores)) / len(valores)
    print(media)



#Forma melhor
import statistics

#Dados coletados de algum sensor:
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#Calculando a média dos dados utilizando a função 'mean()':

media = statistics.mean(dados)
print(f'{media:.2f}')

#APlicando filter: recebe dois parâmetros (função:iterável);

res1 = filter(lambda x : x > media, dados)
print(list(res1))

res2 = filter(lambda x : x < media, dados)
print(list(res2)) #Boolean

#Valor utilizável apenas uma vez, assim como na função map;
#Convertido para list, senão é um object filter.


#Removendo dados faltantes para não alterar o resultado;

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)

res = filter(None, paises) #Remove os None;
print(list(res))

#Forma 'errada':
res2 = filter(lambda pais: len(pais) > 0, paises)
print(list(res2))


# A diferença entre map e filter é:
# MAP = recebe dois parâmetros [função e iterável] e retorna um objeto mapeando a função para cada iterável;
# FILTER = recebe dois parâmetros [função e iterável] e retorna um objeto filtrando apenas os elementos de acordo com a # função
#Map = valores que não true or false;
#Filter = valores booleanos;

#Exemplo mais complexo:

#Forma 1:
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolo", "Eu adoro pizza"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []},
]

print(usuarios)

# Filtrar os usuários que estão inativos no tweeter;

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)
print(len(inativos))


#Exemplo mais complexo:

#Forma 2 - refatorando:
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolo", "Eu adoro pizza"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []},
]

print(usuarios)

# Filtrar os usuários que estão inativos no tweeter;

inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)
print(len(inativos))

#Lista vazia transformada em boolean é False;

"""

# Combinando Filter e Map:

nomes = ['Vanessa', 'Ana', 'Maria']

# Criar uma lista contendo 'Sua instrutora é' + nome da instrutora, desde que cada nome tenha menos de 5 caracteres:

lista = list(map(lambda nome: f'Sua instrutora eh {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

# O FILTER está detro do MAP
