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
    if data == '':
        return 'Data inválida'
    try:
        dia, mes, ano = data.split('/')
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        if dia < 1 or dia > 31:
            return 'Data inválida'
        if mes < 1 or mes > 12:
            return 'Data inválida'
        if mes == 2:
            if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                if dia > 29:
                    return 'Data inválida'
            else:
                if dia > 28:
                    return 'Data inválida'
        if mes in [4, 6, 9, 11]:
            if dia > 30:
                return 'Data inválida'
        return 'Data válida'
    except:
        return 'Data inválida'