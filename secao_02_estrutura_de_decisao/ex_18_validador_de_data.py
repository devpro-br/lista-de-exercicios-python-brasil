"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    dia, mes, ano = data.split('/') # divide a string e coloca cada pedacinho numa variavel por justaposicao
    
    if int(dia) and int(mes) and int(ano) != '':
        if (int(mes)==1 or int(mes)==3 or int(mes)==5 or int(mes)==7 or int(mes)==8 or int(mes)==10 or int(mes)==12):
            if 0 < int(dia) <= 31:
                valida = True
        elif (int(mes) == 4 or int(mes) == 6 or int(mes) == 9 or int(mes) == 11):
            if 0 < int(dia) <= 30:
                valida = True
        elif int(mes) == 2:
            if int(ano) % 4 == 0 and int(ano) % 100 != 0 or int(ano) % 400 == 0:
                    if int(dia) <= 29:
                        valida = True
            elif int(dia) <= 28:
                valida = True
    else:
        print("'Data inválida'")

        
    if(valida):
        print("'Data válida'")
    else:
        print("'Data inválida'")
 
    
