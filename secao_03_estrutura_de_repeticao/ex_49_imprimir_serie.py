"""
Exercício 49 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que mostre os n termos da Série a seguir:
    
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
    
    Imprima no final a soma da série.
    

    

    >>> imprimir_serie(5)
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9
    soma = 3.393650793650793
    >>> imprimir_serie(7)
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + 6/11 + 7/13
    soma = 4.477566877566877
    >>> imprimir_serie(3)
    S = 1/1 + 2/3 + 3/5
    soma = 2.2666666666666666
    >>> imprimir_serie(9)
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + 6/11 + 7/13 + 8/15 + 9/17
    soma = 5.540311975606093

"""


def imprimir_serie(n):
    """Escreva aqui em baixo a sua solução"""
    saida = 'S = '
    naturais_e_impares = zip(range(1, n + 1), range(1, 2 * (n + 1), 2))
    saida += ' + '.join(f'{numerador}/{denominador}' for numerador, denominador in naturais_e_impares)

    # Já foi consumido na linha de cima, precisa ser novamente definido
    naturais_e_impares = zip(range(1, n + 1), range(1, 2 * (n + 1), 2))
    soma = sum(numerador/denominador for numerador, denominador in naturais_e_impares)

    print(saida)
    print(f'soma = {soma}')
