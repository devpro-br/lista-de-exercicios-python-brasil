"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
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
    tipos_de_notas = [100, 50, 10, 5, 1]
    aux = ''
    pedacos = 0
    quantidade_de_notas = []

    resto = valor
    while resto > 0:
        valor = divmod(resto, tipos_de_notas[pedacos])
        notas, resto = valor
        if notas > 1:
            aux = f'{notas} notas de R$ {tipos_de_notas[pedacos]}'
            quantidade_de_notas.append(aux)
        elif notas == 1:
            aux = f'{notas} nota de R$ {tipos_de_notas[pedacos]}'
            quantidade_de_notas.append(aux)
        pedacos += 1
    for i in range(len(quantidade_de_notas)):
        if i == len(quantidade_de_notas) - 1 and len(quantidade_de_notas) > 1:
            quantidade_de_notas[i] = ' e ' + quantidade_de_notas[i]
        elif len(quantidade_de_notas) > 1 and i != len(quantidade_de_notas) - 2:
            quantidade_de_notas[i] = quantidade_de_notas[i] + ', '

    return ''.join(quantidade_de_notas)


