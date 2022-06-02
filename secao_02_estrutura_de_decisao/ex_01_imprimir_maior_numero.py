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


def maior_de_dois_numeros(x, y):
    """Escreva aqui em baixo a sua solução"""

    num1 = int(input("Digite um número"))
    num2 = int(input("Digite outro número"))
    if num1 > num2:
        print(num1)
    else:
        print(num2)
