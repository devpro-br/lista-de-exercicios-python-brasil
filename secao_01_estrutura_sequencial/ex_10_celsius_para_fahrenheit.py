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
    while True:
        c_transformar_para_fahrenheit = int(input('Digite a temperatura em celsus: '))
        dividindo_graus_celsus = c_transformar_para_fahrenheit / 5
        multiplica_graus_celsus = dividindo_graus_celsus * 9
        soma_graus_celsus = multiplica_graus_celsus + 32

        soma_graus_celsus = int(soma_graus_celsus)

        print(f'Essa temperatura é de {soma_graus_celsus} Celsius')
transformar_para_fahrenheit()


