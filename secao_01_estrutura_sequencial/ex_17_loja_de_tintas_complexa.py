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
    area = float(input("Insira a area em metros quadrados"))
    litro_tinta = 6               #1 litro rende 6 metros²
    litros_necessarios = (area / litro_tinta)*1.10
    preco_lata = 80.00
    lata = 18  # 18 litros
    latas_necessarias = math.ceil(litros_necessarios / lata )   # quantidade de latas necessarias
    litro_por_preco = (preco_lata * latas_necessarias) # preco do litro de tinta
    sobra = math.floor(latas_necessarias * lata - litros_necessarios )   #sobra de tinta

    #area = float(input("Insira a area em metros quadrados"))
    galao_tinta =6               # 3.6 litros
    litros_galao = 3.6
    preco_galao = 25.00
    litros_necessarios_galao = math.ceil(area / galao_tinta*1.10)
    galoes_necessarios = math.ceil(litros_necessarios_galao / litros_galao) #quantidade de galoes necessarios
    litro_preco_galao = math.ceil(preco_galao * galoes_necessarios)
    sobra_galoes = (galoes_necessarios * litros_galao - litros_necessarios_galao )
    #inicio terceira parte

    lata = 18
    litros_galao = 3.6
    litros_necessarios = math.ceil((area / litro_tinta) *1.10)
    qnt_latas = math.floor(litros_necessarios / lata)
    subtracao = litros_necessarios - (lata *qnt_latas )     # qnt de litros ainda necessario
    qntd_galoes = math.ceil(subtracao / litros_galao)       # qnts galoes de 3,6 litros ainda precisa
    preco = (qnt_latas * 80 ) + (qntd_galoes * 25)
    sobra3 = ( (qnt_latas * lata) + (qntd_galoes * litros_galao) - litros_necessarios)


    print (f"Você deve comprar {math.ceil(litros_necessarios)} litros de tinta.")
    print (f"Você pode comprar {math.ceil(latas_necessarias)} lata(s) de 18 litros a um custo de R$ {litro_por_preco :.0f}. Vão sobrar {sobra  :.1f} litro(s) de tinta.")
    print(f"Você pode comprar {galoes_necessarios} lata(s) de 3.6 litros a um custo de R$ {litro_preco_galao :.0f}. Vão sobrar {sobra_galoes :.1f} litro(s) de tinta.")
    print (f"Para menor custo, você pode comprar {qnt_latas} lata(s) de 18 litros e {qntd_galoes} galão(ões) de 3.6 litros a um custo de R$ {preco}. Vão sobrar {sobra3 :.1f} litro(s) de tinta.")
