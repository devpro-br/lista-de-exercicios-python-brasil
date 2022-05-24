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
    """Escreva aqui em baixo a sua solução"""
    numero_int_1 = int(input('Digite o primeiro número inteiro: '))
    numero_int_2 = int(input('Digite o segundo número inteiro: '))
    numero_real = float(input('Digite um número real: '))
    primeiro_calculo = (numero_int_1*2) * (numero_int_2/2)
    segundo_calculo = (numero_int_1*3) + numero_real
    terceiro_calculo = numero_real**3
    print(f'O produto do dobro do primeiro com metade do segundo é {primeiro_calculo:.2f}')
    print(f'A soma do triplo do primeiro com o terceiro é {segundo_calculo:.2f}')
    print(f'O terceiro elevado ao cubo é {terceiro_calculo:.2f}')



