"""
Exercício 06 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior deles.

    >>> calcular_maior_de_3_numeros(2,3, 5)
    5
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    -1
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    3
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    15
"""


def calcular_maior_de_3_numeros(x, y, z):
    """Escreva aqui em baixo a sua solução"""
    maior = x
    if y > maior:
        maior = y
    if z > maior:
        maior = z
    print(maior)

while True:
    try:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        z = float(input("Digite o terceiro número: "))
        break
    except ValueError:
        print("Insira um número válido!")
calcular_maior_de_3_numeros(x, y, z)