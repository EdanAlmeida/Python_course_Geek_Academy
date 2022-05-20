"""
DUNDER [MAIN and NAME]:

    - Dunder name -> __name__ (double under)

    - são vários métodos que usam o dunder:
        - if __name__=="__main__":
            ['__annotations__', '__builtins__', '__cached__', '__doc__',
            '__file__', '__loader__', '__name__', '__package__', '__spec__']

- eles evitam conflitos com nomes de variáveis e funções dentro da programação;

- Em 'C' == sem essa função não existe programa 'C'
    int main(){
        return 0;
    }

- Em 'Java' == sem a função abaixo, não existe programa Java:
    - public static void main(String[] args){
    }

- Em python isso não existe: internamente o Python atribui à variável '__name__' o valor '__main__'.
- Indicando que esse é o módulo de execução principal;

"""

print(dir())

print(__name__) # já está rodando


# Na construção dos módulos, é importante usar: if __name__=="__main__"
#Módulos não deve conter print;

from funcoes_parametros import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))
