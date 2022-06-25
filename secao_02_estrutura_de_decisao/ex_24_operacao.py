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
    
while True:
    try:
        operacao = '?'
        num_1 = float(input('Entre com o primeiro número: '))
        while not operacao in ('+', '-', '*', '/'):
            operacao = input('Entre com a operacao desejada: (+, -, / ou *): ')
        
        num_2 = float(input('Entre com o segundo número: '))
   

        if operacao == '+':
            resul = num_1 + num_2
        elif operacao == '-':
            resul = num_1 - num_2
        elif operacao == '/':
            resul = num_1 / num_2
        elif operacao == '*':
            resul = num_1 * num_2

        num = round(resul)
        if resul == num:
            dec_int = 'inteiro'
        else:
            dec_int = 'decimal'

        if resul < 0:
            pos_neg = 'negativo'
        else:
            pos_neg = 'positivo'

        par_imp  = resul % 2

        if par_imp == 0:
            r_par_imp = "par"       
        else:
            r_par_imp = "impar"
        # para atender ao doctest do curso, apesar de zero ser par, 
        # declaro como neutro:
        # -1, 0, 1 --> número par fica entre impares. 
        if resul == 0:
            r_par_imp = 'neutro'
        #-------------------------------------------------------    
        print(f'Resultado: {resul:.2f}') 
        print(f'Número é {r_par_imp}, {pos_neg} e {dec_int}') 
        break
    except ValueError:
        print ('Entrada inválida!!!')
