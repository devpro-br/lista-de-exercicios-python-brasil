"""
Exercício 10 da sessão de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
Mostrar apenas valor inteiro da temperatura

    >>> from sessao_01_estrutura_sequencial import celsius_para_fahrenheit_10
    >>> celsius_para_fahrenheit_10.input = lambda k: '0'
    >>> celsius_para_fahrenheit_10.transformar_para_fahrenheit()
    Essa temperatura é de 32 Fahrenheit
    >>> celsius_para_fahrenheit_10.input = lambda k: '21'
    >>> celsius_para_fahrenheit_10.transformar_para_fahrenheit()
    Essa temperatura é de 70 Fahrenheit

"""


def transformar_para_fahrenheit():
    """Escreva aqui em baixo a sua solução"""
    temperatura_celsius = float(input('Digite uma temperatura em fahrenheit: '))
    temperatura_fahrenheit = temperatura_celsius * 9 / 5 + 32   # 5 * ((temperatura_fahrenheit - 32) / 9)
    print(f'Essa temperatura é de {temperatura_fahrenheit:.0f} Fahrenheit')
