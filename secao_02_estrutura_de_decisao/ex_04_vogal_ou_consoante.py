"""
Exercício 04 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

    >>> vogal_ou_consoante("F")
    'consoante'
    >>> vogal_ou_consoante("a")
    'vogal'
    >>> vogal_ou_consoante('c')
    'consoante'
    >>> vogal_ou_consoante('U')
    'vogal'
"""


def vogal_ou_consoante(letra):
    """Escreva aqui em baixo a sua solução"""
    if letra == 'a' or letra == 'A' or letra == 'e' or letra == 'E' or letra == 'i' or letra == 'I' or letra == 'o' or letra == 'O' or letra == 'u' or letra == 'U':
        print("'vogal'")
    else:
        print("'consoante'")
