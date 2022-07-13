"""
Exercício 28 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar.

Mostre o restultado com duas casas decimais

    >>> calcular_preco_da_carne('Filé Duplo', 2, 'dinheiro')
    '2 kg de Filé Duplo a R$ 4.90/kg saem a R$ 9.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Filé Duplo', 4, 'cartão tabajara')
    '4 kg de Filé Duplo a R$ 4.90/kg saem a R$ 19.60. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 18.62'
    >>> calcular_preco_da_carne('Filé Duplo', 6, 'pix')
    '6 kg de Filé Duplo a R$ 5.80/kg saem a R$ 34.80. Não há desconto, pagamento feito com pix'
    >>> calcular_preco_da_carne('Filé Duplo', 8, 'cartão tabajara')
    '8 kg de Filé Duplo a R$ 5.80/kg saem a R$ 46.40. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 44.08'
    >>> calcular_preco_da_carne('Alcatra', 2, 'dinheiro')
    '2 kg de Alcatra a R$ 5.90/kg saem a R$ 11.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Alcatra', 4, 'cartão tabajara')
    '4 kg de Alcatra a R$ 5.90/kg saem a R$ 23.60. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 22.42'
    >>> calcular_preco_da_carne('Alcatra', 6, 'dinheiro')
    '6 kg de Alcatra a R$ 6.80/kg saem a R$ 40.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Alcatra', 8, 'cartão tabajara')
    '8 kg de Alcatra a R$ 6.80/kg saem a R$ 54.40. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 51.68'
    >>> calcular_preco_da_carne('Picanha', 2, 'dinheiro')
    '2 kg de Picanha a R$ 6.90/kg saem a R$ 13.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Picanha', 4, 'cartão tabajara')
    '4 kg de Picanha a R$ 6.90/kg saem a R$ 27.60. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 26.22'
    >>> calcular_preco_da_carne('Picanha', 6, 'dinheiro')
    '6 kg de Picanha a R$ 7.80/kg saem a R$ 46.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Picanha', 8, 'cartão tabajara')
    '8 kg de Picanha a R$ 7.80/kg saem a R$ 62.40. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 59.28'
    
"""


def calcular_preco_da_carne(tipo_de_carne: str, kilos_de_carne: int, forma_de_pagamento: str) -> str:
    while True:
        try:
            forma_pagamento = 'cartão'
            desconto_percentual = .05
            carne = ''
            modo_pag = ''

            print('Digite (f) para Filé duplo, (a) para Alcatra ou (p) para Picanha: ', end = '')
            
            while carne != 'f' and carne != 'a' and carne != 'p': 
                carne = input().lower()
              
            if carne == 'f':
                tipo_carne = "Filé Duplo"

            if carne == 'a':
                tipo_carne = "Alcatra"
        
            if carne == 'p':
                tipo_carne = "Picanha"


            quantidade = int(input('Quantos kilos?: '))

            print('Forma de pagamento: (d) Dinheiro  (c) Cartão (p) pix: ', end = '')
            
            while modo_pag != 'd' and modo_pag != 'c' and modo_pag != 'p':
                modo_pag = input().lower()
            
            if modo_pag == 'd':
                forma_pagamento = "dinheiro"
            if modo_pag == 'p':
                forma_pagamento = "pix"

            

            if quantidade > 5:

                preco_file = 5.80
                preco_Alcatra = 6.80
                preco_Picanha = 7.80
                if carne == "f": 
                    preco_carne = preco_file
                elif carne == "a":
                    preco_carne = preco_Alcatra
                elif carne == "p":
                    preco_carne = preco_Picanha
            else:

                preco_file = 4.90
                preco_Alcatra = 5.90
                preco_Picanha = 6.90
                
                if carne == "f": 
                    preco_carne = preco_file
                elif carne == "a":
                    preco_carne = preco_Alcatra
                elif carne == "p":
                    preco_carne = preco_Picanha


            valor_compra = quantidade * preco_carne

            if forma_pagamento == "dinheiro" or forma_pagamento == 'pix':
                print(f"'{quantidade} kg de {tipo_carne} a R$ {preco_carne:.2f}/kg saem a R$ {valor_compra:.2f}. Não há desconto, pagamento feito com {forma_pagamento}'")
            
            else: 
                
                valor_com_desconto = valor_compra - (valor_compra * desconto_percentual)
                print(f"'{quantidade} kg de {tipo_carne} a R$ {preco_carne:.2f}/kg saem a R$ {valor_compra:.2f}. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ {valor_com_desconto:.2f}'")    

            break

        except ValueError:
            break    
