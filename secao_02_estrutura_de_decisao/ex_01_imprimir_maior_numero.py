"""
Exercício 01 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça dois números e imprima o maior deles.

    >>> maior_de_dois_numeros(2,3)
    3
    >>> maior_de_dois_numeros(-1,-10)
    -1
    >>> maior_de_dois_numeros(-5,3)
    3
    >>> maior_de_dois_numeros(7,-14)
    7
"""


# def maior_de_dois_numeros(x, y):
#     """Escreva aqui em baixo a sua solução"""
#     if x > y:
#         print(f"O valor {x} é maior que {y}")
#     elif x == y:
#         print(f"O valor {x} é igual a {y}")
#     else:
#         print(f"O valor {y} é maior que {x}")

def maior_de_dois_numeros(x, y):
    """Escreva aqui em baixo a sua solução"""
    if x > y:
        return x
    else:
        return y
    
if __name__ == "__main__":
    print(maior_de_dois_numeros(2, 4))
    print(maior_de_dois_numeros(4, 5))
    print(maior_de_dois_numeros(6, 4))
    print(maior_de_dois_numeros(0, 4))
    print(maior_de_dois_numeros(2, 2))

# if __name__ == "__main__":
#     maior_de_dois_numeros(2,4)
#     maior_de_dois_numeros(4,5)
#     maior_de_dois_numeros(6,4)
#     maior_de_dois_numeros(0,4)
#     maior_de_dois_numeros(2,2)
