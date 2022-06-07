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
    fatorial = []
    aux = n
    calculo = 1
    condicao = 0
    while aux > 0:
        fatorial.append(n)        
        n = n-1
        if aux == 0 or aux == 1:
            print('Fatorial de 1:')
            print('1! = 1 = 1')
            break
        if n >= 0:
            if n >= 0 and condicao == 0:
                calculo = fatorial[len(fatorial)-1]*calculo
            if n == 0:             
                print('Fatorial de %.0f:'%aux)
                print('%.0f! ='%aux, end='')                    
            if n == 0 or condicao == 1:
                condicao = 1                
                if n <= aux:
                    print(' ', fatorial[n], end=' .', sep='')
                    n = n+2
                    if n == aux:
                        print(' ', fatorial[n-1], end=' = ', sep='')
                        print(calculo)
                        break
                else:
                    break          
                
