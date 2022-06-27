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
    area = float(input('Area'))
    area_folga = area * 1.1
    litros_tinta = round((area_folga / 6) + 0.5)

    latas = round((area_folga / (18 * 6)) + 0.5)
    custo_lata = latas * 80
    sobra_tinta_latas = (latas * 18) - litros_tinta

    galoes = round((area_folga / (3.6 * 6)) + 0.5)
    custo_galao = galoes * 25
    sobra_tinta_galoes = (galoes * 3.6) - litros_tinta

    latas_vantagem = (area_folga // (18 * 6))
    resto_latas = (area_folga % 6)
    galoes_vantagem = round((resto_latas / (3.6 * 6)) + 0.5)
    sobra_vantagem = 3.6 - round((resto_latas / 6) + 0.5)
    custo_vantagem = (latas_vantagem * 80) + (galoes_vantagem * 25)

    print(f'Você deve comprar {litros_tinta} litros de tinta.')
    print(
    f'Você pode comprar {latas} lata(s) de 18 litros a um custo de R$ {custo_lata}. Vão sobrar {sobra_tinta_latas:.1f} litro(s) de tinta.')
    print(
    f'Você pode comprar {galoes} lata(s) de 3.6 litros a um custo de R$ {custo_galao}. Vão sobrar {sobra_tinta_galoes:.1f} litro(s) de tinta.')
    print(
    f'Para menor custo, você pode comprar {latas_vantagem:.0f} lata(s) de 18 litros e {galoes_vantagem} galão(ões) de 3.6 litros a um custo de R$ {custo_vantagem:.0f}. Vão sobrar {sobra_vantagem} litro(s) de tinta.')



    