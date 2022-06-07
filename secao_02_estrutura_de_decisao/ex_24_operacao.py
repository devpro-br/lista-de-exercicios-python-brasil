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
    soma = n_1 + n_2
    sub = n_1 - n_2
    mul = n_1 * n_2
    div = n_1 / n_2

    if operacao == '+':
     resultado = soma
    elif operacao == '-':
        resultado = sub
    if operacao == '*':
        resultado = mul
    elif operacao == '/':
        resultado = div

    if resultado // 1 == resultado:
        tipo = 'inteiro'
    else:
        tipo = "decimal"

    if resultado == 0:
        p_n = 'neutro'
    elif resultado >= 0:
        p_n = 'positivo'
    elif resultado <= 0:
        p_n = 'negativo'

    # a = list(str(resultado))

    if resultado % 2 == 0 and tipo != 'decimal':
        p_i = 'par'
    elif resultado % 2 != 0 and tipo != 'decimal':
        p_i = 'impar'
    else:
        p_i =''

    print(f'Resultado: {resultado:.2f}')

    if tipo == 'decimal':
        print(f'Número é {p_n} e {tipo}.')
    else:
        print(f'Número é {p_i}, {p_n} e {tipo}.')
   
      

