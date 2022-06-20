"""
Exercício 16 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o
 valor seja maior que 500.

    >>> calcular_serie_de_fibonacci_ate_valor_ser_maior_que_500()
    '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610'
"""


from turtle import pen


def calcular_serie_de_fibonacci_ate_valor_ser_maior_que_500() -> str:
    """Escreva aqui em baixo a sua solução"""
    ultimo = 0
    penultimo = 1
    soma = 1

    while ultimo <= 500:
        if ultimo == 0:
            print(f"'{ultimo}", end=", ")
        if penultimo > 500:
            print(f"{penultimo}'", end="")
            return
        else:
            print(f"{soma}", end=", ")
            soma = ultimo + penultimo
            ultimo = penultimo
            penultimo = soma
        