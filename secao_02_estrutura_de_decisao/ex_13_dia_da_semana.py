"""
Exercício 13 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.

    >>> calcular_dia_da_semana(1)
    'Domingo'
    >>> calcular_dia_da_semana(2)
    'Segunda'
    >>> calcular_dia_da_semana(3)
    'Terça'
    >>> calcular_dia_da_semana(4)
    'Quarta'
    >>> calcular_dia_da_semana(5)
    'Quinta'
    >>> calcular_dia_da_semana(6)
    'Sexta'
    >>> calcular_dia_da_semana(7)
    'Sábado'
    >>> calcular_dia_da_semana(8)
    'Dia Inválido'
    >>> calcular_dia_da_semana(0)
    'Dia Inválido'

"""


def calcular_dia_da_semana(numero: int):
    """Escreva aqui em baixo a sua solução"""
    if numero == 1:
        return 'Domingo'
    elif numero == 2:
        return 'Segunda'
    elif numero == 3:
        return 'Terça'
    elif numero == 4:
        return 'Quarta'
    elif numero == 5:
        return 'Quinta'
    elif numero == 6:
        return 'Sexta'
    elif numero == 7:
        return 'Sábado'
    else:
        return 'Dia Inválido'
