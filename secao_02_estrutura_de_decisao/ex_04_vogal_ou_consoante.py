"""
Exercício 04 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

    >>> vogal_ou_consoante("F")
    'consoante'
    >>> vogal_ou_consoante("a")
    'vogal'
    >>> vogal_ou_consoante('c')
    'consoante'
    >>> vogal_ou_consoante('U')
    'vogal'
"""


def vogal_ou_consoante(letra):
    
    while True:

        #letra = input("Digite uma letra: ").lower()    
        letra = letra.lower()        

        if letra in vogais:
        
            #print(f'A letra {letra} é uma vogal')
            print("'vogal'")
            
        elif letra in consoantes:
            
             #print(f'A letra {letra} é uma consoante')
            print("'consoante'")
        
        break
