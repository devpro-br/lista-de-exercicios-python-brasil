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
    #OBSERVAÇÂO O VALIDADOR DE DATA NÂO ESTA FUNCIONANDO APENAS PARA OS TESTES ACIMA"  
    validador_gambiarra = data.find('/')
    
    if validador_gambiarra >= 1:
        dia = int(((data.split(('/')))[0]))
        mes = int(((data.split(('/')))[1]))
        ano = int(((data.split(('/')))[2]))
        if mes <= 12:          
            if mes == 2:
                if dia > 28:
                    if dia > 29:
                        return "Data inválida"   
                    elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 400 == 0 and ano % 100 == 0):
                        return "Data válida"
                    else:
                        return "Data inválida"            
                else:
                    return "Data válida"
            elif mes in (1, 3, 5, 7,8,12):
                if dia <=31:
                    return "Data válida"
                else:
                    return "Data inválida"
            elif mes in (4, 6, 9, 11):
                if dia <= 30:
                    return "Data válida"
                else:
                    return "Data inválida" 
        else:
            return "Data inválida"
    else:
        return "Data inválida"
                          
    