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
    while True:
        try:
            nota = 0
            for _ in (1, 2, 3, 4):
                nota = nota + float(input(f'Informe a nota do bimestre {_}: '))
            print(f'A média anual é {nota / 4}')
            break
        except ValueError:
            print('Não foi digitado um número!!!')
            break


