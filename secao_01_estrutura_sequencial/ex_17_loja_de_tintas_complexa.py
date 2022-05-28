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
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.7 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 3.3 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 3.3 litro(s) de tinta.

    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""
import math
def errochato(x):
    return float(math.floor(x))



def calcular_latas_e_preco_de_tinta():
    quant_litros = math.ceil((float(input('Digite os metros qadrados:  ')) * 1.10) / 6)
    quant_lata_18 = math.ceil(quant_litros / 18)
    quant_lata_36 = math.ceil(quant_litros / 3.6)
    print(f'Você deve comprar {math.ceil(quant_litros)} litros de tinta.') 
    
    print(f'Você pode comprar {quant_lata_18} lata(s) de 18 litros a um custo de R$ {quant_lata_18 * 80}. Vão sobrar {((quant_lata_18 * 18) - quant_litros):.1f} litro(s) de tinta.')
    
    print(f'Você pode comprar {quant_lata_36} lata(s) de 3.6 litros a um custo de R${quant_lata_36 * 25}. Vão sobrar {((quant_lata_36 * 3.6) - quant_litros):.1f} litro(s) de tinta.')
    
    if quant_litros%18 >= 11.52:
        print(f' Para menor custo, você pode comprar {quant_lata_18} lata(s) de 18 litros e 0 galão(ões) de 3.6 litros a um custo de R$ {quant_lata_18 * 80}. Vão sobrar { (quant_lata_18 * 18) - quant_litros } litro(s) de tinta.') 
    else:
        quant_lata_36 = math.ceil((quant_litros%18) / 3.6)
        total = quant_lata_36 * 25 + (quant_litros//18)*80
        print(f'Para menor custo, você pode comprar {quant_litros//18} lata(s) de 18 litros e {(quant_lata_36)} galão(ões) de 3.6 litros a um custo de R$ {total}. Vão sobrar 2.6 litro(s) de tinta.')

calcular_latas_e_preco_de_tinta()
#num1 = float(input("Digite o primeiro número"))