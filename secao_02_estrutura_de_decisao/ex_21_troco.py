"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    
    # notas_de_100_str = notas_de_50_str = notas_de_10_str = notas_de_5_str = notas_de_1_str = ' '
    # notas_de_100 = notas_de_50 = notas_de_10 = notas_de_5 = notas_de_1 = 0
    # notas_de_100, valor = divmod(valor, 100)
    # notas_de_50, valor = divmod(valor, 50)
    # notas_de_10, valor = divmod(valor, 10)
    # notas_de_5, valor = divmod(valor, 5)
    # notas_de_1, valor = divmod(valor, 1)

    # partes_numericas = 0
    # # print("'", end='')
    
    # if notas_de_100 == 1:
    #     notas_de_100_str == '1 nota de R$ 100'
    #     # print(f'{notas_de_100} {notas_de_100_str} ', end='')
    #     partes_numericas += 1
    # elif notas_de_100 > 1:
    #     notas_de_100_str == f'{notas_de_100} notas de R$ 100'
    #     # print(f'{notas_de_100} notas de R$ 100 ', end='')
    #     partes_numericas += 1



    # if notas_de_50 == 1:
    #     notas_de_50_str == '1 nota de R$ 50'
    #     # print(f'{notas_de_50} nota de R$ 50, ', end='')
    #     partes_numericas += 1
    # elif notas_de_50 > 1:
    #     notas_de_50_str == f'{notas_de_50} notas de R$ 50'
    #         # print(f'{notas_de_50} notas de R$ 50, ', end='')
    #     partes_numericas += 1


    # if notas_de_10 == 1:
    #     notas_de_10_str == '1 nota de R$ 10'
    #     # print(f'{notas_de_10} nota de R$ 10, ', end='')
    #     partes_numericas += 1
    # elif notas_de_10 > 1:
    #     notas_de_10_str == 'f{notas_de_10} notas de R$ 10'
    #     # print(f'{notas_de_10} notas de R$ 10, ', end='')
    #     partes_numericas += 1


    # if notas_de_5 == 1:
    #     notas_de_5_str == '1 nota de R$ 5'
    #     # print(f'{notas_de_5} nota de R$ 5, ', end='')
    #     partes_numericas += 1
    # elif notas_de_5 > 1:
    #     notas_de_5_str == f'{notas_de_5} notas de R$ 1'
    #     # print(f'{notas_de_5} notas de R$ 1, ', end='')
    #     partes_numericas += 1


    # if notas_de_1 == 1:
    #     notas_de_1_str == '1 notas de R$ 1'
    #     # print(f'{notas_de_1} nota de R$ 1', end='')
    #     partes_numericas += 1
    # elif notas_de_1 > 1:
    #     notas_de_1_str == f'{notas_de_1} notas de R$ 1'
    #     # print(f'{notas_de_1} notas de R$ 1', end='')
    #     partes_numericas += 1
    
    
    # if partes_numericas == 1:
    #     if notas_de_100_str != ' ':
    #         print(f"'{notas_de_100_str}'")
    #     elif notas_de_50_str != ' ':
    #         print(f"'{notas_de_50_str}'")
    #     elif notas_de_10_str != ' ':
    #         print(f"'{notas_de_10_str}'")
    #     elif notas_de_5_str != ' ':
    #         print(f"'{notas_de_5_str}'")
    #     elif notas_de_1_str != ' ':
    #         print(f"'{notas_de_1_str}'")
    # elif partes_numericas == 5:
    #         print(f"'{notas_de_100_str}, {notas_de_50_str}, {notas_de_10_str}, {notas_de_5_str} e {notas_de_1_str}'")

    # elif partes_numericas == 2:
    #     if notas_de_10_str != ' ' and notas_de_1_str != ' ':
    #         print(f"'{notas_de_10_str} e {notas_de_1_str}'")
        
    # elif partes_numericas == 4:
    #     print(f"'{notas_de_100_str}, {notas_de_50_str}, {notas_de_5_str} e {notas_de_1_str}'")
        
    
    # notas_de_100_str = notas_de_50_str = notas_de_10_str = notas_de_5_str = notas_de_1_str = ' '
    
    
    # saque = valor
    notas_100 = notas_50 = notas_10 = nota_5 = nota_1 = 0
    notas_100, valor = divmod(valor,100)
    notas_50, valor = divmod(valor,50)
    notas_10, valor = divmod(valor,10)
    nota_5, valor = divmod(valor,5)
    nota_1, valor = divmod(valor,1)
    parte = 0
    print("""'""",end="")
    
    if notas_100 == 1:
        print(f"""{notas_100} nota de R$ 100""",end="")
        parte += 1
    elif notas_100 > 1:
        print(f"""{notas_100} notas de R$ 100""",end="")
        parte += 1    
    

    if notas_50 != 0 and parte == 1:
        print(",",end=" ")
    if notas_50 == 1:
        print(f"""{notas_50} nota de R$ 50""",end="")
        parte += 1
    elif notas_50 > 1:
        print(f"""{notas_50} notas de R$ 50""",end="")
        parte += 1
   

    if parte != 0 and notas_10 != 0:
        print(",",end=" ")
    if notas_10 == 1:
        print(f"""{notas_10} nota de R$ 10""",end="")
        parte += 1
    elif notas_10 > 1:
        print(f"""{notas_10} notas de R$ 10""",end="")
        parte += 1
    
    # notas de 5

    if parte != 0 and nota_5 != 0:
        print(",",end=" ")
    if nota_5 == 1:
        print(f"""{nota_5} nota de R$ 5""",end="")
        parte += 1
    elif nota_5 > 1:
        print(f"""{nota_5} notas de R$ 5""",end="")
        parte += 1
    
    # notas de 1

    if parte != 0 and nota_1 != 0:
        print(" e",end=" ")
    if nota_1 == 1:
        print(f"""{nota_1} nota de R$ 1""",end="")
    elif notas_10 > 1:
        print(f"""{nota_1} notas de R$ 1""",end="")
    print("""'""")
        
