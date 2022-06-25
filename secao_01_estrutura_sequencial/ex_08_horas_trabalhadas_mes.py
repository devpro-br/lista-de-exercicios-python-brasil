"""
Exercício 08 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
Mostrar salário com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_08_horas_trabalhadas_mes
    >>> numeros =['80', '55.62']
    >>> ex_08_horas_trabalhadas_mes.input = lambda k: numeros.pop()
    >>> ex_08_horas_trabalhadas_mes.calcular_salario()
    Seu salário este mês foi de 4449.60 reais

"""


def calcular_salario():
    """Escreva aqui em baixo a sua solução"""

    valor_hora = float(input('Valor da hora em Reais: '))
    horas_trabalhadas = int(input('Quantas horas trabalhadas? '))
    salario = valor_hora * horas_trabalhadas
    print(f'Seu salário este mês foi de {salario:.2f} reais')