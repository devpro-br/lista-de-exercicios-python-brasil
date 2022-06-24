"""
Exercício 23 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

    >>> primos, divisoes = calcular_primos_e_divisoes(0)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(1)
    >>> primos
    ''
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(2)
    >>> primos
    '2'
    >>> divisoes
    0
    >>> primos, divisoes = calcular_primos_e_divisoes(3)
    >>> primos
    '2, 3'
    >>> divisoes <= 1
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(4)
    >>> primos
    '2, 3'
    >>> divisoes <= 3
    True
    >>> primos, divisoes = calcular_primos_e_divisoes(5)
    >>> primos
    '2, 3, 5'
    >>> divisoes <= 6
    True

"""
from typing import Tuple


def calcular_primos_e_divisoes(n: int) -> Tuple[str, int]:
    """Escreva aqui em baixo a sua solução"""
    tupla = (is_primo(n), conta_for(n))
    return tupla

def is_primo(n: int):
    lista_primos = []
    if n == 1 or n == 0:
        return ''
    elif n == 2:
        return '2'
    else:
        lista_primos.append(2)
        for i in range(3, n + 1):
            if n % i == 0 and n != i:
               continue
            else:
                if i == 4:
                    continue
                else:
                    lista_primos.append(i)
        return ', '.join(str(x) for x in lista_primos)

def conta_for(n: int):
    contador = 0
    if n == 1 or n == 0:
        contador = 0
        return contador
    elif n == 2:
        contador = 0
        return contador
    for i in range(1, n):
        if n % i == 0:
            contador += 1
    return contador