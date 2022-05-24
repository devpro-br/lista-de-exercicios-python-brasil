"""
Exercício 07 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
Mostrar a área com 2 casas decimais.

    >>> from secao_01_estrutura_sequencial import ex_07_area_quadrado
    >>> ex_07_area_quadrado.input = lambda k: '2'
    >>> ex_07_area_quadrado.calcular_area_de_quadrado()
    A área do quadrado com esse lado é: 4.00
    O dobro da aŕea do quadrado é: 8.00
    >>> ex_07_area_quadrado.input = lambda k: '2.5'
    >>> ex_07_area_quadrado.calcular_area_de_quadrado()
    A área do quadrado com esse lado é: 6.25
    O dobro da aŕea do quadrado é: 12.50

"""


def calcular_area_de_quadrado():
    import math
    lado = float(input("Digite o lado do quadrado: "))
    print(f"A área do quadrado com esse lado é: {lado*lado:.2f}")
    print(f"O dobro da aŕea do quadrado é: {lado*lado*2:.2f}")


