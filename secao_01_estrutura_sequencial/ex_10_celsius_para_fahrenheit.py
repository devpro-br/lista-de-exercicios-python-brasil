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


def transformar_para_fahrenheit(C):
    """Escreva aqui em baixo a sua solução"""
    return (9/5) * C + 32
while True:
    try:
        C = float(input("Insira a temperatura em graus Celsius: "))
        break
    except ValueError:
        print("Insira uma temperatura válida!")
F = transformar_para_fahrenheit(C)
print(f"Essa temperatura é de {int(F)} Fahrenheit")
