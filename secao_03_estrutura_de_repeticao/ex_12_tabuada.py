"""
Exercício 12 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.

    >>> gerar_tabuada(0)
    Somente pode ser gerada tabuada de 1 a 10
    >>> gerar_tabuada(11)
    Somente pode ser gerada tabuada de 1 a 10
    >>> gerar_tabuada(1)
    1 X 1 = 1
    1 X 2 = 2
    1 X 3 = 3
    1 X 4 = 4
    1 X 5 = 5
    1 X 6 = 6
    1 X 7 = 7
    1 X 8 = 8
    1 X 9 = 9
    1 X 10 = 10
    >>> gerar_tabuada(2)
    2 X 1 = 2
    2 X 2 = 4
    2 X 3 = 6
    2 X 4 = 8
    2 X 5 = 10
    2 X 6 = 12
    2 X 7 = 14
    2 X 8 = 16
    2 X 9 = 18
    2 X 10 = 20
    >>> gerar_tabuada(3)
    3 X 1 = 3
    3 X 2 = 6
    3 X 3 = 9
    3 X 4 = 12
    3 X 5 = 15
    3 X 6 = 18
    3 X 7 = 21
    3 X 8 = 24
    3 X 9 = 27
    3 X 10 = 30
    >>> gerar_tabuada(4)
    4 X 1 = 4
    4 X 2 = 8
    4 X 3 = 12
    4 X 4 = 16
    4 X 5 = 20
    4 X 6 = 24
    4 X 7 = 28
    4 X 8 = 32
    4 X 9 = 36
    4 X 10 = 40
    >>> gerar_tabuada(5)
    5 X 1 = 5
    5 X 2 = 10
    5 X 3 = 15
    5 X 4 = 20
    5 X 5 = 25
    5 X 6 = 30
    5 X 7 = 35
    5 X 8 = 40
    5 X 9 = 45
    5 X 10 = 50
    >>> gerar_tabuada(6)
    6 X 1 = 6
    6 X 2 = 12
    6 X 3 = 18
    6 X 4 = 24
    6 X 5 = 30
    6 X 6 = 36
    6 X 7 = 42
    6 X 8 = 48
    6 X 9 = 54
    6 X 10 = 60
    >>> gerar_tabuada(7)
    7 X 1 = 7
    7 X 2 = 14
    7 X 3 = 21
    7 X 4 = 28
    7 X 5 = 35
    7 X 6 = 42
    7 X 7 = 49
    7 X 8 = 56
    7 X 9 = 63
    7 X 10 = 70
    >>> gerar_tabuada(8)
    8 X 1 = 8
    8 X 2 = 16
    8 X 3 = 24
    8 X 4 = 32
    8 X 5 = 40
    8 X 6 = 48
    8 X 7 = 56
    8 X 8 = 64
    8 X 9 = 72
    8 X 10 = 80
    >>> gerar_tabuada(9)
    9 X 1 = 9
    9 X 2 = 18
    9 X 3 = 27
    9 X 4 = 36
    9 X 5 = 45
    9 X 6 = 54
    9 X 7 = 63
    9 X 8 = 72
    9 X 9 = 81
    9 X 10 = 90
    >>> gerar_tabuada(10)
    10 X 1 = 10
    10 X 2 = 20
    10 X 3 = 30
    10 X 4 = 40
    10 X 5 = 50
    10 X 6 = 60
    10 X 7 = 70
    10 X 8 = 80
    10 X 9 = 90
    10 X 10 = 100

"""


def gerar_tabuada(n: int) -> str:
    """Escreva aqui em baixo a sua solução"""
