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


def calcular_latas_e_preco_de_tinta(area_pintar):
    #Parametros
    import math

    rendimento = 6
    valor_lata = 80
    valor_galao = 25


    #area_pintar = float(input('Qual área a pintar em m²? '))
    litros = math.ceil((area_pintar/rendimento) * 1.1)
    lata = math.ceil(litros/18)
    valor_lata = lata * 80
    sobra = (lata * 18) - litros
    retorno_latas = f'Você pode comprar {lata} lata(s) de 18 litros a um custo de R$ '\
                    f'{valor_lata}. Vão sobrar {sobra:.1f} litro(s) de tinta.'



    galao = math.ceil(litros /3.6)
    valor_galao = galao * 25
    sobra = (galao * 3.6) - litros
    retorno_galao =  f'Você pode comprar {galao} lata(s) de 3.6 litros a um custo de R$ '\
                     f'{valor_galao}. Vão sobrar {sobra:.1f} litro(s) de tinta.'



    lata_18 = litros//18
    lata18 = (litros /18)
    lata18_valor = lata_18 * 80
    diferença = lata18 - (litros //18)
    diferença = diferença * 18
    diferença = math.ceil(diferença/3.6)

    galao_completa_latas = diferença

    if diferença > 0 and diferença <=  3.6:
        galao_completa_latas= 1
    else:
        galao_completa_latas  =  math.ceil(galao_completa_latas/3.6)
    valor_mescla_lata_galao = (lata18_valor) + (galao_completa_latas * 25)

    sobra = ((lata_18 * 18) + (galao_completa_latas * 3.6)) - litros
    retorno_lata_galao = f'Para menor custo, você pode comprar {lata_18} lata(s) de 18 litros e {galao_completa_latas} galão(ões) '\
                         f'de 3.6 litros a um custo de R$ {valor_mescla_lata_galao}. Vão sobrar {sobra:.1f} litro(s) de tinta.'


    print(f'Você deve comprar {litros:.2f} litros de tinta.')


    print(retorno_latas)
    print(retorno_galao)
    print(retorno_lata_galao)

    
