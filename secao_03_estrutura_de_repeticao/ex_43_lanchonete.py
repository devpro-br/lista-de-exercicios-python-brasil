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
    contador = 0
    total_cachorro = 0
    quantidade_cachorro = 0        
    total_bauro_simples = 0
    quantidade_bauro_simples = 0
    total_bauro_ovo = 0
    quantidade_bauro_ovo = 0
    total_hamburger = 0
    quantidade_hamburger = 0
    total_x_burger = 0
    quantidade_x_burger = 0
    total_refri = 0
    quantidade_refri = 0
    if len(itens) > 0:
        codigo, unidades = zip(*itens)
        quantidade_itens = len(unidades)        
        print('_____________________________________________________________________________')
        print('|                              RESUMO DA CONTA                              |')
        print('|---------------------------------------------------------------------------|')
        print('| Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |')
        while len(unidades) > contador:
            if codigo[contador] == '100':
                total_cachorro = (unidades[contador]*1.20) + total_cachorro
                quantidade_cachorro = unidades[contador]+quantidade_cachorro
                contador += 1
            elif codigo[contador] == '101':
                total_bauro_simples = (unidades[contador]*1.30) + total_bauro_simples
                quantidade_bauro_simples = unidades[contador]+quantidade_bauro_simples
                contador += 1
            elif codigo[contador] == '102':
                total_bauro_ovo = (unidades[contador]*1.50) + total_bauro_ovo
                quantidade_bauro_ovo = unidades[contador]+quantidade_bauro_ovo
                contador += 1
            elif codigo[contador] == '103':
                total_hamburger = (unidades[contador]*1.20) + total_hamburger
                quantidade_hamburger = unidades[contador]+quantidade_hamburger
                contador += 1
            elif codigo[contador] == '104':
                total_x_burger = (unidades[contador]*1.30) + total_x_burger
                quantidade_x_burger = unidades[contador]+quantidade_x_burger
                contador += 1
            elif codigo[contador] == '105':
                total_refri = (unidades[contador]*1.00) + total_refri
                quantidade_refri = unidades[contador]+quantidade_refri
                contador += 1
            else:
                contador += 1
        
        if total_cachorro > 0:
            print('| Cachorro Quente  | 100    | 1.20                |          %.0f |       %.2f |'%(quantidade_cachorro,total_cachorro)) 
        if total_bauro_simples > 0:
            print('| Bauru Simples    | 101    | 1.30                |          %.0f |       %.2f |'%(quantidade_bauro_simples,total_bauro_simples))
        if total_bauro_ovo:
            print('| Bauru com Ovo    | 102    | 1.50                |          %.0f |       %.2f |'%(quantidade_bauro_ovo,total_bauro_ovo))
        if total_hamburger:
            print('| Hamburger        | 103    | 1.20                |          %.0f |       %.2f |'%(quantidade_hamburger,total_hamburger))
        if total_x_burger:
            print('| Cheeseburger     | 104    | 1.30                |          %.0f |       %.2f |'%(quantidade_x_burger,total_x_burger))
        if total_refri:
            print('| Refrigerante     | 105    | 1.00                |          %.0f |       %.2f |'%(quantidade_refri,total_refri))

        total_geral = total_x_burger+total_cachorro+total_bauro_ovo+total_bauro_simples+total_hamburger+total_refri
        total_itens = quantidade_bauro_ovo+quantidade_bauro_simples+quantidade_cachorro+quantidade_hamburger+quantidade_refri+quantidade_x_burger
        if total_itens > 9:
            print('|---------------------------------------------------------------------------|')
            print('| Total Geral:                                    |         %.0f |      %.2f |'%(total_itens,total_geral))
            print('-----------------------------------------------------------------------------')
        else:
            print('|---------------------------------------------------------------------------|')
            print('| Total Geral:                                    |          %.0f |      %5.2f |'%(total_itens,total_geral))
            print('-----------------------------------------------------------------------------')
    else:
        print('_____________________________________________________________________________')
        print('|                              RESUMO DA CONTA                              |')
        print('|---------------------------------------------------------------------------|')
        print('| Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |')
        print('|---------------------------------------------------------------------------|')
        print('| Total Geral:                                    |          0 |       0.00 |')
        print('-----------------------------------------------------------------------------')

    
    