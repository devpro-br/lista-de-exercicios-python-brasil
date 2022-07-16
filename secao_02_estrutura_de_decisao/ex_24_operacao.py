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
            num_1 = n_1 #float(input('Entre com o primeiro número: '))
            
            num_2 = n_2#float(input('Entre com o segundo número: '))
            
            while not operacao in ('+', '-', '*', '/'):
                #operacao = input('Entre com a operacao desejada: (+, -, / ou *): ')
             

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

            if num < 0:
                pos_neg = 'negativo'
            if num > 0:
                pos_neg = 'positivo'            
            if num == 0:
                pos_neg = 'neutro'
                r_par_imp = 'par'
            par_imp  = resul % 2

            if par_imp == 0:
                r_par_imp = "par"       
            else:
                r_par_imp = "impar"

            if dec_int == 'decimal':
                saida = f'Número é {pos_neg} e {dec_int}'
            else:
                saida = f'Número é {r_par_imp}, {pos_neg} e {dec_int}'
            
            #-------------------------------------------------------    
            print(f'Resultado: {resul:.2f}') 
            print(saida) 
            break
        except ValueError:
            print ('Entrada inválida!!!')

