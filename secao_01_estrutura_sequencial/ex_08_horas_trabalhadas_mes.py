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
    Seu salário desse mês é 4449.60

"""


def calcular_salario():
    while True:
        try:
            valor_hora = float(input('Informe o valor recebido por hora trabalhada: R$ '))
            total_hora_mes = int(input('Informe a quantidade de horas trabalhadas no mês: '))
            salario = valor_hora * total_hora_mes
            print(f'Seu salário desse mês é {salario:.2f}')
            
        except ValueError:
            print('Informe um valor válido!!!')
            break
