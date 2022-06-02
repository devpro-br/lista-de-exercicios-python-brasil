"""
Exercício 16 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o
 valor seja maior que 500.

    >>> calcular_serie_de_fibonacci_ate_valor_ser_maior_que_500()
    '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610'
"""


def calcular_serie_de_fibonacci_ate_valor_ser_maior_que_500() -> str:
    """Escreva aqui em baixo a sua solução"""
    fibonacci = [0]
    contador = 0
    print("'",end='')
    while fibonacci[contador] < 500:
        if len(fibonacci)==1:
            fibonacci.append(1)
            print(fibonacci[contador], end=', ')            
            contador = contador + 1
            continue
        if len(fibonacci) >= 2:
            if len(fibonacci) <= 2:
                fibonacci.append(1)            
                print(fibonacci[contador], end=', ')
                contador = contador + 1                
                continue        
            elif fibonacci[contador] < 500:
                numero = fibonacci[(contador)] + fibonacci[(contador-1)]
                fibonacci.append(numero)
                print(fibonacci[contador], end=', ')                           
                contador = contador + 1
                continue
    else:
        numero = fibonacci[(contador-1)] + fibonacci[(contador-2)]
        fibonacci.append(numero)
        print(fibonacci[contador], end='')
        print("'",end='')
       