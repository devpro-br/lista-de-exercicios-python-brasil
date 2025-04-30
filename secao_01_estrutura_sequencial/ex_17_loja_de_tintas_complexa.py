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
def calcular_latas_e_preco_de_tinta(area):
    area_com_folga = area * 1.10
    litros = area_com_folga / 6
    latas = math.ceil(litros / 18)
    preco_latas = latas * 80
    sobra_latas = (latas * 18) - litros
    galoes = math.ceil(litros / 3.6)
    preco_galoes = galoes * 25
    sobra_galoes = (galoes * 3.6) - litros
    melhor_preco = float('inf')
    melhor_latas = 0
    melhor_galoes = 0
    sobra_mistura = 0
    
    for latas_usadas in range(latas + 1):
        litros_usados = latas_usadas * 18
        litros_restantes = max(0, litros - litros_usados)
        galoes_usados = math.ceil(litros_restantes / 3.6)
        
        custo_total = (latas_usadas * 80) + (galoes_usados * 25)
        sobra = (latas_usadas * 18 + galoes_usados * 3.6) - litros
        
        if custo_total < melhor_preco:
            melhor_preco = custo_total
            melhor_latas = latas_usadas
            melhor_galoes = galoes_usados
            sobra_mistura = sobra
    
    # Exibindo os resultados
    print(f"Você deve comprar {math.ceil(litros)} litros de tinta.")
    print(f"Você pode comprar {latas} lata(s) de 18 litros a um custo de R$ {preco_latas}. Vão sobrar {sobra_latas:.1f} litro(s) de tinta.")
    print(f"Você pode comprar {galoes} galão(ões) de 3.6 litros a um custo de R$ {preco_galoes}. Vão sobrar {sobra_galoes:.1f} litro(s) de tinta.")
    print(f"Para menor custo, você pode comprar {melhor_latas} lata(s) de 18 litros e {melhor_galoes} galão(ões) de 3.6 litros a um custo de R$ {melhor_preco}. Vão sobrar {sobra_mistura:.1f} litro(s) de tinta.")
    
while True:
    try:
        area = float(input("Insira o tamanho em metros quadrados da área a ser pintada: "))
        if area <= 0:
            print("A área deve ser um número positivo!")
            continue
        break
    except ValueError:
        print("Insira uma área válida!")
        
calcular_latas_e_preco_de_tinta(area)