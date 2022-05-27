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
from math import ceil

def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    # entrada dos metros quadrados a serem pintados
    metros = float(input("Quantos metros quadrados você vai pintar? "))
    litros = metros / 6
    
    # quantidade total de litros
    folga_litros = (10 /100) * litros
    total_litros = ceil(litros + folga_litros) 
    
    # Quantidade de latas de 18 litros 
    latas  = total_litros / 18
    sobra_latas = (ceil(latas) * 18) - total_litros
    custo_lata = ceil(latas) * 80
    
    # quantidade de galões de 3.6 litros
    galoes = total_litros / 3.6
    custo_galoes = ceil(galoes) * 25
    sobra_galoes = (ceil(galoes) * 3.6) - total_litros

    # latas e galões para um melhor custo
    lata_melhor_custo = total_litros / 18
    galao_melhor_custo = total_litros % 18
    melhor_custo = (round(lata_melhor_custo) * 80) + (galao_melhor_custo * 25)
    
    # sobra em litros das latas e galões para um melhor custo
    sobra_tintas = ((round(lata_melhor_custo) * 18) + (galao_melhor_custo * 3.6)) - total_litros 

    # resultado esperado
    print(f"Você deve comprar {total_litros} litros de tinta.")
    print(f"Você pode comprar {ceil(latas)} lata(s) de 18 litros a um custo de R$ {custo_lata}. Vão sobrar {float(sobra_latas)} litro(s) de tinta.")
    print(f"Você pode comprar {ceil(galoes)} lata(s) de 3.6 litros a um custo de R$ {custo_galoes}. Vão sobrar {sobra_galoes:.1f} litro(s) de tinta.")
    print(f"Para menor custo, você pode comprar {round(lata_melhor_custo)} lata(s) de 18 litros e {ceil(galao_melhor_custo)} galão(ões) de 3.6 litros a um custo de R$ {melhor_custo}. Vão sobrar {sobra_tintas:.1f} litro(s) de tinta.")
