"""
Exercício 10 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
Mostrar apenas valor inteiro da temperatura

    >>> from secao_01_estrutura_sequencial import ex_10_celsius_para_fahrenheit
    >>> ex_10_celsius_para_fahrenheit.input = lambda k: '0'
    >>> ex_10_celsius_para_fahrenheit.transformar_para_fahrenheit()
    Essa temperatura é de 32 Fahrenheit
    >>> ex_10_celsius_para_fahrenheit.input = lambda k: '21'
    >>> ex_10_celsius_para_fahrenheit.transformar_para_fahrenheit()
    Essa temperatura é de 70 Fahrenheit

"""


def transformar_para_fahrenheit():
    """Escreva aqui em baixo a sua solução"""
    graus = float(input("Digite quantos graus Celsius devem ser convertidos para Fahrenheit: "))
    convertido = 32 + (graus * (9/5))
    print("Essa temperatura é de", "%.0f" % convertido, "Fahrenheit")