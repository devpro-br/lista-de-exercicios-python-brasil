"""
Exercício 09 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre-os em ordem decrescente.

    >>> ordenar_decrescente(2, 3, 5)
    5, 3, 2
    >>> ordenar_decrescente(10, 5.55, 7)
    10, 7, 5.55
    >>> ordenar_decrescente(20, 30, 17.62)
    30, 20, 17.62
    >>> ordenar_decrescente(7, 1, 15)
    15, 7, 1

"""


def ordenar_decrescente(x, y, z):
    """Escreva aqui em baixo a sua solução"""
    if x > y:
        if x > z:
            if z > y:
                print(x, z, y, sep=', ')                      
            else:
                print(x, y, z, sep=', ')     
        else:
            if x > y:
                print(z, x, y, sep=', ')                 
            else:
                print(z, y, x, sep=', ')            
    else:
        if y > z:
            if z > x:
                print(y, z, x, sep=', ') 
            else:
                print(y, x, z, sep=', ')         
        else:
            if x > y:
                print(z, x, y, sep=', ')                 
            else:
                print(z, y, x, sep=', ') 