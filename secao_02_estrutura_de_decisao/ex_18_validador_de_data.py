"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    data_list = data.split('/')
    if len(data_list) < 3:
        print("'Data inválida'")
        return None
    if 0 < int(data_list[0]) <= 31 and 0 < int(data_list[1]) <= 12:
        if int(data_list[1]) == 2 and int(data_list[0]) > 29:
            print("'Data inválida'")
        else:
            print("'Data válida'")
    else:
        print("'Data inválida'")