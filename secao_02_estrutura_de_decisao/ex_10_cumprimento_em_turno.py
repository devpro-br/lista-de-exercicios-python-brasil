"""
Exercício 10 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

    >>> cumprimentar('M')
    'Bom dia!'
    >>> cumprimentar('m')
    'Bom dia!'
    >>> cumprimentar('V')
    'Boa tarde!'
    >>> cumprimentar('v')
    'Boa tarde!'
    >>> cumprimentar('N')
    'Boa noite!'
    >>> cumprimentar('n')
    'Boa noite!'
    >>> cumprimentar('X')
    'Valor Inválido!'

"""


def cumprimentar(turno: str):
    #turno = input('Em que turno você estuda?  (M)atutino  (V)espertino (N)oturno ').lower()

    turno = turno.lower()

    if turno == 'm':
        mensagem = "'Bom Dia!'"
    elif turno == 'v':
        mensagem = "'Boa Tarde!'"
    elif turno == 'n':
        mensagem = "'Boa Noite!'"
    else:
        mensagem = "'Valor Inválido!'"

    print(mensagem)

