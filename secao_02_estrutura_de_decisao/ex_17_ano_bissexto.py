"""
Exercício 17 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não
bissexto.
    >>> eh_ano_bissexto(400)
    True
    >>> eh_ano_bissexto(800)
    True
    >>> eh_ano_bissexto(2100)
    False
    >>> eh_ano_bissexto(2004)
    True
    >>> eh_ano_bissexto(2022)
    False

"""


def eh_ano_bissexto(ano: int):
    
    import calendar

    try:
        
     
        ano = int(input("Digite o ano que deseja consultar se é bissexto: "))        

        quatro = ano % 4
        cem = ano % 100
        quatrocentos = ano % 400
                
        mensagem = calendar.isleap(ano)
                
                
        print(mensagem)
               
    except ValueError:
        print('Entrada inválida!!!')    

