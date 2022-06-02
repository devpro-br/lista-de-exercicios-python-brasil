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

from math import ceil, floor


# lata
    area_a_ser_pintada = int(input('Digite a área a ser pintada em m2: '))
    area_com_folga = float(area_a_ser_pintada *1.1)
    litros_por_metro = 6
    litros_a_serem_usados = ceil(area_com_folga / litros_por_metro)
    litros_por_lata = 18
    numero_de_latas = ceil(litros_a_serem_usados /litros_por_lata)
    valor_com_apenas_latas = numero_de_latas * 80
    sobra_da_tinta = (numero_de_latas * litros_por_lata) - litros_a_serem_usados
    print(f'Você pode comprar {numero_de_latas} lata(s) de 18 litros a um custo de R$ {valor_com_apenas_latas}. Vão sobrar {sobra_da_tinta:.1f} litro(s) de tinta.')

# galao
    litros_por_galao = 3.6
    numero_de_galoes = ceil(litros_a_serem_usados / litros_por_galao)
    valor_com_apenas_galoes = numero_de_galoes * 25
    sobra_do_galao = (numero_de_galoes * litros_por_galao) - litros_a_serem_usados
    print(f'Você pode comprar {numero_de_galoes} lata(s) de 3.6 litros a um custo de R$ {valor_com_apenas_galoes}. Vão sobrar {sobra_do_galao:.1f} litro(s) de tinta.')

# lata e galao juntos
    numero_de_latas_baixo = floor(litros_a_serem_usados - litros_por_lata)
    valor_de_latas = numero_de_latas * 80



    litros_faltantes = litros_a_serem_usados % litros_por_lata
    numero_de_galoes_baixo = ceil(litros_faltantes / litros_por_galao)
    valor_com_galoes = numero_de_galoes * 25



    valor_total = numero_de_latas_baixo *80 + numero_de_galoes_baixo * 25 

    sobra = (numero_de_latas_baixo + numero_de_galoes_baixo) 

    print(f'Para menor custo, você pode comprar {numero_de_latas_baixo} lata(s) de 18 litros e {numero_de_galoes_baixo} galão(ões) de 3.6 litros a um custo de R$ {valor_total}. Vão sobrar {sobra:.1f} litro(s) de tinta.')