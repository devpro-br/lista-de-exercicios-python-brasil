"""
Exercício 05 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que receba um vetor de inteiros. Armazene os números pares no vetor PAR e os
números IMPARES no vetor impar. Imprima os três vetores.

    >>> separar_em_vertores_par_e_impar([])
    'Vetor original: []. Vetor com elementos pares: []. Vetor com elementos impares: [].'
    >>> separar_em_vertores_par_e_impar([1])
    'Vetor original: [1]. Vetor com elementos pares: []. Vetor com elementos impares: [1].'
    >>> separar_em_vertores_par_e_impar([1, 2])
    'Vetor original: [1, 2]. Vetor com elementos pares: [2]. Vetor com elementos impares: [1].'
    >>> separar_em_vertores_par_e_impar(list(range(10)))
    'Vetor original: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]. Vetor com elementos pares: [0, 2, 4, 6, 8]. Vetor com elementos impares: [1, 3, 5, 7, 9].'

"""


def separar_em_vertores_par_e_impar(inteiros: list) -> str:
    """Escreva aqui em baixo a sua solução"""
