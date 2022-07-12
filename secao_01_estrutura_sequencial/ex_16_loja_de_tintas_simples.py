"""
Exercício 16 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

    >>> from secao_01_estrutura_sequencial import ex_16_loja_de_tintas_simples
    >>> ex_16_loja_de_tintas_simples.input = lambda k: '50'
    >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
    Você deve comprar 1 lata(s) tinta ao custo de R$ 80.00
    >>> ex_16_loja_de_tintas_simples.input = lambda k: '100'
    >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
    Você deve comprar 2 lata(s) tinta ao custo de R$ 160.00


"""


def calcular_latas_e_preco_de_tinta():
    import math
    rendimento = 3 # cada litro cobre 3 m²

    while True:

         try:

              area_pintar = float(input('Informe a área a pintar em m²: '))
              area_cobertura_lata = 18 * rendimento
              quant_latas = math.ceil(area_pintar / area_cobertura_lata)
              valor_pagar = quant_latas * 80
              #print(f'Para cobrir {area_pintar}m² ==>   {quant_latas} latas x R$ 80,00 = {valor_pagar}')
              print(f'Você deve comprar {quant_latas} lata(s) tinta ao custo de R$ {valor_pagar:.2f}')
              break
         except ValueError:

             print('Valor inválido!!!')


