"""
Exercício 24 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

    >>> fazer_operacao_e_classificar(2, 3, '+')
    Resultado: 5.00
    Número é impar, positivo e inteiro.
    >>> fazer_operacao_e_classificar(-4, 2, '/')
    Resultado: -2.00
    Número é par, negativo e inteiro.
    >>> fazer_operacao_e_classificar(0, 2, '*')
    Resultado: 0.00
    Número é par, neutro e inteiro.
    >>> fazer_operacao_e_classificar(-3.14, 2, '*')
    Resultado: -6.28
    Número é negativo e decimal.
    >>> fazer_operacao_e_classificar(3.14, 2, '-')
    Resultado: 1.14
    Número é positivo e decimal.

"""


def fazer_operacao_e_classificar(n_1: float, n_2: float, operacao: str):
    """Escreva aqui em baixo a sua solução"""
    resultado = eval(f'{n_1}{operacao}{n_2}')

    par_ou_impar = {
        'par': lambda x: x % 2 == 0,
        'impar': lambda x: x % 2 != 0
    }
    positivo_ou_negativo = {
        'positivo': lambda x: x > 0,
        'negativo': lambda x: x < 0,
        'neutro': lambda x: x == 0
    }
    inteiro_ou_decimal = {
        'inteiro': lambda x: x % 1 == 0,
        'decimal': lambda x: x % 1 != 0
    }
    #
    for i in par_ou_impar:
        if par_ou_impar[i](resultado):
            par_ou_impar = i
            break
    for i in positivo_ou_negativo:
        if positivo_ou_negativo[i](resultado):
            positivo_ou_negativo = i
            break
    for i in inteiro_ou_decimal:
        if inteiro_ou_decimal[i](resultado):
            inteiro_ou_decimal = i
            break
    if inteiro_ou_decimal == 'decimal':
        print(f'Resultado: {resultado:.2f}')
        print(f'Número é {positivo_ou_negativo} e {inteiro_ou_decimal}.')
        return
    print(f'Resultado: {resultado:.2f}')
    print(f'Número é {par_ou_impar}, {positivo_ou_negativo} e {inteiro_ou_decimal}.')