"""
Exercício 19 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    >>> decompor_numero(1000)
    'O número precisa ser menor que 1000'
    >>> decompor_numero(-1)
    'O número precisa ser positivo'
    >>> decompor_numero(326)
    '326 = 3 centenas, 2 dezenas e 6 unidades'
    >>> decompor_numero(300)
    '300 = 3 centenas'
    >>> decompor_numero(100)
    '100 = 1 centena'
    >>> decompor_numero(320)
    '320 = 3 centenas e 2 dezenas'
    >>> decompor_numero(310)
    '310 = 3 centenas e 1 dezena'
    >>> decompor_numero(305)
    '305 = 3 centenas e 5 unidades'
    >>> decompor_numero(301)
    '301 = 3 centenas e 1 unidade'
    >>> decompor_numero(311)
    '311 = 3 centenas, 1 dezena e 1 unidade'
    >>> decompor_numero(111)
    '111 = 1 centena, 1 dezena e 1 unidade'
    >>> decompor_numero(101)
    '101 = 1 centena e 1 unidade'
    >>> decompor_numero(25)
    '25 = 2 dezenas e 5 unidades'
    >>> decompor_numero(20)
    '20 = 2 dezenas'
    >>> decompor_numero(21)
    '21 = 2 dezenas e 1 unidade'
    >>> decompor_numero(10)
    '10 = 1 dezena'
    >>> decompor_numero(16)
    '16 = 1 dezena e 6 unidades'
    >>> decompor_numero(1)
    '1 = 1 unidade'
    >>> decompor_numero(7)
    '7 = 7 unidades'

"""


from math import ceil, floor


def decompor_numero(numero: int):
    """Escreva aqui em baixo a sua solução"""
    if numero < 1000 and numero > 0:
        if numero < 10 and numero != 1:
            print('\'%0.f = %0.f unidades\'' %(numero, numero))
        elif numero == 1:
            print('\'%0.f = %0.f unidade\'' %(numero, numero))
        elif numero >= 10 and numero < 100:
            numero_unidade = numero % 10
            numero_dezenas = floor(numero/10)
            if numero_unidade == 1 and numero_dezenas == 1:                
                print('\'%0.f = %0.f dezena e %0.f unidade\'' %(numero, numero_dezenas, numero_unidade))
            elif numero_unidade == 0 and numero_dezenas == 1:                
                print('\'%0.f = %0.f dezena\'' %(numero, numero_dezenas))
            elif numero_dezenas == 1:
                print('\'%0.f = %0.f dezena e %0.f unidades\'' %(numero, numero_dezenas, numero_unidade))
            elif numero_unidade == 1:
                print('\'%0.f = %0.f dezenas e %0.f unidade\'' %(numero, numero_dezenas, numero_unidade))
            elif numero_unidade == 0:
                print('\'%0.f = %0.f dezenas\'' %(numero, numero_dezenas))
            else:
                print('\'%0.f = %0.f dezenas e %0.f unidades\'' %(numero, numero_dezenas, numero_unidade))
        elif numero >= 100:
            numero_aux = numero % 100
            numero_unidade = numero_aux % 10
            numero_dezenas = floor(numero_aux/10)
            numero_centenas = floor(numero/100)
            if numero_unidade == 1 and numero_dezenas == 1 and numero_centenas == 1:                
                print('\'%0.f = %0.f centena, %0.f dezena e %0.f unidade\'' %(numero, numero_centenas, numero_dezenas, numero_unidade))
            elif numero_centenas == 1  and numero_dezenas == 1 and numero_unidade == 0:                
                print('\'%0.f = %0.f centena e %0.f dezena\'' %(numero, numero_centenas, numero_dezenas))
            elif numero_centenas == 1  and numero_dezenas == 0 and numero_unidade == 0:                
                print('\'%0.f = %0.f centena\'' %(numero, numero_centenas))
            elif numero_centenas == 1 and numero_dezenas == 0 and numero_unidade == 1  :                
                print('\'%0.f = %0.f centena e %0.f unidade\'' %(numero, numero_centenas, numero_unidade))
            elif numero_dezenas == 1 and numero_unidade == 1:                
                print('\'%0.f = %0.f centenas, %0.f dezena e %0.f unidade\'' %(numero, numero_centenas, numero_dezenas, numero_unidade))            
            elif numero_dezenas == 1 and numero_unidade == 0:                
                print('\'%0.f = %0.f centenas e %0.f dezena\'' %(numero, numero_centenas, numero_dezenas))
            elif numero_dezenas == 1:
                print('\'%0.f = %0.f centenas, %0.f dezena e %0.f unidades\'' %(numero, numero_centenas, numero_dezenas, numero_unidade))
            elif numero_dezenas == 0 and numero_unidade == 0:
                print('\'%0.f = %0.f centenas\'' %(numero, numero_centenas))
            elif numero_dezenas == 0 and numero_unidade == 1:                
                print('\'%0.f = %0.f centenas e %0.f unidade\'' %(numero, numero_centenas, numero_unidade))
            elif numero_unidade == 1:
                print('\'%0.f = %0.f centenas, %0.f dezenas e %0.f unidade\'' %(numero, numero_centenas, numero_dezenas, numero_unidade))  
            elif numero_dezenas == 0:
                print('\'%0.f = %0.f centenas e %0.f unidades\'' %(numero, numero_centenas, numero_unidade))
            elif numero_unidade == 0:
                print('\'%0.f = %0.f centenas e %0.f dezenas\'' %(numero, numero_centenas, numero_dezenas))               
            else:
                print('\'%0.f = %0.f centenas, %0.f dezenas e %0.f unidades\'' %(numero, numero_centenas, numero_dezenas, numero_unidade))       
    elif numero < 0:
        return 'O número precisa ser positivo'
    else:
        return 'O número precisa ser menor que 1000'