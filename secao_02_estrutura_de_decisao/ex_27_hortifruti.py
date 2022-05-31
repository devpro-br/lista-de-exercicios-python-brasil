"""
Exercício 27 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o
valor a ser pago pelo cliente.
Mostre o restultado com duas casas decimais

    >>> calcular_preco_da_compra(2, 0)
    (+)  Morango  - valor:  R$  5.00 - quantidade:  2 kg - preço: R$ 2.50/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  5.00
    >>> calcular_preco_da_compra(6, 0)
    (+)  Morango  - valor:  R$ 13.20 - quantidade:  6 kg - preço: R$ 2.20/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$ 13.20
    >>> calcular_preco_da_compra(9, 0)
    (+)  Morango  - valor:  R$ 19.80 - quantidade:  9 kg - preço: R$ 2.20/kg
    (-)  Desconto - valor:  R$  1.98
              Valor Total:  R$ 17.82
    >>> calcular_preco_da_compra(0, 2)
    (+)  Maça     - valor:  R$  3.60 - quantidade:  2 kg - preço: R$ 1.80/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  3.60
    >>> calcular_preco_da_compra(0, 6)
    (+)  Maça     - valor:  R$  9.00 - quantidade:  6 kg - preço: R$ 1.50/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  9.00
    >>> calcular_preco_da_compra(0, 9)
    (+)  Maça     - valor:  R$ 13.50 - quantidade:  9 kg - preço: R$ 1.50/kg
    (-)  Desconto - valor:  R$  1.35
              Valor Total:  R$ 12.15
    >>> calcular_preco_da_compra(2, 2)
    (+)  Morango  - valor:  R$  5.00 - quantidade:  2 kg - preço: R$ 2.50/kg
    (+)  Maça     - valor:  R$  3.60 - quantidade:  2 kg - preço: R$ 1.80/kg
    (-)  Desconto - valor:  R$  0.00
              Valor Total:  R$  8.60
    >>> calcular_preco_da_compra(7, 2)
    (+)  Morango  - valor:  R$ 15.40 - quantidade:  7 kg - preço: R$ 2.20/kg
    (+)  Maça     - valor:  R$  3.60 - quantidade:  2 kg - preço: R$ 1.80/kg
    (-)  Desconto - valor:  R$  1.90
              Valor Total:  R$ 17.10
    >>> calcular_preco_da_compra(7, 7)
    (+)  Morango  - valor:  R$ 15.40 - quantidade:  7 kg - preço: R$ 2.20/kg
    (+)  Maça     - valor:  R$ 10.50 - quantidade:  7 kg - preço: R$ 1.50/kg
    (-)  Desconto - valor:  R$  2.59
              Valor Total:  R$ 23.31

"""


from os import sep


def calcular_preco_da_compra(kilos_de_morango: int, kilos_de_maca: int):
    """Escreva aqui em baixo a sua solução"""    
    
    if kilos_de_maca <= 5:
        
        valor_maca = 1.8
    else:
        
        valor_maca = 1.5

    if kilos_de_morango <= 5:
        valor_morango = 2.5
    else:
        valor_morango = 2.2

    valor_total_morango = kilos_de_morango*valor_morango
    valor_total_maca = kilos_de_maca*valor_maca
    valor_total_frutas = (valor_total_maca)+(valor_total_morango)
    kilos_de_frutas = kilos_de_maca + kilos_de_morango    

    if kilos_de_frutas > 8 or valor_total_frutas > 25:
        desconto_em_porcentagem = 10
        desconto = desconto_em_porcentagem/100
        valor_de_desconto = valor_total_frutas*desconto
        valor_total_frutas = valor_total_frutas-valor_de_desconto
    else:
        desconto_em_porcentagem = 0
        desconto = desconto_em_porcentagem/100
        valor_de_desconto = valor_total_frutas*desconto
        valor_total_frutas = valor_total_frutas-valor_de_desconto
    

    #Auxilio print
    valor_total_morango = str('%.2f'%valor_total_morango)
    valor_total_maca = str('%.2f'%valor_total_maca)
    valor_morango = str('%.2f' %valor_morango)
    valor_maca = str('%.2f' %valor_maca)
    valor_de_desconto = str('%.2f'%valor_de_desconto)
    valor_total_frutas = str('%.2f'%valor_total_frutas)
    
    if kilos_de_morango > 0 and kilos_de_maca == 0:
        print('(+)  Morango  - valor:  R$', valor_total_morango.rjust(6,' '), ' - quantidade:', str(kilos_de_morango).rjust(3,' '), ' kg - preço: R$ ', valor_morango.rjust(3,' '),'/kg',sep='')
        print('(-)  Desconto - valor:  R$', valor_de_desconto.rjust(5,' '))
        print('          Valor Total:  R$', valor_total_frutas.rjust(5,' '))
    elif kilos_de_morango == 0 and kilos_de_maca > 0:
        print('(+)  Maça     - valor:  R$', valor_total_maca.rjust(6,' '), ' - quantidade:', str(kilos_de_maca).rjust(3,' '), ' kg - preço: R$ ', valor_maca.rjust(3,' '),'/kg',sep='')
        print('(-)  Desconto - valor:  R$', valor_de_desconto.rjust(5,' '))
        print('          Valor Total:  R$', valor_total_frutas.rjust(5,' '))
    else:
        print('(+)  Morango  - valor:  R$', valor_total_morango.rjust(6,' '), ' - quantidade:', str(kilos_de_morango).rjust(3,' '), ' kg - preço: R$ ', valor_morango.rjust(3,' '),'/kg',sep='')
        print('(+)  Maça     - valor:  R$', valor_total_maca.rjust(6,' '), ' - quantidade:', str(kilos_de_maca).rjust(3,' '), ' kg - preço: R$ ', valor_maca.rjust(3,' '),'/kg',sep='')
        print('(-)  Desconto - valor:  R$', valor_de_desconto.rjust(5,' '))
        print('          Valor Total:  R$', valor_total_frutas.rjust(5,' '))