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
    num = numero
    if numero >= 1000:
        print(f"'O número precisa ser menor que 1000'")
    elif numero <= 0:
        print(f"'O número precisa ser positivo'")
    else:
        if numero < 1000 and numero > 0:
            unidade = numero % 10
            numero = (numero - unidade)/10
            dezena = numero % 10
            numero = (numero - dezena)/10
            centena = numero
            centena = int(centena)
            dezena = int(dezena)
            if centena > 1 and dezena > 1 and unidade > 1:
                print(f"'{num} = {centena} centenas, {dezena} dezenas e {unidade} unidades'")
            elif centena > 1 and dezena == 0 and unidade == 0:
                print(f"'{num} = {centena} centenas'")
            elif centena == 1 and dezena == 0 and unidade == 0:
                print(f"'{num} = {centena} centena'")
            elif centena > 1 and dezena > 1 and unidade == 0:
                print(f"'{num} = {centena} centenas e {dezena} dezenas'")
            elif centena > 1 and dezena == 1 and unidade == 0:
                print(f"'{num} = {centena} centenas e {dezena} dezena'")
            elif centena > 1 and dezena == 0 and unidade > 1:
                print(f"'{num} = {centena} centenas e {unidade} unidades'")
            elif centena > 1 and dezena == 0 and unidade == 1:
                print(f"'{num} = {centena} centenas e {unidade} unidade'")
            elif centena > 1 and dezena == 1 and unidade == 1:
                print(f"'{num} = {centena} centenas, {dezena} dezena e {unidade} unidade'")
            elif centena == 1 and dezena == 1 and unidade == 1:
                print(f"'{num} = {centena} centena, {dezena} dezena e {unidade} unidade'")
            elif centena == 1 and dezena == 0 and unidade == 1:
                print(f"'{num} = {centena} centena e {unidade} unidade'")
            elif centena == 0 and dezena > 1 and unidade > 1:
                print(f"'{num} = {dezena} dezenas e {unidade} unidades'")
            elif centena == 0 and dezena > 1 and unidade == 0:
                print(f"'{num} = {dezena} dezenas'")
            elif centena == 0 and dezena > 1 and unidade == 1:
                print(f"'{num} = {dezena} dezenas e {unidade} unidade'")
            elif centena == 0 and dezena == 1 and unidade == 0:
                print(f"'{num} = {dezena} dezena'")
            elif centena == 0 and dezena == 1 and unidade > 1:
                print(f"'{num} = {dezena} dezena e {unidade} unidades'")
            elif centena == 0 and dezena == 0 and unidade == 1:
                print(f"'{num} = {unidade} unidade'")
            elif centena == 0 and dezena == 0 and unidade > 1:
                print(f"'{num} = {unidade} unidades'")