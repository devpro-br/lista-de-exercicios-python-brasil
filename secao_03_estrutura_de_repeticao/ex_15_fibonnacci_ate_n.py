"""
Exercício 15 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o
n−ésimo termo.

    >>> calcular_serie_de_fibonacci(1)
    '1'
    >>> calcular_serie_de_fibonacci(2)
    '1, 1'
    >>> calcular_serie_de_fibonacci(3)
    '1, 1, 2'
    >>> calcular_serie_de_fibonacci(4)
    '1, 1, 2, 3'
    >>> calcular_serie_de_fibonacci(5)
    '1, 1, 2, 3, 5'
    >>> calcular_serie_de_fibonacci(6)
    '1, 1, 2, 3, 5, 8'
    >>> calcular_serie_de_fibonacci(7)
    '1, 1, 2, 3, 5, 8, 13'

"""
def calcular_serie_de_fibonacci(n: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    n1 = 1
    n2 = 1
    if n == 1:
        print(f"'{n1}'")
    elif n == 2:
        print(f"'{n1}, {n2}'")
    else:
        print(f"""'{n1}""", end=', ')
        print(f"""{n2}""", end=', ')
        for numero in range(n-2):
            resultado = n1 + n2
            n2 = n1
            n1 = resultado
            if numero == n-3:
                print(resultado, end="'")
            else:
                print(resultado, end=', ')