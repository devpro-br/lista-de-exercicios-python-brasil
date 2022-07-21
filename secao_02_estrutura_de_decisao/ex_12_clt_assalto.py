"""
Exercício 12 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos
os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
  Salário Bruto até 900 (inclusive) - isento
  Salário Bruto até 1500 (inclusive) - desconto de 5%
  Salário Bruto até 2500 (inclusive) - desconto de 10%
  Salário Bruto acima de 2500 - desconto de 20%

Mostrar valores monetários com duas casas decimais, alinhados à direita, com espaço para 5 dígitos de salário, ou seja,
até R$ 99999,99

    >>> calcular_salario_liquido(1, 160)
    Salário Bruto: (R$ 1.00 * 160)     : R$   160.00
    (-) IR (0%)                        : R$     0.00
    (-) INSS (10%)                     : R$    16.00
    (-) Sindicato (3%)                 : R$     4.80
    FGTS (11%)                         : R$    17.60
    Total de descontos                 : R$    20.80
    Salário Liquido                    : R$   139.20
    >>> calcular_salario_liquido(5, 220)
    Salário Bruto: (R$ 5.00 * 220)     : R$  1100.00
    (-) IR (5%)                        : R$    55.00
    (-) INSS (10%)                     : R$   110.00
    (-) Sindicato (3%)                 : R$    33.00
    FGTS (11%)                         : R$   121.00
    Total de descontos                 : R$   198.00
    Salário Liquido                    : R$   902.00
    >>> calcular_salario_liquido(10, 160)
    Salário Bruto: (R$ 10.00 * 160)    : R$  1600.00
    (-) IR (10%)                       : R$   160.00
    (-) INSS (10%)                     : R$   160.00
    (-) Sindicato (3%)                 : R$    48.00
    FGTS (11%)                         : R$   176.00
    Total de descontos                 : R$   368.00
    Salário Liquido                    : R$  1232.00
    >>> calcular_salario_liquido(100, 160)
    Salário Bruto: (R$ 100.00 * 160)   : R$ 16000.00
    (-) IR (20%)                       : R$  3200.00
    (-) INSS (10%)                     : R$  1600.00
    (-) Sindicato (3%)                 : R$   480.00
    FGTS (11%)                         : R$  1760.00
    Total de descontos                 : R$  5280.00
    Salário Liquido                    : R$ 10720.00

"""


def calcular_salario_liquido(valor_hora: float, horas_trabalhadas: int):
    """Escreva aqui em baixo a sua solução"""
    salario_bruto = valor_hora * horas_trabalhadas
    inss = 10 * salario_bruto / 100
    fgts = 11 * salario_bruto / 100
    sindicato = 3 * salario_bruto / 100
    if salario_bruto <= 900:
        valor_ir = 0
        ir = 0
    elif salario_bruto <= 1500:
        valor_ir = 5 * salario_bruto / 100
        ir = 5
    elif salario_bruto <= 2500:
        valor_ir = 10 * salario_bruto / 100
        ir = 10
    else:
        valor_ir = 20 * salario_bruto / 100
        ir = 20

    total_descontos = valor_ir + inss + sindicato
    salario_liquido = salario_bruto - total_descontos

    # Inteiros transformados em strings para passar rjust() e ljust
    valor = f'{valor_hora: .2f}'
    horas = f'{horas_trabalhadas}'
    linha_sal_bruto = f'Salário Bruto: (R${valor} * {horas})'
    linha_ir = f'(-) IR ({ir}%) '
    s_salario_bruto = f'{salario_bruto:.2f}'
    s_valor_ir = f'{valor_ir:.2f}'
    s_inss = f'{inss:.2f}'
    s_sindicato = f'{sindicato:.2f}'
    s_fgts = f'{fgts:.2f}'
    s_total_descontos = f'{total_descontos:.2f}'
    s_salario_liquido = f'{salario_liquido:.2f}'

    print(
f'''{linha_sal_bruto.ljust(33)}  : R$ {s_salario_bruto.rjust(8)}
{linha_ir.ljust(27)}        : R$ {s_valor_ir.rjust(8)}
(-) INSS (10%)                     : R$ {s_inss.rjust(8)}
(-) Sindicato (3%)                 : R$ {s_sindicato.rjust(8)}
FGTS (11%)                         : R$ {s_fgts.rjust(8)}
Total de descontos                 : R$ {s_total_descontos.rjust(8)}
Salário Liquido                    : R$ {s_salario_liquido.rjust(8)}''')
