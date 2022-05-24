"""
Exercício 05 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que converta metros para centímetros.

    >>> from secao_01_estrutura_sequencial import ex_05_metros_para_centimetros
    >>> ex_05_metros_para_centimetros.input = lambda k: '1'
    >>> ex_05_metros_para_centimetros.converter_metros_para_centrimetros()
    Transformando para centímetros dá 100.0 cm
    >>> ex_05_metros_para_centimetros.input = lambda k: '3.621'
    >>> ex_05_metros_para_centimetros.converter_metros_para_centrimetros()
    Transformando para centímetros dá 362.1 cm

"""


def converter_metros_para_centrimetros():
    """Escreva aqui em baixo a sua solução"""
    centimetro = 0
    metros = float(input('Digite o valor em metros'))
    centimetro = metros*100
    print('Transformando para centímetros dá', centimetro, 'cm')

    
