"""
Exercício 04 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento.

    >>> calcular_ano_ultrapassagem_populacional()
    'População de A, depois de 63 ano(s) será de 515033 pessoas, superando a de B, que será de 510964 pessoas'


"""
from itertools import count


def calcular_ano_ultrapassagem_populacional() -> str:
    """Escreva aqui em baixo a sua solução"""
    populacao_menor = 80_000
    taxa_crescimento_populacao_menor = 0.03
    populacao_maior = 200_000
    taxa_crescimento_populacao_maior = 0.015
    for ano in count(0):
        if int(populacao_menor) > int(populacao_maior):
            break
        populacao_maior *= (1 + taxa_crescimento_populacao_maior)
        populacao_menor *= (1 + taxa_crescimento_populacao_menor)
    populacao_menor = int(populacao_menor)
    populacao_maior = int(populacao_maior)
    return (
        f'População de A, depois de {ano} ano(s) será de {populacao_menor} pessoas, superando a de B, que será de'
        f' {populacao_maior} pessoas'
    )
