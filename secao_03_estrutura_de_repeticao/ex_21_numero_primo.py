"""
Exercício 21 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é
divisível somente por ele mesmo e por 1.

    >>> eh_primo(0)
    False
    >>> eh_primo(1)
    False
    >>> eh_primo(2)
    True
    >>> eh_primo(3)
    True
    >>> eh_primo(4)
    False
    >>> eh_primo(5)
    True
    >>> eh_primo(6)
    False
    >>> eh_primo(7)
    True
    >>> eh_primo(8)
    False
    >>> eh_primo(9)
    False
    >>> eh_primo(10)
    False
    >>> eh_primo(11)
    True
    >>> eh_primo(547)
    True
    >>> eh_primo(548)
    False

"""
from itertools import chain
from math import sqrt, ceil


def eh_primo(n: int) -> bool:
    """Escreva aqui em baixo a sua solução"""
    if n < 2:
        return False
    elif n == 2:
        return True

    raiz_de_n = sqrt(n)
    for i in chain([2], range(3, ceil(raiz_de_n) + 1, 2)):
        if n % i == 0:
            return False
    return True
