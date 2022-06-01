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
    sal_bruto = valor_hora * horas_trabalhadas
    fgts = sal_bruto * .11
    inss = sal_bruto * .1
    sindicato = sal_bruto * .03
    ir = 0

    if sal_bruto <= 900.0:
      ir = 0
    elif sal_bruto <= 1500.0:
      ir = .05
    elif sal_bruto <= 2500.0:
      ir = .1
    else:
      ir = .2
    
    descontos = inss+(ir*sal_bruto)+sindicato
    salario_liquido = sal_bruto - descontos

    print(f"Salário Bruto: (R$ {valor_hora:.2f} * {horas_trabalhadas:.0f})".ljust(34), f"{': R$'} {sal_bruto:>8.2f}")
    print(f"(-) IR ({ir*100:.0f}%)".ljust(34), f"{': R$'} {ir*sal_bruto:>8.2f}")
    print(f"(-) INSS (10%)".ljust(34), f"{': R$'} {inss:>8.2f}")
    print(f"(-) Sindicato (3%)".ljust(34), f"{': R$'} {sindicato:>8.2f}")
    print(f"FGTS (11%)".ljust(34), f"{': R$'} {fgts:>8.2f}")
    print(f"Total de descontos".ljust(34), f"{': R$'} {descontos:>8.2f}")
    print(f"Salário Liquido".ljust(34), f"{': R$'} {salario_liquido:>8.2f}")