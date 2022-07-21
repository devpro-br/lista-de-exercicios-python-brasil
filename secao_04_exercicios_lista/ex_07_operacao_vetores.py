""" 
Exercício 07 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

    >>> ler_cinco_inteiros([1, 1, 1, 1, 1])
    Soma = 5
    Multiplicação = 1
    1, 1, 1, 1, 1
    >>> ler_cinco_inteiros([2, 7, 6, 8, 15])
    Soma = 38
    Multiplicação = 10080
    2, 7, 6, 8, 15
    >>> ler_cinco_inteiros([4, 0, 5, 10, 9])
    Soma = 28
    Multiplicação = 0
    4, 0, 5, 10, 9
    >>> ler_cinco_inteiros([3, -4, 8, 11, 1])
    Soma = 19
    Multiplicação = -1056
    3, -4, 8, 11, 1

"""
from math import prod
def ler_cinco_inteiros(inteiros: list):
    """Escreva aqui em baixo a sua solução"""
