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
    salario = (valor_hora*horas_trabalhadas)
    if salario <= 900:
      #Valores em porcentagem#
      porcentagem_ir = 0
      porcentagem_inss = 10
      porcentagem_sindicato = 3
      porcenteagem_fgts = 11
      #calculos descontos#
      ir = salario*(porcentagem_ir/100)
      inss = salario*(porcentagem_inss/100)
      sindicato = salario*(porcentagem_sindicato/100)
      fgts = salario*(porcenteagem_fgts/100)
      total_descontos = ir+inss+sindicato
      salario_liquido = salario-total_descontos
      #Auxilio do print#
      salario = "{:.2f}".format(salario)
      salario = str(salario)
      ir = "{:.2f}".format(ir)
      ir = str(ir)
      inss = "{:.2f}".format(inss)
      inss = str(inss)
      sindicato = "{:.2f}".format(sindicato)
      sindicato = str(sindicato)
      fgts = "{:.2f}".format(fgts)
      fgts = str(fgts)
      total_descontos = "{:.2f}".format(total_descontos)
      total_descontos = str(total_descontos)
      salario_liquido = "{:.2f}".format(salario_liquido)
      salario_liquido = str(salario_liquido)
      print('Salário Bruto: (R$ ','%.2f' % valor_hora,' * ', horas_trabalhadas,')     : R$', salario.rjust(9,' '), sep='')
      print('(-) IR (','%.0f' %porcentagem_ir,'%)                        : R$', ir.rjust(9,' '), sep='')
      print('(-) INSS (','%.0f'%porcentagem_inss,'%)                     : R$', inss.rjust(9,' '), sep='')
      print('(-) Sindicato (','%.0f'%porcentagem_sindicato,'%)                 : R$', sindicato.rjust(9,' '), sep='')
      print('FGTS (','%.0f'%porcenteagem_fgts,'%)                         : R$', fgts.rjust(9,' '), sep='')
      print('Total de descontos                 : R$', total_descontos.rjust(9,' '), sep='')
      print('Salário Liquido                    : R$', salario_liquido.rjust(9,' '), sep='')
    elif salario <= 1500:
      #Valores em porcentagem#
      porcentagem_ir = 5
      porcentagem_inss = 10
      porcentagem_sindicato = 3
      porcenteagem_fgts = 11
      #calculos descontos#
      ir = salario*(porcentagem_ir/100)
      inss = salario*(porcentagem_inss/100)
      sindicato = salario*(porcentagem_sindicato/100)
      fgts = salario*(porcenteagem_fgts/100)
      total_descontos = ir+inss+sindicato
      salario_liquido = salario-total_descontos
      #Auxilio do print#
      salario = "{:.2f}".format(salario)
      salario = str(salario)
      ir = "{:.2f}".format(ir)
      ir = str(ir)
      inss = "{:.2f}".format(inss)
      inss = str(inss)
      sindicato = "{:.2f}".format(sindicato)
      sindicato = str(sindicato)
      fgts = "{:.2f}".format(fgts)
      fgts = str(fgts)
      total_descontos = "{:.2f}".format(total_descontos)
      total_descontos = str(total_descontos)
      salario_liquido = "{:.2f}".format(salario_liquido)
      salario_liquido = str(salario_liquido)
      print('Salário Bruto: (R$ ','%.2f' % valor_hora,' * ', horas_trabalhadas,')     : R$', salario.rjust(9,' '), sep='')
      print('(-) IR (','%.0f' %porcentagem_ir,'%)                        : R$', ir.rjust(9,' '), sep='')
      print('(-) INSS (','%.0f'%porcentagem_inss,'%)                     : R$', inss.rjust(9,' '), sep='')
      print('(-) Sindicato (','%.0f'%porcentagem_sindicato,'%)                 : R$', sindicato.rjust(9,' '), sep='')
      print('FGTS (','%.0f'%porcenteagem_fgts,'%)                         : R$', fgts.rjust(9,' '), sep='')
      print('Total de descontos                 : R$', total_descontos.rjust(9,' '), sep='')
      print('Salário Liquido                    : R$', salario_liquido.rjust(9,' '), sep='')
    elif salario <= 2500:
      #Valores em porcentagem#
      porcentagem_ir = 10
      porcentagem_inss = 10
      porcentagem_sindicato = 3
      porcenteagem_fgts = 11
      #calculos descontos#
      ir = salario*(porcentagem_ir/100)
      inss = salario*(porcentagem_inss/100)
      sindicato = salario*(porcentagem_sindicato/100)
      fgts = salario*(porcenteagem_fgts/100)
      total_descontos = ir+inss+sindicato
      salario_liquido = salario-total_descontos
      #Auxilio do print#
      salario = "{:.2f}".format(salario)
      salario = str(salario)
      ir = "{:.2f}".format(ir)
      ir = str(ir)
      inss = "{:.2f}".format(inss)
      inss = str(inss)
      sindicato = "{:.2f}".format(sindicato)
      sindicato = str(sindicato)
      fgts = "{:.2f}".format(fgts)
      fgts = str(fgts)
      total_descontos = "{:.2f}".format(total_descontos)
      total_descontos = str(total_descontos)
      salario_liquido = "{:.2f}".format(salario_liquido)
      salario_liquido = str(salario_liquido)
      print('Salário Bruto: (R$ ','%.2f' % valor_hora,' * ', horas_trabalhadas,')    : R$', salario.rjust(9,' '), sep='')
      print('(-) IR (','%.0f' %porcentagem_ir,'%)                       : R$', ir.rjust(9,' '), sep='')
      print('(-) INSS (','%.0f'%porcentagem_inss,'%)                     : R$', inss.rjust(9,' '), sep='')
      print('(-) Sindicato (','%.0f'%porcentagem_sindicato,'%)                 : R$', sindicato.rjust(9,' '), sep='')
      print('FGTS (','%.0f'%porcenteagem_fgts,'%)                         : R$', fgts.rjust(9,' '), sep='')
      print('Total de descontos                 : R$', total_descontos.rjust(9,' '), sep='')
      print('Salário Liquido                    : R$', salario_liquido.rjust(9,' '), sep='')
    elif salario > 2500:
      #Valores em porcentagem#
      porcentagem_ir = 20
      porcentagem_inss = 10
      porcentagem_sindicato = 3
      porcenteagem_fgts = 11
      #calculos descontos#
      ir = salario*(porcentagem_ir/100)
      inss = salario*(porcentagem_inss/100)
      sindicato = salario*(porcentagem_sindicato/100)
      fgts = salario*(porcenteagem_fgts/100)
      total_descontos = ir+inss+sindicato
      salario_liquido = salario-total_descontos
      #Auxilio do print#
      salario = "{:.2f}".format(salario)
      salario = str(salario)
      ir = "{:.2f}".format(ir)
      ir = str(ir)
      inss = "{:.2f}".format(inss)
      inss = str(inss)
      sindicato = "{:.2f}".format(sindicato)
      sindicato = str(sindicato)
      fgts = "{:.2f}".format(fgts)
      fgts = str(fgts)
      total_descontos = "{:.2f}".format(total_descontos)
      total_descontos = str(total_descontos)
      salario_liquido = "{:.2f}".format(salario_liquido)
      salario_liquido = str(salario_liquido)
      print('Salário Bruto: (R$ ','%.2f' % valor_hora,' * ', horas_trabalhadas,')   : R$', salario.rjust(9,' '), sep='')
      print('(-) IR (','%.0f' %porcentagem_ir,'%)                       : R$', ir.rjust(9,' '), sep='')
      print('(-) INSS (','%.0f'%porcentagem_inss,'%)                     : R$', inss.rjust(9,' '), sep='')
      print('(-) Sindicato (','%.0f'%porcentagem_sindicato,'%)                 : R$', sindicato.rjust(9,' '), sep='')
      print('FGTS (','%.0f'%porcenteagem_fgts,'%)                         : R$', fgts.rjust(9,' '), sep='')
      print('Total de descontos                 : R$', total_descontos.rjust(9,' '), sep='')
      print('Salário Liquido                    : R$', salario_liquido.rjust(9,' '), sep='')