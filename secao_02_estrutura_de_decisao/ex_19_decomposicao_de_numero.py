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
    centenas_str = dezenas_str = unidades_str = ''
    
    centenas_int, numero = divmod(numero, 100)

    partes_numericas = 0

    if centenas_int == 1:
        centenas_str = '1 centena'
    elif centenas_int > 1:
        centenas_str = f'{centenas_int} centenas'

        centenas_int = numero // 100

    dezenas_int, numero = divmod(numero, 100)

    if dezenas_int == 1:
        dezenas_str = '1 dezena'
        partes_numericas += 1
    elif dezenas_int > 1:
        dezenas_str = f'{dezenas_int} dezenas'
        partes_numericas += 1

    if numero == 1:
        unidades_str = '1 unidade'
        partes_numericas += 1
    elif numero > 1:
        unidades_str = f'{numero} unidades'
        partes_numericas += 1
    
    if partes_numericas == 0:
        print('Numero 0 nao possui centenas, dezenas ou unidades')
    elif partes_numericas == 1:
        print(centenas_str + dezenas_str + unidades_str)
    elif partes_numericas == 2:
        if centenas_str != '':
            segunda_parte = dezenas_str + unidades_str
            print(f'{centenas_str} e {segunda_parte}')
        else:
            print(f'{dezenas_str} e {unidades_str}')
    
    elif partes_numericas == 3:
        # print(f'{centenas_str}, {dezenas_str} e {unidades_str}')
        print(f'{numero} = {centenas_int} {centenas_str}, {dezenas_int} {dezenas_str} e {numero} {unidades_str}')