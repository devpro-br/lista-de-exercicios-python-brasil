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

import math


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    a_quadrada = float(input('Digite o valor da área para cálculo: '))
    a_folga = a_quadrada * 1.1
    li_pm = math.ceil(a_folga / 6)
    lata_li = math.ceil(li_pm / 18)
    galao_li = math.ceil(li_pm / 3.5)
    preco_lata = lata_li * 80
    preco_galao = galao_li * 25
    sobra_lata = (lata_li * 18) - li_pm
    sobra_galao = (galao_li * 3.6) - li_pm
    resto = li_pm % 18
    latas_int = math.floor(li_pm / 18)
    galao_resto = math.ceil(resto / 3.6)
    la_ga = (latas_int * 80) + (galao_resto * 25)
    res_tot = ((latas_int * 18) + (galao_resto * 3.6)) - li_pm

    print(f'Você deve comprar {li_pm} litros de tinta.')
    print(
        f'Você pode comprar {lata_li} lata(s) de 18 litros a um custo de R$ {preco_lata}. Vão sobrar {sobra_lata:.1f} litro(s) de tinta.')
    print(
        f'Você pode comprar {galao_li} lata(s) de 3.6 litros a um custo de R$ {preco_galao}. Vão sobrar {sobra_galao:.1f} litro(s) de tinta.')
    print(
        f'Para menor custo, você pode comprar {latas_int} lata(s) de 18 litros e {galao_resto} galão(ões) de 3.6 litros a um custo de R$ {la_ga:.0f}. Vão sobrar {res_tot:.1f} litro(s) de tinta.')