"""
Exercício 32 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120

    >>> calcular_fatorial(1)
    Fatorial de 1:
    1! = 1 = 1
    >>> calcular_fatorial(2)
    Fatorial de 2:
    2! = 2 . 1 = 2
    >>> calcular_fatorial(3)
    Fatorial de 3:
    3! = 3 . 2 . 1 = 6
    >>> calcular_fatorial(4)
    Fatorial de 4:
    4! = 4 . 3 . 2 . 1 = 24
    >>> calcular_fatorial(5)
    Fatorial de 5:
    5! = 5 . 4 . 3 . 2 . 1 = 120

"""
def calcular_fatorial(n: int):
    """Escreva aqui em baixo a sua solução"""
    resultado = 1
    lista = []
    print(f'Fatorial de {n}:')
    print(f'{n}! = ', end='')
    for numero in range(1, n+1):
        resultado *= numero
        lista.append(resultado)
        lista.sort(reverse=True)
    for i in range (0, len(lista)-1):
        lista[i] = lista[i]/lista[i+1]
        lista[i] = int(lista[i])
        i+=1
    print(*lista, sep=' . ', end='')
    print(f' = {resultado}')