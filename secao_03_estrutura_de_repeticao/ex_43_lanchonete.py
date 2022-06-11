"""
Exercício 43 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que receba os itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido e quantidade de itens
comprados.


    >>> fechar_conta()
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          0 |       0.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          1 |       1.20 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          1 |       1.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          3 |       3.60 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          5 |       6.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          8 |      10.70 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         12 |      15.50 |
    -----------------------------------------------------------------------------

    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('104', 5))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Cheeseburger     | 104    | 1.30                |          5 |       6.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         17 |      22.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('105', 6))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Refrigerante     | 105    | 1.00                |          6 |       6.00 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         18 |      21.50 |
    -----------------------------------------------------------------------------

"""
def fechar_conta(*itens):
    """Escreva aqui em baixo a sua solução"""
    print('_____________________________________________________________________________')
    print('|                              RESUMO DA CONTA                              |')
    print('|---------------------------------------------------------------------------|')
    print('| Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |')
    qtd_cachorro_quente = 0
    qtd_bauru_simples = 0
    qtd_bauru_com_ovo = 0
    qtd_hamburger = 0
    qtd_cheeseburger = 0
    qtd_refrigerante = 0
    preco_cachorro_quente = 1.20
    preco_bauru_simples = 1.30
    preco_bauru_com_ovo = 1.50
    preco_hamburger = 1.20
    preco_cheeseburger = 1.30
    preco_refrigerante = 1.00
    for codigo, quantidade in itens:
        if codigo == '100':
            qtd_cachorro_quente+= quantidade
        if codigo == '101':
            qtd_bauru_simples+= quantidade
        if codigo == '102':
            qtd_bauru_com_ovo+= quantidade
        if codigo == '103':
            qtd_hamburger+= quantidade
        if codigo == '104':
            qtd_cheeseburger+= quantidade
        if codigo == '105':
            qtd_refrigerante+= quantidade
    preco_cachorro_quente*= qtd_cachorro_quente
    preco_bauru_simples*= qtd_bauru_simples
    preco_bauru_com_ovo*= qtd_bauru_com_ovo
    preco_hamburger*= qtd_hamburger
    preco_cheeseburger*= qtd_cheeseburger
    preco_refrigerante*=qtd_refrigerante
    if qtd_cachorro_quente > 0:
        print(f'| Cachorro Quente  | 100    | 1.20                |          {qtd_cachorro_quente} |       {preco_cachorro_quente:.2f} |')
    if qtd_bauru_simples > 0:
        print(f'| Bauru Simples    | 101    | 1.30                |          {qtd_bauru_simples} |       {preco_bauru_simples:.2f} |')
    if qtd_bauru_com_ovo > 0:
        print(f'| Bauru com Ovo    | 102    | 1.50                |          {qtd_bauru_com_ovo} |       {preco_bauru_com_ovo:.2f} |')
    if qtd_hamburger > 0:
        print(f'| Hamburger        | 103    | 1.20                |          {qtd_hamburger} |       {preco_hamburger:.2f} |')
    if qtd_cheeseburger > 0:
        print(f'| Cheeseburger     | 104    | 1.30                |          {qtd_cheeseburger} |       {preco_cheeseburger:.2f} |')
    if qtd_refrigerante > 0:
       print(f'| Refrigerante     | 105    | 1.00                |          {qtd_refrigerante} |       {preco_refrigerante:.2f} |') 
    quantidade_total = qtd_cachorro_quente+qtd_bauru_simples+qtd_bauru_com_ovo+qtd_hamburger+qtd_cheeseburger+qtd_refrigerante
    preco_total = preco_cachorro_quente+preco_bauru_simples+preco_bauru_com_ovo+preco_hamburger+preco_cheeseburger+preco_refrigerante
    print('|---------------------------------------------------------------------------|')
    if quantidade_total < 10 and preco_total < 10:
        print(f'| Total Geral:                                    |          {quantidade_total} |       {preco_total:.2f} |')
    elif quantidade_total < 10 and preco_total >=10:
        print(f'| Total Geral:                                    |          {quantidade_total} |      {preco_total:.2f} |')
    else:
        print(f'| Total Geral:                                    |         {quantidade_total} |      {preco_total:.2f} |')
    print('-----------------------------------------------------------------------------')