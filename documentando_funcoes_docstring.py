"""
DOCUMENTANDO FUNÇÕES COM DOC STRING:
 - o comentário aqui é uma doc string;
 - É importante documentar partes importantes do código;
 - deixar documentado para auxiliar o entendimento do código;
print(help(print))
 - Podemos acessar a documentação de uma função usando a propriedade especial __doc__;
 - POdemos acessar a documentação usando também a função help.
"""
"""
def diz_oi():
    #"""Uma função simples que retorna a string 'oi!'"""
    return 'Oi!'
"""
"""
print(diz_oi())
print(help(diz_oi))
print(diz_oi.__doc__)

"""

def exponencial(numero, potencia=2):
    """
    FUnção que retorna por padrão o quadrado de um 'número' ou número à potencia informada.
    :param numero: numero que desejamos gerar o exponencial.
    :param potenia: potencia que queremos gerar o exponencial, por padrão 2.
    :return: retorna o exponencial de número por potencia.
    """
    return numero ** potencia

