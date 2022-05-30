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


def decompor_numero(numero: int):
    """Escreva aqui em baixo a sua solução"""
    if numero <= 0:
        print(f"'O número precisa ser positivo'")
        return None
    if numero >= 1000:
        print("'O número precisa ser menor que 1000'")
        return None
    #------------------------------------------

    string_num = []
    x = list(str(numero))
    numero_aux = numero
    if 100 <= numero < 200:
        string_num.append(x[0] + ' centena')
        numero -= (numero // 100) * 100
        del x[0]
    elif 200<= numero:
        string_num.append(x[0] + ' centenas')
        numero -= (numero // 100) * 100
        del x[0]

    #--------------------------------

    if 10 <= numero < 20:
        string_num.append(x[0] + ' dezena')
        numero -= (numero //10) * 10
        del x[0]
    elif numero >= 20:
        string_num.append(x[0] + ' dezenas')
        numero -= (numero // 10) * 10
        del x[0]

    elif numero < 10 and numero_aux >= 100 :
        del x[0]
    #----------------------------------

    if numero == 1:
        string_num.append(x[0] + ' unidade')
    elif numero > 1:
        string_num.append(x[0] + ' unidades')

    #-----------------------------------------

    if len(string_num) == 3:
        print(f"'{numero_aux} = {string_num[0]}, {string_num[1]} e {string_num[2]}'")
    elif len(string_num) == 2:
        print(f"'{numero_aux} = {string_num[0]} e {string_num[1]}'")
    elif len(string_num) == 1:
        print(f"'{numero_aux} = {string_num[0]}'")









