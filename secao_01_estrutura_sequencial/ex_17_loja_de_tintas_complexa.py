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

import  math
def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    area_tinta = int(input(''))
    custo_lata = 80.00
    custo_galo = 25.00


    litros_comprar = math.ceil((area_tinta / 6) * 1.10)
    latas_comprar_lata = math.ceil((litros_comprar / 18) * 1.10)
    lista_comprar_galao= round((litros_comprar / 3.6) * 1.10)
    menor_custo_lata = litros_comprar // 18
    resto = (litros_comprar % 18)
    sobra_lata = (latas_comprar_lata * 18) - litros_comprar
    sobra_galao = ((lista_comprar_galao * 3.6) - litros_comprar)
    total_tintas =(menor_custo_lata * 18 + resto * 3.6) - litros_comprar
    print(f'Você deve comprar {litros_comprar} litros de tinta.')
    print(f'Você pode comprar {latas_comprar_lata} lata(s) de 18 litros a um custo de R$ {custo_lata *latas_comprar_lata:.0f}. Vão sobrar {sobra_lata:.1f} litro(s) de tinta.')
    print(f'Você pode comprar {lista_comprar_galao} lata(s) de 3.6 litros a um custo de R$ {custo_galo * lista_comprar_galao:.0f}. Vão sobrar {sobra_galao:.1f} litro(s) de tinta.')
    print(f'Para menor custo, você pode comprar {menor_custo_lata} lata(s) de 18 litros e {resto} galão(ões) de 3.6 litros a um custo de R$ {(resto * 25) + (menor_custo_lata * 80)}. Vão sobrar {total_tintas:.1f} litro(s) de tinta.')