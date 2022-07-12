"""
Exercício 02 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. Caso seja igual a 0, retorne None.

    >>> positivo_ou_negativo(1)
    'positivo'
    >>> positivo_ou_negativo(-1)
    'negativo'
    >>> positivo_ou_negativo(0)
    'não tem positivo nem negativo'
    >>> positivo_ou_negativo(-100)
    'negativo'
"""


def positivo_ou_negativo(n):
    while True:
        try:
            numero = float(input('Digite um número: '))
       
        except ValueError:
            print('Digite um número!!!') 
            break
        
        if numero > 0:
                num = "'positivo'"
        elif numero < 0:
                num = "'negativo'"
        else:
                num = "'não tem positivo nem negativo'"
                
        print(num)

