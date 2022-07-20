"""
Exercício 06 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele
mostre os números um ao lado do outro.

    >>> escrever_numeros_de_1_a_20(formato = 'um_abaixo_do_outro')
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    >>> escrever_numeros_de_1_a_20(formato = 'um_ao_lado_do_outro')
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
"""


def escrever_numeros_de_1_a_20(formato:str) -> str:
    """Escreva aqui em baixo a sua solução"""
    # lista = list(range(1,21))
    # print(formato)


    if formato == 'um_abaixo_do_outro':
        numero = 1
        while numero <= 20:
            print(numero)
            numero += 1
    else:
        numero = 1
        while numero < 20:
            print(numero, end=' ')
            numero += 1
            if numero == 20:
                print(numero, end='')

        


    






    

