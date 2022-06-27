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
    
    numero = valor
    centena = int(numero / 100)
    dezena = int((numero - (centena * 100)) / 10)
    unidade = numero - (centena * 100 + (dezena * 10))

    nota_100 = centena

    if dezena >= 5:
        nota_50 = 1
        nota_10 = dezena - 5
    elif dezena < 5:
        nota_10 = dezena

    if unidade >=5:
        nota_5 = 1
        nota_1 = unidade - 5
    else:
        nota_1 = unidade

    if centena == 0 and dezena == 0 and unidade == 1:
        print(f"'{unidade} nota de R$ 1'")
    if centena == 0 and dezena == 0 and unidade >= 5:
        print(f"'{nota_5} nota de R$ 5'")

    if centena == 0 and dezena == 1 and unidade == 0:
        print(f"'{dezena} nota de R$ 10'")
    if centena == 0 and dezena == 1 and unidade == 1:
        print(f"'{dezena} nota de R$ 10 e {unidade} nota de R$ 1'")

    if centena > 1 and dezena >5 and unidade >= 5:
        print(f"'{centena} notas de R$ 100, {nota_50} nota de R$ 50, {nota_10} notas de R$ 10, {nota_5} nota de R$ 5 e {nota_1} notas de R$ 1'")

    if centena > 1 and dezena == 5 and unidade > 1:
        print(f"'{centena} notas de R$ 100, {nota_50} nota de R$ 50, {nota_5} nota de R$ 5 e {nota_1} nota de R$ 1'")