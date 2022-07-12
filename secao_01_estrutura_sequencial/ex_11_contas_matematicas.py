"""
Exercício 11 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 1) o produto do dobro do primeiro com metade do segundo;
 2) a soma do triplo do primeiro com o terceiro;
 3) o terceiro elevado ao cubo.

 Apresente os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_11_contas_matematicas
    >>> numeros = ['3.14', '43', '42']
    >>> ex_11_contas_matematicas.input = lambda k: numeros.pop()
    >>> ex_11_contas_matematicas.calcular_formulas()
    O produto do dobro do primeiro com metade do segundo é 1806.00
    A soma do triplo do primeiro com o terceiro é 129.14
    O terceiro elevado ao cubo é 30.96

"""


def calcular_formulas():
    while True:
        try:

            num_i_01 = float(input('Entre com um número inteiro: '))
            num_i_02 = float(input('Entre com outro número inteiro: '))
            num_real = float(input('Entre com um número real: '))

            print(f'O produto do dobro do primeiro com metade do segundo é {(((num_i_01)*2) * (num_i_02/2)):.2f}')

            print(f'A soma do triplo do primeiro com o terceiro é {((3 * num_i_01) + num_real):.2f}')

            print(f'O terceiro elevado ao cubo é {(num_real ** 3):.2f}')
            break
        except ValueError:
