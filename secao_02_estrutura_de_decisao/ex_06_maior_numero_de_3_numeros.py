"""
Exercício 06 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior deles.

    >>> calcular_maior_de_3_numeros(2,3, 5)
    5
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    -1
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    3
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    15
"""


def calcular_maior_de_3_numeros(x, y, z):
    while True:
        try:
            numero1 = 0
            numero2 = 0
            numero3 = 0
            maior = 0
            while numero1 == numero2 == numero3:
                numero1 = int(input('Entre com o primeiro número: '))
                numero2 = int(input('Entre com o segundo número: '))
                numero3 = int(input('Entre com o terceiro número: '))
            
          
            if numero1 >= numero2:
                maior = numero1
            if numero2 >= numero1:
                maior = numero2
            if numero3 >= maior:
                maior = numero3
             
            print(maior)   
            break        
        except ValueError:
            #print('Digite um número!!')
            break
                   
