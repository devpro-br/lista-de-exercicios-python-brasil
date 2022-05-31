"""
Exercício 26 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o
preço do litro do álcool é R$ 1,90.

Mostre o restultado com duas casas decimais

    >>> calcular_abastecimento(10, 'A')
    '10 litro(s) de álcool custa(m): R$ 19.00. Com 3% de desconto, fica R$ 18.43'
    >>> calcular_abastecimento(20, 'A')
    '20 litro(s) de álcool custa(m): R$ 38.00. Com 3% de desconto, fica R$ 36.86'
    >>> calcular_abastecimento(30, 'A')
    '30 litro(s) de álcool custa(m): R$ 57.00. Com 5% de desconto, fica R$ 54.15'
    >>> calcular_abastecimento(10, 'G')
    '10 litro(s) de gasolina custa(m): R$ 25.00. Com 4% de desconto, fica R$ 24.00'
    >>> calcular_abastecimento(20, 'G')
    '20 litro(s) de gasolina custa(m): R$ 50.00. Com 4% de desconto, fica R$ 48.00'
    >>> calcular_abastecimento(30, 'G')
    '30 litro(s) de gasolina custa(m): R$ 75.00. Com 6% de desconto, fica R$ 70.50'

"""


def calcular_abastecimento(litros_de_combustivel: float, tipo_de_combustivel: str) -> str:
    """Escreva aqui em baixo a sua solução"""
    if tipo_de_combustivel == 'A':
        tipo_de_combustivel = 'álcool'
        valor_combustivel = 1.9
    elif tipo_de_combustivel == 'G':
        tipo_de_combustivel = 'gasolina'
        valor_combustivel = 2.5


    if litros_de_combustivel <= 20 and tipo_de_combustivel == 'álcool':
        desconto_em_porcentagem = 3
        desconto = desconto_em_porcentagem/100
        valor_total = (valor_combustivel*litros_de_combustivel)
        valor_desconto = valor_total-(valor_total*desconto)
    elif litros_de_combustivel > 20 and tipo_de_combustivel == 'álcool':
        desconto_em_porcentagem = 5
        desconto = desconto_em_porcentagem/100
        valor_total = (valor_combustivel*litros_de_combustivel)
        valor_desconto = valor_total-(valor_total*desconto)
    elif litros_de_combustivel <= 20 and tipo_de_combustivel == 'gasolina':
        desconto_em_porcentagem = 4
        desconto = desconto_em_porcentagem/100
        valor_total = (valor_combustivel*litros_de_combustivel)
        valor_desconto = valor_total-(valor_total*desconto)
    elif litros_de_combustivel > 20 and tipo_de_combustivel == 'gasolina':
        desconto_em_porcentagem = 6
        desconto = desconto_em_porcentagem/100
        valor_total = (valor_combustivel*litros_de_combustivel)
        valor_desconto = valor_total-(valor_total*desconto)

    #Formatação para str do return
    valor_total = str('%.2f'%valor_total)
    valor_desconto = str('%.2f'%valor_desconto)
    return str(litros_de_combustivel) + ' litro(s) de ' + str(tipo_de_combustivel) + ' custa(m): R$ ' + str(valor_total) + '. Com ' + str(desconto_em_porcentagem) + '% de desconto, fica R$ ' + str(valor_desconto) 
    


    
