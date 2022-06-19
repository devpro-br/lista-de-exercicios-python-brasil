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
    while True:
    try:
        ano_str = "11111"
        while len(ano_str) != 4:
            ano = int(input("Digite o ano que deseja consultar se é bissexto: "))
            ano_str = str(ano)
            # Só segue adiante recebendo 4 digitos. recebendo letras cai em ValueError.
     

        quatro = ano % 4
        cem = ano % 100
        quatrocentos = ano % 400
                
        # primeira situação
        if quatro == 0:
            if cem != 0:  
                mensagem = "bissexto"
            else:
                mensagem = "Não é bissexto"
                
        #segunda situação    
        if quatro != 0:
            if quatrocentos == 0: 
                mensagem = "bissexto"
            else:
                mensagem = "Não é bissexto"
            
        #terceira condição
        if quatro != 0:
            if quatrocentos == 0:
                mensagem = "bissexto"
            else:
                mensagem = "Não é bissexto"
        print(mensagem)
        
    except ValueError:
        print('Entrada inválida!!!')
