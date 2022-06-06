"""
Exercício 10 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido.

    >>> calcular_numeros_no_intervalo(1, 10)
    '1, 2, 3, 4, 5, 6, 7, 8, 9'
    >>> calcular_numeros_no_intervalo(-10, -1)
    '-10, -9, -8, -7, -6, -5, -4, -3, -2'
    >>> calcular_numeros_no_intervalo(-1, -10)
    ''

"""
from itertools import count

def calcular_numeros_no_intervalo(inicio: int, fim: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    lista = []
    if inicio > fim:
        return ''
    else:
        for numero in count(inicio):
            if numero >= fim:
                break
            lista.append(str(numero))
        return ', '.join(lista)


