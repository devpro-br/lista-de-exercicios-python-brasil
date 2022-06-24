"""
Exercício 05 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosFuncoes

Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

    >>> somaImposto(20, 55)
    66
    >>> somaImposto(30.5, 95.7)
    125
    >>> somaImposto(-10, 90)
    A taxa de Imposto não pode ser negativa
    >>> somaImposto(10, -90)
    O custo não pode ser negativo
"""

def somaImposto(taxaImposto, custo):
    """escreva aqui em baixo sua solução"""
    
    print(somaAlterada(taxaImposto, custo))

