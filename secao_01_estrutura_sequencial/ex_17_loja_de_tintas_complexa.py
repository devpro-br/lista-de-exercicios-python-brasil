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

    from math import ceil
    M2_POR_LITRO = 6
    PRECO_GALAO = 80
    LITROS_GALAO = 18
    PRECO_LATA = 25
    LITROS_LATA = 3.6
    MARGEM_SEGURANCA = 1.1

    m2 = float(input('informe a quantidade de METRO QUADRADO (m²) a ser pintado: '))

    consumo_litro = ceil(m2 / M2_POR_LITRO * MARGEM_SEGURANCA)
    qtd_galao_apenas = ceil(consumo_litro / LITROS_GALAO)
    valor_galao_apenas = qtd_galao_apenas * PRECO_GALAO
    qtd_lata_apenas = ceil(consumo_litro / LITROS_LATA)
    valor_lata_apenas = ceil(qtd_lata_apenas * PRECO_LATA)
    qtd_galao_misto = ceil(consumo_litro // LITROS_GALAO)
    qtd_lata_misto = ceil((consumo_litro - qtd_galao_misto * LITROS_GALAO) / LITROS_LATA)
    sobra_36 = (qtd_lata_apenas * 3.6) - consumo_litro
    sobra_18 = (qtd_galao_apenas * 18) - consumo_litro
    sobra_final = (qtd_galao_misto * 18) + (qtd_lata_misto * 3.6) - consumo_litro
    valor_galao_misto = qtd_galao_misto * PRECO_GALAO
    valor_lata_misto = qtd_lata_misto * PRECO_LATA
    valor_misto_final = (qtd_galao_misto * 80) + (qtd_lata_misto * 25)

    print(f'Você deve comprar {consumo_litro:.0f} litros de tinta.')
    print(f'Você pode comprar {qtd_galao_apenas:.0f} lata(s) de 18 litros a um custo de R$ {valor_galao_apenas:.0f}. Vão sobrar {sobra_18:.1f} litro(s) de tinta.')
    print(f'Você pode comprar {qtd_lata_apenas:.0f} lata(s) de 3.6 litros a um custo de R$ {valor_lata_apenas:.0f}. Vão sobrar {sobra_36:.1f} litro(s) de tinta.')
    print(f'Para menor custo, você pode comprar {qtd_galao_misto:.0f} lata(s) de 18 litros e {qtd_lata_misto:.0f} galão(ões) de 3.6 litros a um custo de R$ {valor_misto_final:.0f}. Vão sobrar {sobra_final:.1f} litro(s) de tinta.')
