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
    area_pintada = float(input("Coloque o valor da area em m² aqui: "))
    valor_lata = float(80)
    lata = int(0)
    if area_pintada < 54:
        print(f"Você deve comprar {lata + 1} lata(s) tinta ao custo de R$ {valor_lata:.2f}")
    elif (area_pintada > 50) and (area_pintada <= 108):
        print(f"Você deve comprar {lata + 2} lata(s) tinta ao custo de R$ {valor_lata*2:.2f}")
