"""
Exercício 33 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

Mostre a média com uma casa decimal.

    >>> calcular_estatisticas()
    'Maior temperatura: não existe. Menor temperatura: não existe. Média: não existe'
    >>> calcular_estatisticas(1)
    'Maior temperatura: 1. Menor temperatura: 1. Média: 1.0'
    >>> calcular_estatisticas(1, 2)
    'Maior temperatura: 2. Menor temperatura: 1. Média: 1.5'
    >>> calcular_estatisticas(1, 2, -1)
    'Maior temperatura: 2. Menor temperatura: -1. Média: 0.7'


"""


def calcular_estatisticas(*temperaturas) -> str:
    """Escreva aqui em baixo a sua solução"""
    maior_temperatura = 'não existe'
    menor_temperatura = 'não existe'
    soma = 0
    for n in temperaturas:
        if maior_temperatura == 'não existe':
            menor_temperatura = maior_temperatura = n

        if maior_temperatura < n:
            maior_temperatura = n

        if menor_temperatura > n:
            menor_temperatura = n

        soma += n

    n_lidas = len(temperaturas)
    if n_lidas == 0:
        media = 'não existe'
    else:
        media = soma / n_lidas
        media=f'{media:.1f}'
    return f'Maior temperatura: {maior_temperatura}. Menor temperatura: {menor_temperatura}. Média: {media}'
