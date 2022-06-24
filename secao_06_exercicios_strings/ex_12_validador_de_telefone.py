"""
Exercício 12 da seção de strings da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

    >>> from secao_06_exercicios_strings import ex_12_validador_de_telefone
    >>> numero = ['461-0133']
    >>> ex_12_validador_de_telefone.input = lambda k: numero.pop()
    >>> ex_12_validador_de_telefone.validar_telefone()
    Valida e corrige número de telefone
    Telefone: 461-0133
    Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
    Telefone corrigido sem formatação: 34610133
    Telefone corrigido com formatação: 3461-0133
    >>> numero = ['4610133']
    >>> ex_12_validador_de_telefone.input = lambda k: numero.pop()
    >>> ex_12_validador_de_telefone.validar_telefone()
    Valida e corrige número de telefone
    Telefone: 4610133
    Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
    Telefone corrigido sem formatação: 34610133
    Telefone corrigido com formatação: 3461-0133
    >>> numero = ['14610133']
    >>> ex_12_validador_de_telefone.input = lambda k: numero.pop()
    >>> ex_12_validador_de_telefone.validar_telefone()
    Valida e corrige número de telefone
    Telefone: 14610133
    Telefone corrigido sem formatação: 14610133
    Telefone corrigido com formatação: 1461-0133

"""


def validar_telefone():
    """Escreva aqui em baixo a sua solução"""
