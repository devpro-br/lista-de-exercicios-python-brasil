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
    if len(data) >= 8:
        day, month, year = data.split('/')
        day = int(day.lstrip('0'))
        month = int(month.lstrip('0'))
        year = int(year)
        if day in range(1, 29) and month in range(1, 12) and year in range(1, 9999):
            return 'Data válida'
        return 'Data inválida'
    return 'Data inválida'
    
    

        
    #     if month > 12:
    #         return f'Data inválida'
    #     if year > 9999 and year < 0000:
    #         return f'Data inválida'
    # else:
    #     return f'Data inválida'
    

            
            
        



    

    

    

    








    