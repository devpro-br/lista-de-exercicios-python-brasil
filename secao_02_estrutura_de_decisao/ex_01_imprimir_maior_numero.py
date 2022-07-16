"""
Exercício 01 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça dois números e imprima o maior deles.

    >>> maior_de_dois_numeros(2,3)
    3
    >>> maior_de_dois_numeros(-1,-10)
    -1
    >>> maior_de_dois_numeros(-5,3)
    3
    >>> maior_de_dois_numeros(7,-14)
    7
"""


def maior_de_dois_numeros(numero01, numero02):
    #numero01 = int(input('Entre com o primeiro número: '))
    #numero02 = int(input('Entre com o segundo  número: '))

    if numero01 > numero02:
        print(numero01)
    else:
        print(numero02)

