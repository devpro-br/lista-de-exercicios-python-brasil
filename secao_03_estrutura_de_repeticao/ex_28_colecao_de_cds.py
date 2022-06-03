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
from statistics import mean


def calcular_estatisticas_colecao_de_cd():
    """Escreva aqui em baixo a sua solução"""
    numero_de_cds = int(input('Digite o número de cds: '))
    custos_por_cd = []
    print(f'Número de cds: {numero_de_cds}')
    while len(custos_por_cd) < numero_de_cds:
        cd_atual = len(custos_por_cd) + 1
        custo_cd_atual = float(input(f'Digite quantos custou o cd {cd_atual}: '))
        if 0 > custo_cd_atual:
            print(f'O cd deve ter um custo positivo, não pode ser {custo_cd_atual}')
        else:
            custos_por_cd.append(custo_cd_atual)

    media_de_custo_por_cd = mean(custos_por_cd)
    custo_total_colecao = sum(custos_por_cd)

    print(f'Valor total da coleção: R$ {custo_total_colecao:.2f}')
    print(f'Custo médio dos cds: R$ {media_de_custo_por_cd:.2f}')
