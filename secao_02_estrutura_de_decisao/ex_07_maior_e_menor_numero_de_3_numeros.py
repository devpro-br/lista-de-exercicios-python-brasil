"""
Exercício 07 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre o maior e o menor deles.

    >>> calcular_maior_de_3_numeros(2,3, 5)
    Maior: 5
    Menor: 2
    >>> calcular_maior_de_3_numeros(-1, -10, -2)
    Maior: -1
    Menor: -10
    >>> calcular_maior_de_3_numeros(-5, 3, 0)
    Maior: 3
    Menor: -5
    >>> calcular_maior_de_3_numeros(7, -14, 15)
    Maior: 15
    Menor: -14
"""


def calcular_maior_de_3_numeros(x, y, z):
    while True:
        try:
            numero1 = 0
            numero2 = 0
            numero3 = 0
            maior = 0
            menor = 0
            while numero1 == numero2 == numero3:
                numero1 = int(input('Entre com o primeiro número: '))
                numero2 = int(input('Entre com o segundo número: '))
                numero3 = int(input('Entre com o terceiro número: '))
                num_01 = numero1
                num_02 = numero2
                num_03 = numero3
                
                
            if numero1 >= numero2:
                maior = numero1
            if numero2 >= numero1:
                maior = numero2          
            if numero3 >= maior:
                maior = numero3
                
            
            if num_01 <= num_02:
                menor = num_01
            if num_02 <= num_01:
                menor = num_02
            if num_03 <= menor:
                menor = num_03
            
           
            print(f'Maior: {maior}')
            print(f'Menor: {menor}')
            break               
        except ValueError:
            #print('Digite um número!!')
            break
