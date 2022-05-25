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
    p_i = ''
    pos_neg = ''
    dec_int= ''
    resultado = 0
    if operacao == '+':
        resultado = n_1+n_2
        print(f"""Resultado: {resultado:.2f}""")
    elif operacao == '-':
        resultado = n_1-n_2
        print(f"""Resultado: {resultado:.2f}""")
    elif operacao == '/':
        resultado = n_1/n_2
        print(f"""Resultado: {resultado:.2f}""")
    elif operacao == '*':
        resultado = n_1*n_2
        print(f"""Resultado: {resultado:.2f}""")


    if resultado > 0:
        pos_neg = 'positivo'
    elif resultado == 0:
        pos_neg = 'neutro'
    else:
        pos_neg = 'negativo'

    if resultado % 1 == 0:
        dec_int = 'inteiro'
        if resultado % 2 == 0:
            p_i = 'par'
        else:
            p_i = 'impar'
        print(f"""Número é {p_i}, {pos_neg} e {dec_int}.""")
    else:
        dec_int = 'decimal'
        print(f"""Número é {pos_neg} e {dec_int}.""")

