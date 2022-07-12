"""
Exercício 09 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre-os em ordem decrescente.

    >>> ordenar_decrescente(2, 3, 5)
    5, 3, 2
    >>> ordenar_decrescente(10, 5.55, 7)
    10, 7, 5.55
    >>> ordenar_decrescente(20, 30, 17.62)
    30, 20, 17.62
    >>> ordenar_decrescente(7, 1, 15)
    15, 7, 1

"""


def ordenar_decrescente(x, y, z):
    while True:
        try:
            #print('digite três números que serão apresentados em ordem decrescente.')
            n1 = float(input('Entre com o primeiro número: '))
            n2 = float(input('Entre com o segundo número: '))
            n3 = float(input('Entre com o terceiro número: '))
            
            
            # A seguir, solução que encontrei para atender ao doctest do curso
            # recebia por exemplo:
            # 10, 5.5 e 7 e pedia saida: 10, 7, 5.5
            # sem essa solução a saída seria: 10.0, 7.0, 5.0
            
                    
            if round(n1) == n1:
                n1 = round(n1)
            if round(n2) ==n2:
                n2 = round(n2)
            if round(n3) == n3:
                n3 = round(n3)
                
            
                  
            if n1 < n3:
                n1, n3 =  n3, n1 
            if n1 < n2:
                n1, n2 = n2, n1 
            if n2 < n3:
                n2, n3 = n3, n2
                
           
            print(f'{n1}, {n2}, {n3}')   
            break
        
        except ValueError:
            break
        
            #print('Entrada inválida!!!')        
        
