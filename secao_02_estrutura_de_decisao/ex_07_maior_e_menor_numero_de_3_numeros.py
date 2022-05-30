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
    """Escreva aqui em baixo a sua solução"""
    if y < x > z:
        if y > z:
            resp = f"Maior: {x}\nMenor: {z}"
        elif z > y:
            resp = f"Maior: {x}\nMenor: {y}"
    elif z < y > x:
        if z > x:
            resp = f"Maior: {y}\nMenor: {x}"
        elif z < x:
            resp = f"Maior: {y}\nMenor: {z}"
    elif y < z > x:
        if y > x:
            resp = f"Maior: {z}\nMenor: {x}"
        elif y < x:
            resp = f"Maior: {z}\nMenor: {y}"
    
    print(resp)
    