"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça dois números inteiros e imprima a soma.

    >>> from secao_01_estrutura_sequencial import ex_03_imprima_soma_de_dois_numeros
    >>> numeros =['42', '43']
    >>> ex_03_imprima_soma_de_dois_numeros.input = lambda k: numeros.pop()
    >>> ex_03_imprima_soma_de_dois_numeros.imprima_a_soma_de_dois_numeros()
    A soma dos dois números informados é 85

"""


def imprima_a_soma_de_dois_numeros():
    numero_1 = int(input('Entre com o primeiro número: '))
    numero_2 = int(input('Entre com o segundo número: '))
    print(f'A soma dos dois números informados é {numero_1 + numero_2}')

imprima_a_soma_de_dois_numeros(42)
imprima_a_soma_de_dois_numeros(43)