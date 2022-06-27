"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.
    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""

    saque = valor
    notas_de_100 = notas_de_50 = notas_de_10 = notas_de_5 = notas_de_1 = 0
    notas_de_100, saque = divmod(saque, 100)
    notas_de_50, saque = divmod(saque, 50)
    notas_de_10, saque = divmod(saque, 10)
    notas_de_5, notas_de_1 = divmod(saque, 5)
    parte = 0

    print("'",end="")
    if notas_de_100 == 1:
        print(f"{notas_de_100} nota de R$ 100",end="")
        parte += 1
    elif notas_de_100 > 1:
        print(f"{notas_de_100} notas de R$ 100",end="")
        parte += 1
    if notas_de_50 != 0 and parte == 1:
        print(",",end=" ")
    if notas_de_50 == 1:
        print(f"{notas_de_50} nota de R$ 50",end="")
        parte += 1
    elif notas_de_50 > 1:
        print(f"{notas_de_50} notas de R$ 50",end="")
        parte += 1
    if parte != 0 and notas_de_10 != 0:
        print(",",end=" ")
    if notas_de_10 == 1:
        print(f"{notas_de_10} nota de R$ 10",end="")
        parte += 1
    elif notas_de_10 > 1:
        print(f"{notas_de_10} notas de R$ 10",end="")
        parte += 1
    if parte != 0 and notas_de_5 != 0:
        print(",",end=" ")
    if notas_de_5 == 1:
        print(f"{notas_de_5} nota de R$ 5",end="")
        parte += 1
    elif notas_de_5 > 1:
        print(f"{notas_de_5} notas de R$ 5",end="")
        parte += 1
    if parte != 0 and notas_de_1 != 0:
        print(" e",end=" ")
    if notas_de_1 == 1:
        print(f"{notas_de_1} nota de R$ 1",end="")
    elif notas_de_10 > 1:
        print(f"{notas_de_1} notas de R$ 1",end="")
    print("'")
