"""
Exercício 01 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

    >>> ler_5_valores()

"""


def ler_5_valores():
    """Escreva aqui em baixo a sua solução"""
    numeros = []
    for _ in range(5):
        num = float(input('Digite um número: '))
        numeros.append(num)
    print(numeros)


#Ex 02
numeros = []
    for _ in range(10):
        num = float(input('Digite um número: '))
        numeros.append(num)
    numeros.reverse()
    print(numeros)