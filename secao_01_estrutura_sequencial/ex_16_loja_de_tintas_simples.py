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
    """Escreva aqui em baixo a sua solução"""
    import math
    area = float(input('Digite o tamanho da área a ser pintada em m²: '))
    litros_por_metro = 3
    litros_necessarios = area / litros_por_metro
    litros_por_lata = 18
    numero_de_latas = math.ceil((litros_necessarios / litros_por_lata))
    valor_em_latas = numero_de_latas * 80
    print(f'Você deve comprar {numero_de_latas:.0f} lata(s) tinta ao custo de R$ {valor_em_latas:.2f}')