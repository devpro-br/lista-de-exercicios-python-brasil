"""
Exercício 13 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.

    >>> calcular_dia_da_semana(1)
    'Domingo'
    >>> calcular_dia_da_semana(2)
    'Segunda'
    >>> calcular_dia_da_semana(3)
    'Terça'
    >>> calcular_dia_da_semana(4)
    'Quarta'
    >>> calcular_dia_da_semana(5)
    'Quinta'
    >>> calcular_dia_da_semana(6)
    'Sexta'
    >>> calcular_dia_da_semana(7)
    'Sábado'
    >>> calcular_dia_da_semana(8)
    'Dia Inválido'
    >>> calcular_dia_da_semana(0)
    'Dia Inválido'

"""


def calcular_dia_da_semana(dia: int):
    try:
    
        #dia = int(input('Digite um número entre 1 e 7: '))
          
          
        if  dia < 1 or dia >7:
            print("'Dia Inválido'")

        elif dia == 1:
            print("'Domingo'")
        elif dia == 2:
            print("'Segunda'")
        elif dia == 3:
            print("'Terça'")
        elif dia == 4:
            print("'Quarta'")
        elif dia == 5:
            print("'Quinta'")
        elif dia == 6:
            print("'Sexta'")
        elif dia == 7:
            print("'Sábado'")
            
    except ValueError:
        print('Dia Inválido')
