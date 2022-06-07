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


def calcular_preco_da_compra(kilos_de_morango: int, kilos_de_maca: int):
    """Escreva aqui em baixo a sua solução"""
    frutas_peso = kilos_de_maca + kilos_de_morango


    if kilos_de_maca <= 5:
        preco_maca = 1.8
    else: preco_maca = 1.5

    total_maca = preco_maca * kilos_de_maca

    if kilos_de_morango <= 5:
        preco_morango= 2.5
    else: preco_morango = 2.2

    total_morango = preco_morango * kilos_de_morango

    total = total_morango + total_maca

    if frutas_peso > 8 or total > 25:
        desconto = total * 0.1
        valor_total = total - desconto
    else:
        desconto = 0
        valor_total = total - desconto

    if kilos_de_morango > 0 and kilos_de_maca > 0:
        morango_str = '(+)  Morango '
        total_morango_str = str(round((kilos_de_morango * preco_morango), 2))
        print(f'{morango_str} {" " * (13 - len(morango_str))}- valor:{" " * 2}R${kilos_de_morango * preco_morango:>6.2f} - quantidade:  {kilos_de_morango} kg - preço: R$ {preco_morango:.2f}/kg')
        maca_str = '(+)  Maça '
        total_maca_str = str(round((kilos_de_maca * preco_maca), 2))
        print(f'{maca_str} {" " * (13 - len(maca_str))}- valor:{" " * 2}R${kilos_de_maca * preco_maca:>6.2f} - quantidade:  {kilos_de_maca} kg - preço: R$ {preco_maca:.2f}/kg')
        desconto_str = str(round((desconto), 2))
        print(f'(-)  Desconto - valor:{" " * 2}R${desconto:>6.2f}')
        valor_total_nome_str = 'Valor Total:'
        valor_total_str = str(round((valor_total), 2))
        print(f'{" " * 10}{valor_total_nome_str}{" " * 2}R${valor_total:>6.2f}')

    elif kilos_de_morango > 0 and kilos_de_maca == 0:
        morango_str = '(+)  Morango '
        total_morango_str = str(round((kilos_de_morango * preco_morango), 2))
        print(f'{morango_str} {" " * (13 - len(morango_str))}- valor:{" " * 2}R${kilos_de_morango * preco_morango:>6.2f} - quantidade:  {kilos_de_morango} kg - preço: R$ {preco_morango:.2f}/kg')
        desconto_str = str(round((desconto), 2))
        print(f'(-)  Desconto - valor:{" " * 2}R${desconto:>6.2f}')
        valor_total_nome_str = 'Valor Total:'
        valor_total_str = str(round((valor_total), 2))
        print(f'{" " * 10}{valor_total_nome_str}{" " * 2}R${valor_total:>6.2f}')

    elif kilos_de_morango == 0 and kilos_de_maca > 0:
         maca_str = '(+)  Maça '
         total_maca_str = str(round((kilos_de_maca * preco_maca), 2))
         print(f'{maca_str} {" " * (13 - len(maca_str))}- valor:{" " * 2}R${kilos_de_maca * preco_maca:>6.2f} - quantidade:  {kilos_de_maca} kg - preço: R$ {preco_maca:.2f}/kg')
         desconto_str = str(round((desconto), 2))
         print(f'(-)  Desconto - valor:{" " * 2}R${desconto:>6.2f}')
         valor_total_nome_str = 'Valor Total:'
         valor_total_str = str(round((valor_total), 2))
         print(f'{" " * 10}{valor_total_nome_str}{" " * 2}R${valor_total:>6.2f}')
    
