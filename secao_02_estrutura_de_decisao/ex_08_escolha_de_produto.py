"""
Exercício 08 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão
é sempre pelo mais barato.
Mostrar o resultado com duas casas decimais

    >>> decidir_melhor_produto(2, 3, 5)
    Melhor produto custa R$ 2.00
    >>> decidir_melhor_produto(10, 5.55, 7)
    Melhor produto custa R$ 5.55
    >>> decidir_melhor_produto(20, 30, 17.62)
    Melhor produto custa R$ 17.62
    >>> decidir_melhor_produto(7, 1, 15)
    Melhor produto custa R$ 1.00

"""


def decidir_melhor_produto(x, y, z):
    while True:
        try:
            preco_prod_01 = float(input('Entre com o valor do produto 01: '))
            preco_prod_02 = float(input('Entre com o valor do produto 02: '))
            preco_prod_03 = float(input('Entre com o valor do produto 03: '))
            
        except ValueError:
            
            print('Entrada inválida!!!')
            break
        
        if preco_prod_01 <= preco_prod_02:
            menor_preco = preco_prod_01
            
        if preco_prod_01 >= preco_prod_02:
            menor_preco = preco_prod_02
        
        if menor_preco > preco_prod_03:
            menor_preco = preco_prod_03
            
        
        print(f'Melhor produto custa R$ {menor_preco:,.2f}')
