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
    fibonacci = []
    contador = 0
    print("'",end='')
    while contador < n and n > 0:
        if n == 1:
            fibonacci.append(1)
            print(fibonacci[contador], end='')
            print("'")
            contador = contador + 1
        if n != 1:
            if len(fibonacci) <= 1:
                fibonacci.append(1)            
                print(fibonacci[contador], end=', ')
                contador = contador + 1
                if n == 2:
                    print(fibonacci[contador-1], end='')
                    print("'")
                    contador = contador + 1          
            elif contador < n-1:
                numero = fibonacci[(contador-1)] + fibonacci[(contador-2)]
                fibonacci.append(numero)
                print(fibonacci[contador], end=', ')            
                contador = contador + 1
                continue
            else:
                numero = fibonacci[(contador-1)] + fibonacci[(contador-2)]
                fibonacci.append(numero)
                print(fibonacci[contador], end='')
                print("'",end='')
                break
    

        

