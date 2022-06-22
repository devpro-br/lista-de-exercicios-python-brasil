"""
xercício 12 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante

    >>> salarios_nos_intervalos([3000])
    [0, 0, 1, 0, 0, 0, 0, 0, 0]
    >>> salarios_nos_intervalos([3000, 6000, 6001, 600000000])
    [0, 0, 1, 0, 0, 2, 0, 0, 1]
    >>> salarios_nos_intervalos([2000, 20000, 4500, 1500, 3200])
    [0, 2, 1, 0, 1, 0, 0, 0, 1]
    >>> salarios_nos_intervalos([1000, 4000, 5000, 7000, 8000])
    [1, 0, 0, 1, 1, 0, 1, 1, 0]
"""

def salarios_nos_intervalos(n):
    """Escreva aqui em baixo a sua solução"""
    