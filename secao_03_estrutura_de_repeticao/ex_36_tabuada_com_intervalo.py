"""
Exercício 36 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada
não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

    >>> gerar_tabuada(1, 1, 10)
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
    >>> gerar_tabuada(2, 2, 8)
    2 X 2 = 4
    2 X 3 = 6
    2 X 4 = 8
    2 X 5 = 10
    2 X 6 = 12
    2 X 7 = 14
    2 X 8 = 16
    >>> gerar_tabuada(3, 5, 7)
    3 X 5 = 15
    3 X 6 = 18
    3 X 7 = 21
    >>> gerar_tabuada(3, 5, 4)
    O limite final (4) deve ser maior que o inicial (5)
    >>> gerar_tabuada(3, 9, 1)
    O limite final (1) deve ser maior que o inicial (9)

"""


def gerar_tabuada(n: int, de: int, ate: int):
    """Escreva aqui em baixo a sua solução"""
