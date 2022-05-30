"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

    >>> from secao_01_estrutura_sequencial import ex_04_notas_bimestrais
    >>> numeros =['7', '8','9','10']
    >>> ex_04_notas_bimestrais.input = lambda k: numeros.pop()
    >>> ex_04_notas_bimestrais.calcular_media()
    A média anual é 8.5

"""


def calcular_media():
    """Escreva aqui em baixo a sua solução"""

    b1 = int(input("Informe sua nota do 1 Bimestre:"))
    b2 = int(input("Informe sua nota do 2 Bimestre:"))
    b3 = int(input("Informe sua nota do 3 Bimestre:"))
    b4 = int(input("Informe sua nota do 4 Bimestre:"))
    s1 = b1 + b2 + b3 + b4
    print("A média anual é", s1 / 4)

