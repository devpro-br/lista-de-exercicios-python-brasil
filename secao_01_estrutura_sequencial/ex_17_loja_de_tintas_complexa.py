"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    import math
    area = float(input('Área a ser pintada: '))
    litros = math.ceil((area/6) *1.10)

    # Quantidade de latas de tinta de 18 litros
    qtd_latas1 = math.ceil(litros / 18)
    preco_tinta1 = math.ceil(qtd_latas1 * 80)
    sobra_1 = qtd_latas1 * 18 - litros

    # Quantidade de latas de tinta de 3,6 litros
    qtd_latas2 = math.ceil(litros/ 3.6)
    preco_tinta2 = math.ceil(qtd_latas2 * 25)
    sobra_2 = qtd_latas2 * 3.6 - litros

    # Quantidades misturadas
    qtd_latas_18 = round(litros / 18)
    qtd_latas_3 = math.ceil((litros - qtd_latas_18 * 18)/ 3.6)
    preco = qtd_latas_18 * 80 + qtd_latas_3 * 25
    sobra_mistura =(qtd_latas_18 * 18) + (qtd_latas_3 * 3.6) - litros

    print(f'Você deve comprar {litros} litros de tinta.')
    print(f'Você pode comprar {qtd_latas1} lata(s) de 18 litros a um custo de R$ {preco_tinta1}. Vão sobrar {sobra_1:.1f} litro(s) de tinta.')
    print(f'Você pode comprar {qtd_latas2} lata(s) de 3.6 litros a um custo de R$ {preco_tinta2}. Vão sobrar {sobra_2 :.1f} litro(s) de tinta.')
    print(f'Para menor custo, você pode comprar {qtd_latas_18} lata(s) de 18 litros e {qtd_latas_3} galão(ões) de 3.6 litros a um custo de R$ {preco}. Vão sobrar {sobra_mistura :.1f} litro(s) de tinta.')
