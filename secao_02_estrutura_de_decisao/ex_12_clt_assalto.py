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

    percentual_inss = 0.1
    desconto_inss = salario_bruto * percentual_inss

    percentual_sindicato = 0.03
    desconto_sindicato = salario_bruto * percentual_sindicato

    percentual_fgts = 0.11
    desconto_fgts = salario_bruto * percentual_fgts

    faixas_ir = {0: 900, 0.05: 1500, 0.10: 2500}
    percentual_ir = 0.2
    for percentual_progressivo, salario_limite in faixas_ir.items():
        if salario_bruto <= salario_limite:
            percentual_ir = percentual_progressivo
            break

    desconto_ir = salario_bruto * percentual_ir

    descontos_totais = desconto_ir + desconto_sindicato + desconto_inss

    salario_liquido = salario_bruto - descontos_totais

    tamanho_label = len('Salário Bruto: (R$ 100.00 * 160)   ')

    label_salario_bruto = f'Salário Bruto: (R$ {valor_hora:.2f} * {horas_trabalhadas})'
    label_salario_bruto = completar_com_espacos_em_branco(label_salario_bruto, tamanho_label)

    label_ir = f'(-) IR ({percentual_ir:.0%})'
    label_ir = completar_com_espacos_em_branco(label_ir, tamanho_label)

    print(f'{label_salario_bruto}: R$ {salario_bruto:8.2f}')
    print(f'{label_ir}: R$ {desconto_ir:8.2f}')
    print(f'(-) INSS ({percentual_inss:.0%})                     : R$ {desconto_inss:8.2f}')
    print(f'(-) Sindicato ({percentual_sindicato:.0%})                 : R$ {desconto_sindicato:8.2f}')
    print(f'FGTS ({percentual_fgts:.0%})                         : R$ {desconto_fgts:8.2f}')
    print(f'Total de descontos                 : R$ {descontos_totais:8.2f}')
    print(f'Salário Liquido                    : R$ {salario_liquido:8.2f}')


def completar_com_espacos_em_branco(label, tamanho_label):
    return label + (' ' * (tamanho_label - len(label)))
