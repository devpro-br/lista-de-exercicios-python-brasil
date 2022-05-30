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
    #Realiza operação desejada
    if operacao == '+':
      resultado_operacao = n_1 + n_2
    elif operacao == '-':
      resultado_operacao = n_1 - n_2
    elif operacao == '/':
      resultado_operacao = n_1 / n_2
    elif operacao == '*':
      resultado_operacao = n_1 * n_2

    #Testa se é decimal ou inteiro
    if int(str(float(resultado_operacao)).split(('.'))[1]) >= 1:
        decimal_inteiro = 'decimal.'
    else:
        decimal_inteiro = 'inteiro.'

    #Testa se é positivo, negativo ou neutro
    if resultado_operacao > 0:
      positivo_negativo = 'positivo'
    elif resultado_operacao == 0:
      positivo_negativo = 'neutro'
    else:
      positivo_negativo = 'negativo'

    #Testa se é par ou impar
    teste = resultado_operacao % 2
    if teste > 0:
        par_impar = 'impar,'
    else:
        par_impar = 'par,'

    #Entrega resposta
    if decimal_inteiro == 'decimal.':
      print('Resultado: %.2f' % resultado_operacao)
      print('Número é', positivo_negativo, 'e', decimal_inteiro)
    else:
      print('Resultado: %.2f' % resultado_operacao)
      print('Número é', par_impar, positivo_negativo, 'e', decimal_inteiro)       