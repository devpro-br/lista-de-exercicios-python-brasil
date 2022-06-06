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
from os import uname_result

def trata_string(numero, unidade):
    retorno = ''
    if numero == 1:
        retorno = f'1 {unidade}'
    elif numero > 1:
        retorno = f'{numero} {unidade}s'
    return retorno

def decompor_numero(numero: int):
    """Escreva aqui em baixo a sua solução"""
    if numero > 999:
        print("'O número precisa ser menor que 1000'")
        return
    if numero < 0:
        print("'O número precisa ser positivo'")
        return

    centenas_str = ''
    dezenas_str = ''
    unidades_str = ''

    pos_nums = []
    num = numero
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10

    if pos_nums[0] > 0:
        num = pos_nums[0]
        unidades_str = trata_string(num,'unidade')
    if len(pos_nums)>1 and pos_nums[1] > 0:
        num = pos_nums[1]
        dezenas_str = trata_string(num,'dezena')
    if len(pos_nums)>2 and pos_nums[2] > 0:
        num = pos_nums[2]
        centenas_str = trata_string(num,'centena')

    result_array = []
    result_string = ''

    if (centenas_str):
        result_array.append(centenas_str)
    if (dezenas_str):
        result_array.append(dezenas_str)
    if (unidades_str):
        result_array.append(unidades_str)

    if len(result_array) == 1:
        result_string = f"{numero} = {result_array[0]}"
    if 1 < len(result_array) < 3:
        result_string = f"{numero} = {result_array[0]} e {result_array[1]}"
    if len(result_array) == 3:
        result_string = f"{numero} = {result_array[0]}, {result_array[1]} e {result_array[2]}"

    print(f"'{result_string}'")
