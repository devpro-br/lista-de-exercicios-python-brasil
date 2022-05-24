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
    area = float(input('Digite o tamanho da área a ser pintada em m²: '))
    area_com_folga = area * 1.1
    litros_por_metro = 6
    litros_necessarios = area_com_folga / litros_por_metro
    print(f'Você deve comprar {litros_necessarios:.0f} litros de tinta.')
  
    # Cálculo em latas
    litros_por_lata = 18
    numero_de_latas = math.ceil(litros_necessarios / litros_por_lata)
    valor_em_latas = numero_de_latas * 80
    resto_em_litros = (numero_de_latas * litros_por_lata) % litros_necessarios
    print(f'Você pode comprar {numero_de_latas} lata(s) de 18 litros a um custo de R$ {valor_em_latas}. Vão sobrar {resto_em_litros:.1f} litro(s) de tinta.')

    # Cálculo em galões
    litros_por_galao = 3.6
    numero_de_galoes = math.ceil(litros_necessarios / litros_por_galao)
    valor_em_galoes = numero_de_galoes * 25
    resto_em_litros = (numero_de_galoes * litros_por_galao) % litros_necessarios
    print(f'Você pode comprar {numero_de_galoes} lata(s) de 3.6 litros a um custo de R$ {valor_em_galoes}. Vão sobrar {resto_em_litros:.1f} litro(s) de tinta.')
    
    # Cálculo em latas e galões
    numero_de_latas = math.floor(litros_necessarios / litros_por_lata)
    valor_em_latas = numero_de_latas * 80
    resto_em_litros = litros_necessarios % litros_por_lata
    numero_de_galoes = math.ceil(resto_em_litros / litros_por_galao)
    valor_em_galoes = numero_de_galoes * 25
    valor_total = valor_em_latas + valor_em_galoes
    resto_final = ((numero_de_latas*18 + numero_de_galoes*3.6)) % litros_necessarios
    print(f'Para menor custo, você pode comprar {numero_de_latas} lata(s) de 18 litros e {numero_de_galoes} galão(ões) de 3.6 litros a um custo de R$ {valor_total}. Vão sobrar {resto_final:.1f} litro(s) de tinta.')

