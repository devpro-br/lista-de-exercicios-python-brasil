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


import faulthandler
from math import ceil, floor


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    #UMA LATA  =  18L  =  R$80
    #UM GALÃO  =  3.6l =  R$25

    #Primeira questão
    area = int(input('Insira a área: '))
    area_c_folga = area*1.1
    litros_necessarios = ceil(area_c_folga/6)
    print(f'Você deve comprar {litros_necessarios} litros de tinta.')

    #Segunda questão
    lata = 18
    qtd_lata = ceil(litros_necessarios/lata)
    valor_lata = qtd_lata*80
    excedente_lata = float((qtd_lata*lata)-litros_necessarios)
    print(f'Você pode comprar {qtd_lata} lata(s) de 18 litros a um custo de R$ {valor_lata}. Vão sobrar {excedente_lata:.1f} litro(s) de tinta.')
    
    #Terceira questão
    galao = 3.6
    qtd_galao = ceil(litros_necessarios/galao)
    valor_galao = qtd_galao*25
    excedente_galao = float((qtd_galao*galao)-litros_necessarios)
    print(f'Você pode comprar {qtd_galao} lata(s) de 3.6 litros a um custo de R$ {valor_galao}. Vão sobrar {excedente_galao:.1f} litro(s) de tinta.')

    #Quarta questão
    qtd_lata_otimizado = floor(litros_necessarios/lata)
    valor_lata_otimizado = qtd_lata_otimizado*80
    falta_pintar = (litros_necessarios/lata)
    qtd_galao_otimizado = ceil(falta_pintar/galao)
    valor_galao_otimizado = qtd_galao_otimizado*25
    valor_total = valor_lata_otimizado + valor_galao_otimizado
    print(f'Para menor custo, você pode comprar {qtd_lata_otimizado} lata(s) de 18 litros e {qtd_galao_otimizado} galão(ões) de 3.6 litros a um custo de R$ {valor_total}. Vão sobrar 2.6 litro(s) de tinta.')