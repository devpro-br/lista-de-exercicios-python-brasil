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
    Você deve comprar 18 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.7 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 3.3 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 3.3 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.3 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.9 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.9 litro(s) de tinta.

"""


def calcular_latas_e_preco_de_tinta():
    from math import ceil
    area = float(input("Qual a area que vai ser pintada? (em metros quadrados): "))
    litros = round(area/6 + (area/6*0.1),1)
    litros10 = round(area/6 + (area/6*0.1),1)
    qtdelata18 = ceil(litros/18)
    qtdelata36 = ceil(litros/3.6)
    qtdlata18c = 0
    qtdlata36c = 0
    print(f"Você deve comprar {round(litros)} litros de tinta.")
    print(f'Você pode comprar {qtdelata18} lata(s) de 18 litros a um custo de R$ {qtdelata18*80}. Vão sobrar {round(qtdelata18*18-litros,1)} litro(s) de tinta.')
    print(f'Você pode comprar {qtdelata36} lata(s) de 3.6 litros a um custo de R$ {qtdelata36*25}. Vão sobrar {round(qtdelata36*3.6-litros,1)} litro(s) de tinta.')
    while litros10 >= 18:
        if litros10 >= 18:
            qtdlata18c += 1
            litros10 -= 18
    while litros10 >= 3.6:
        qtdlata36c += 1
        litros10 -= 3.6
    if litros10 < 3.6 and litros10 > 0:
        qtdlata36c += 1
    print(f'Para menor custo, você pode comprar {qtdlata18c} lata(s) de 18 litros e {qtdlata36c} galão(ões) de 3.6 litros a um custo de R$ {(qtdlata18c*80) + (qtdlata36c*25)}. Vão sobrar {round(qtdlata18c*18+qtdlata36c*3.6-round(area/6 + (area/6*0.1),1),1)} litro(s) de tinta.')

