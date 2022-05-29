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
    n1 = 0
    n2 = 1
    n3 = 1
    print(f"'{n1}, {n2}, {n3}", end=', ')
    resultado = 0
    while resultado < 500:
        resultado = n2 + n3
        n3 = n2
        n2 = resultado
        if resultado >= 500:
            print(resultado, end="'")
        else:
            print(resultado, end=', ')