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
    # 1, 5, 10, 50 e 100 reais
    notas_100 = notas_50 = notas_10 = notas_5 = notas_1 = 0
    
    notas_100, valor = divmod(valor, 100)
    notas_50, valor = divmod(valor, 50)
    notas_10, valor = divmod(valor, 10)
    notas_5, valor = divmod(valor, 5)
    notas_1, valor = divmod(valor, 1)

    if notas_100 > 1:
        notas_100 += 1
    else:
        notas_100 += 0
    #     print(f'{notas_100} nota de 100')
    # elif notas_100 > 1:
    #     print(f'{notas_100} notas de 100')

    if notas_50 > 1:
        notas_50 += 1
    else:
        notas_50 += 0 
    #     print(f'{notas_50} nota de 50')
    # elif notas_50 > 1:
    #     print(f'{notas_50} notas de 50')
            
    if notas_10 > 1:
        notas_10 += 1
    else:
        notas_10 += 0 
    #     print(f'{notas_10} nota de 10')
    # elif notas_10 > 1:
    #     print(f'{notas_10} notas de 10')

    if notas_5 > 1:
        notas_5 += 1
    else:
        notas_5 += 0 
    #     print(f'{notas_5} nota de 5')
    # elif notas_5 > 1:
    #     print(f'{notas_5} notas de 5')
    
    if notas_1 > 1:
        notas_1 += 1
    else:
        notas_1 += 0 
    #     print(f'{notas_1} nota de 1')
    # elif notas_1 > 1:
    #     print(f'{notas_1} notas de 1')
    print(f'{notas_100} notas de R$ 100, {notas_50} nota de R$ 50, {notas_10} notas de R$ 10, {notas_5} nota de R$ 5 e {notas_1} notas de R$ 1')