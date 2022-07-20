"""
Exercício 18 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

    >>> calcular_estatisticas()
    'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    >>> calcular_estatisticas(1)
    'Maior valor: 1. Menor valor: 1. Soma: 1'
    >>> calcular_estatisticas(1, 2)
    'Maior valor: 2. Menor valor: 1. Soma: 3'
    >>> calcular_estatisticas(1, 2, -1)
    'Maior valor: 2. Menor valor: -1. Soma: 2'

"""


def calcular_estatisticas(*numeros) -> str:
    """Escreva aqui em baixo a sua solução"""
    if len(numeros) == 0:
        print("'Maior valor: não existe. Menor valor: não existe. Soma: 0'")
        return
    maior = max(numeros)
    menor = min(numeros)
    soma = 0

    for n in numeros: 
        soma +=n
    print(f"'Maior valor: {maior}. Menor valor: {menor}. Soma: {soma}'")
        