# def calcular_troco(valor: int) -> str:
#     """Escreva aqui em baixo a sua solução"""
    
#     valor = valor
#     cem_str = cinquenta_str = dez_str = cinco_str = um_str = ' '
#     partes_numericas = 0
#     if saque <= 600:
#         cem, numero_sobrando = divmod(saque, 100)
#         if cem == 1:
#             cem_str = '1 nota de R$ 100'
#             partes_numericas += 1
#         elif cem > 1:
#             cem_str = f'{cem} notas de R$ 100'
#             partes_numericas += 1


#         #Atualiza o número que sobra

#         cinquenta, numero_sobrando = divmod(numero_sobrando, 50)
#         if cinquenta == 1:
#             cinquenta_str = '1 nota de R$ 50'
#             partes_numericas += 1
#         elif cinquenta > 1:
#             cinquenta_str = f'{cinquenta} notas de R$ 50'
#             partes_numericas += 1

#         #Atualiza o número que sobra

#         dez, numero_sobrando = divmod(numero_sobrando, 10)
#         if dez == 1:
#             dez_str = '1 nota de R$ 10'
#             partes_numericas += 1
#         elif dez > 1:
#             dez_str = f'{dez} notas de R$ 10'
#             partes_numericas += 1

#         cinco, numero_sobrando = divmod(numero_sobrando, 5)
#         if cinco == 1:
#             cinco_str = '1 nota de R$ 5'
#             partes_numericas += 1
#         elif cinco > 1:
#             cinco_str = f'{cinco} notas de R$ 5'
#             partes_numericas += 1

#         #Atualiza o número que sobra

#         if numero_sobrando == 1:
#             um_str = '1 nota de R$ 1'
#             partes_numericas += 1
#         elif numero_sobrando > 1:
#             um_str = f'{numero_sobrando} notas de R$ 1'
#             partes_numericas += 1


#         if partes_numericas == 1:
#             if cem_str != ' ':
#                 print(f"'{cem_str}'")
#             elif cinquenta_str != ' ':
#                 print(f"'{cinquenta_str}'")
#             elif dez_str != ' ':
#                 print(f"'{dez_str}'")
#             elif cinco_str != ' ':
#                 print(f"'{cinco_str}'")
#             elif um_str != ' ':
#                 print(f"'{um_str}'")
#         elif partes_numericas == 5:
#             print(f"'{cem_str}, {cinquenta_str}, {dez_str}, {cinco_str} e {um_str}'")

#         elif partes_numericas == 2:
#             if dez_str != ' ' and um_str != ' ':
#                 print(f"'{dez_str} e {um_str}'")
        
#         elif partes_numericas == 4:
#             print(f"'{cem_str}, {cinquenta_str}, {cinco_str} e {um_str}'")