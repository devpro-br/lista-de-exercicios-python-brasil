"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120

    >>> calcular_fatorial(0)
    1
    >>> calcular_fatorial(1)
    1
    >>> calcular_fatorial(2)
    2
    >>> calcular_fatorial(3)
    6
    >>> calcular_fatorial(4)
    24
    >>> calcular_fatorial(5)
    120

"""


def calcular_fatorial(n: int) -> int:
    """Escreva aqui em baixo a sua solução"""
    fatorial = []
    aux = n
    calculo = 1
    while True:
        fatorial.append(n)        
        n = n-1
        if aux == 0 or aux == 1:
            print(1)
            break
        if n >= 0:              
            calculo = fatorial[len(fatorial)-1]*calculo                    
            if n == 0:
                print(calculo) 
                break

            
