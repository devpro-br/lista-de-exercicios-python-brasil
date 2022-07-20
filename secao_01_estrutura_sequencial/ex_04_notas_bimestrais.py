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
    media1 = float(input('Digite a media do 1 bimestre '))
    media2 = float(input('Digite a media do 2 bimestre '))
    media3 = float(input('Digite a media do 3 bimestre '))
    media4 = float(input('Digite a media do 4 bimestre '))
    print (f'A média anual é {(media1 + media2 + media3 + media4) / 4}')
