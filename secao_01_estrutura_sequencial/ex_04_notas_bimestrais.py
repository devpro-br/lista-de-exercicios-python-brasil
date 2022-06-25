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

    nota_1 = float(input('Digite a primeira nota: '))
    nota_2 = float(input('Digite a segunda nota: '))
    nota_3 = float(input('Digite a terceira nota: '))
    nota_4 = float(input('Digite a quarta nota: '))

    media_aluno = (nota_1 + nota_2 + nota_3 + nota_4) / 4

    print(f'A média anual é {media_aluno}')


"""
(Solução 2)
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

    >>> from secao_01_estrutura_sequencial import ex_04_notas_bimestrais
    >>> numeros =['7', '8','9','10']
    >>> ex_04_notas_bimestrais.input = lambda k: numeros.pop()
    >>> ex_04_notas_bimestrais.calcular_media_2()
    A média anual é 8.5

"""


def calcular_media_2():
    """Escreva aqui em baixo a sua solução"""

    notas = []
    nota_a = notas.append(float(input('Digite a primeira nota: ')))
    nota_b = notas.append(float(input('Digite a segunda nota: ')))
    nota_c = notas.append(float(input('Digite a terceira nota: ')))
    nota_d = notas.append(float(input('Digite a quarta nota: ')))

    media_aluno_2 = sum(notas) / 4

    print(f'A média anual é {media_aluno_2}')
