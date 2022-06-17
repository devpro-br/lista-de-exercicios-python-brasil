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


def calcular_numeros_no_intervalo(inicio: int, fim: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    # caso o inicio seja maior q o fim:
    if inicio > fim:
        print("''")
    # se as condições forem boas, o código continua:
    for n in range (inicio, fim):
        # no inicio, precisa ter uma ' pra bater com o doctest
        if n == inicio:
            print("'", end="")
        # no fim (fim menos 1), ele precisa de uma ' pra fechar e bater com o doctest
        if n == fim - 1:
            print(f"{n}'", end="")
            break
        # aqui ele printa tudo
        print(f"{n},", end=" ")
