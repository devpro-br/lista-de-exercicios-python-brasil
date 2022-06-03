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

    if operacao == '+':
        num = n_1 + n_2
    elif operacao == '/':
        num = n_1 / n_2
    elif operacao == '-':
        num = n_1 - n_2
    elif operacao == '*':
        num = n_1 * n_2

    print(f'Resultado: {num :.2f}')

    if num % 2 == 0:
        if num < 0:
          print('Número é par, negativo e inteiro.')
        if num > 0:
            print('Número é par, positivo e inteiro.')
        if num == 0:
            print('Número é par, neutro e inteiro.')
    elif num % 2 != 0 and int(num) == num:
        if num <0:
            print('Número é impar, positivo e inteiro.')
        if num > 0:
            print('Número é impar, positivo e inteiro.')
        if num == 0:
            print('Número é impar, neutro e inteiro.')
    else:
        if num > 0:
            print('Número é positivo e decimal.')
        if num < 0:
            print('Número é negativo e decimal.')