"""
Exercício 07 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior e o menor deles.

    >>> calcular_maior_de_3_numeros(2,3, 5)
    Maior: 5
    Menor: 2
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    Maior: -1
    Menor: -10
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    Maior: 3
    Menor: -5
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    Maior: 15
    Menor: -14
"""


def calcular_maior_de_3_numeros(x, y, z):
    """Escreva aqui em baixo a sua solução""",
    MaiorXY = ((x+y+abs(x-y))/2)
    MaiorXYZ = ((MaiorXY+z+abs(MaiorXY-z))/2)
    MenorXY = ((x+y-abs(x-y))/2)
    MenorXYZ = ((MenorXY+z-abs(MenorXY-z))/2)
    print("Maior:",int(MaiorXYZ))
    print("Menor:",int(MenorXYZ))