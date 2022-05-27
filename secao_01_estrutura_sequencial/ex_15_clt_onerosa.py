"""
Exercício 15 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido
Mostrar os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_15_clt_onerosa
    >>> numeros =['80', '55.62']
    >>> ex_15_clt_onerosa.input = lambda k: numeros.pop()
    >>> ex_15_clt_onerosa.calcular_assalto_no_salario()
    + Salário Bruto : 4449.60
    - IR (11%) : R$ 489.46
    - INSS (8%) : R$ 355.97
    - Sindicato ( 5%) : R$ 222.48
    = Salário Liquido : R$ 3381.70

"""


def calcular_assalto_no_salario():
    """Escreva aqui em baixo a sua solução"""
    valor = float(input("Quanto vale sua hora de trabalho? "))
    horas = float(input("Quantas horas você trabalhou este mês? "))
    
    salario_bruto = valor * horas
    imposto_renda = (11 / 100) * salario_bruto
    inss = (8 / 100) * salario_bruto
    sindicato = (5 / 100) * salario_bruto
    liquido = salario_bruto - (imposto_renda + inss + sindicato)
    print(f"+ Salário Bruto : {salario_bruto:.2f}\n- IR (11%) : R$ {imposto_renda:.2f}")
    print(f"- INSS (8%) : R$ {inss:.2f}\n- Sindicato ( 5%) : R$ {sindicato:.2f}\n= Salário Liquido : R$ {liquido:.2f}")
