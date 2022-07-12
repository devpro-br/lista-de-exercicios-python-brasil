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
    def alinha_saida_valores_no_print(numero: float, num_caracteres: int):
        ''' Resulta em alinhamento das colunas de impressão de valores com número
            de caracteres diferente. Retornando uma string do tamanho indicado em
            num_caracters.
        '''
        
        num_str = str(numero)
        tamanho = len(num_str)
        posicao = 0
        inteiro = ''

        while posicao < tamanho and num_str[posicao] != '.':
            inteiro += num_str[posicao]
            posicao += 1      
            
        if posicao == tamanho:
            num_str += '.00'
        
        elif posicao == tamanho - 2:
            num_str += '0'
        
        elif num_str[posicao] == '.' and tamanho - posicao - 1 >= 2:
            num_str = inteiro + num_str[posicao] + num_str[posicao + 1] + num_str[posicao + 2]       
           
     
        num_espacos = num_caracteres - posicao
        num_espacos_str = ' ' * num_espacos

        saida = num_espacos_str + num_str  
        return saida

    def alinha_a_direita(dado: str, num_caracteres: int):
        ''' Resulta em alinhamento das colunas de impressão de valores com número
            de caracteres diferente. Retornando uma string do tamanho indicado em
            num_caracters.
        '''
        
        tamanho = len(dado)
        inteiro = ''

        num_espacos = num_caracteres - tamanho
        num_espacos_str = ' ' * num_espacos
        alinhado = num_espacos_str + dado  
        return alinhado



    valor_hora = float(input('Entre com o valor da hora: '))
    quant_hora = int(input('Entrer com a quantidade de horas trabalhadas: '))

    salario_bruto = valor_hora * quant_hora

    if salario_bruto <= 900:
        ir = 0
        ir_por = '0'
    elif salario_bruto <= 1500:
        ir = (salario_bruto * .05)
        ir_por = '5'
    elif salario_bruto <= 2500:
        ir = (salario_bruto * .1)
        ir_por = '10'
    elif salario_bruto > 2500:
        ir = (salario_bruto * .2)
        ir_por = '20'
    inss = salario_bruto * .1
    sindicato = salario_bruto * .03
    fgts = salario_bruto * .11
    total_descontos = ir + inss + sindicato
    salario_liquido = salario_bruto- total_descontos

    inss_alinhado = alinha_saida_valores_no_print(inss, 8)
    sindicato_alinhado = alinha_saida_valores_no_print(sindicato, 8)
    fgts_alinhado =alinha_saida_valores_no_print(fgts, 8)
    total_descontos_alinhado = alinha_saida_valores_no_print(total_descontos, 8)
    salario_liquido_alinhado = alinha_saida_valores_no_print(salario_liquido, 8)
    ir_alinhado = alinha_saida_valores_no_print(ir, 8)
    salario_bruto_alinhado = alinha_saida_valores_no_print(salario_bruto, 8)
    valor_hora_alinhado = alinha_saida_valores_no_print(valor_hora, 4)
    #ir_por = alinha_a_direita(ir_por, 2)



    print(f'Salário Bruto: (R$ {valor_hora_alinhado} * {quant_hora})     : R$ {salario_bruto_alinhado}')
    if ir_por == '0' or ir_por == '5':
        print(f'(-) IR ({ir_por}%)                           : R$ {ir_alinhado}')
    else:
        print(f'(-) IR ({ir_por}%)                          : R$ {ir_alinhado}')
    print(f'(-) INSS ( 10%)                       : R$ {inss_alinhado}')
    print(f'(-) Sindicato (3%)                    : R$ {sindicato_alinhado}')
    print(f'FGTS (11%)                            : R$ {fgts_alinhado}')
    print(f'Total de descontos                    : R$ {total_descontos_alinhado}')
    print(f'Salário Líquido                       : R$ {salario_liquido_alinhado}')

