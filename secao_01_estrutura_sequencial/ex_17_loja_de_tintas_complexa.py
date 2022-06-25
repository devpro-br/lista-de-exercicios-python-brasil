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

    area_a_ser_pintada = int(input('Qual a área em metros a ser pintada? '))
    area_com_folga = area_a_ser_pintada * 1.1
    metros_por_litro = 6
    litros_a_serem_usados = math.ceil(area_com_folga / metros_por_litro)

    litros_por_lata = 18
    valor_18_l = 80
    numero_de_latas_18 = math.ceil(litros_a_serem_usados / litros_por_lata)
    valor_somente_latas = numero_de_latas_18 * valor_18_l
    sobra_de_litros_18 = (numero_de_latas_18 * litros_por_lata) - litros_a_serem_usados

    litros_por_galao = 3.6
    valor_3_6_l = 25
    numero_de_galoes_3_6 = math.ceil(litros_a_serem_usados / litros_por_galao)
    valor_somente_galoes = numero_de_galoes_3_6 * valor_3_6_l
    sobra_de_litros_3_6 = (numero_de_galoes_3_6 * litros_por_galao) - litros_a_serem_usados

    numero_de_latas_18_cheias = math.floor(litros_a_serem_usados / litros_por_lata)
    valor_com_latas = numero_de_latas_18_cheias * valor_18_l
    litros_faltantes = litros_a_serem_usados % litros_por_lata
    numero_de_galoes_para_completar = math.ceil(litros_faltantes / litros_por_galao)
    Valor_com_galoes = numero_de_galoes_para_completar * valor_3_6_l
    valor_total = valor_com_latas + Valor_com_galoes
    total_de_litros_com_lata_e_galoes = (numero_de_latas_18_cheias * litros_por_lata) + (numero_de_galoes_para_completar * litros_por_galao)
    sobra_de_tinta = total_de_litros_com_lata_e_galoes - litros_a_serem_usados

    print(f'Você deve comprar {litros_a_serem_usados} litros de tinta.')
    print(f'Você pode comprar {numero_de_latas_18} lata(s) de 18 litros a um custo de R$ {valor_somente_latas}. Vão sobrar {sobra_de_litros_18:.1f} litro(s) de tinta.')
    print(f'Você pode comprar {numero_de_galoes_3_6} lata(s) de 3.6 litros a um custo de R$ {valor_somente_galoes}. Vão sobrar {sobra_de_litros_3_6:.1f} litro(s) de tinta.')
    print(f'Para menor custo, você pode comprar {numero_de_latas_18_cheias} lata(s) de 18 litros e {numero_de_galoes_para_completar} galão(ões) de 3.6 litros a um custo de R$ {valor_total}. Vão sobrar {sobra_de_tinta:.1f} litro(s) de tinta.')
