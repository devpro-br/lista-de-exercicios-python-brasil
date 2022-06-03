"""
Exercício 28 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em
cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

Mostre os valores monetórios com duas casas decimais..

    >>> from secao_03_estrutura_de_repeticao import ex_28_colecao_de_cds
    >>> entradas = ['1', '1']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 1
    Valor total da coleção: R$ 1.00
    Custo médio dos cds: R$ 1.00
    >>> entradas = ['40', '40', '2']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 2
    Valor total da coleção: R$ 80.00
    Custo médio dos cds: R$ 40.00
    >>> entradas = ['10', '20', '30', '40', '4']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 4
    Valor total da coleção: R$ 100.00
    Custo médio dos cds: R$ 25.00
    >>> entradas = ['10', '20', '30', '3']
    >>> ex_28_colecao_de_cds.input = lambda k: entradas.pop()
    >>> ex_28_colecao_de_cds.calcular_estatisticas_colecao_de_cd()
    Número de cds: 3
    Valor total da coleção: R$ 60.00
    Custo médio dos cds: R$ 20.00

"""


def calcular_estatisticas_colecao_de_cd():
    """Escreva aqui em baixo a sua solução"""
    entradas = []
    entradas.append(int(input('Insira o número de CD(s): ')))
    contador = 0
    soma_cd = 0
    numero_cd = entradas[0]
    cd_teste = 0   
    print('Número de cds: %.0f'% numero_cd)
    while contador < len(entradas):
        entradas.insert(0, int(input('Insira o valor do CD: ')))
        contador = contador + 1
        if entradas[0] <= 0:
            print('O valor do CD precisa ser maior que 0, não pode ser: %.0f '%entradas[0])
        else:            
            soma_cd = soma_cd + entradas[0]     
            cd_teste = cd_teste + 1
        if cd_teste == numero_cd:
            media = soma_cd/entradas[len(entradas)-1]            
            contador = contador + 1
    else:
        print('Valor total da coleção: R$ %.2f'% soma_cd)
        print('Custo médio dos cds: R$ %.2f'% media)
