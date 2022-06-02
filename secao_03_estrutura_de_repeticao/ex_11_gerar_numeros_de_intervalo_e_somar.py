"""
Exercício 11 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao


Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido.
Também mostre a soma dos números da sequência.

    >>> calcular_numeros_no_intervalo_e_somar(1, 10)
    'Sequência: 1, 2, 3, 4, 5, 6, 7, 8, 9. Soma: 45'
    >>> calcular_numeros_no_intervalo_e_somar(-10, -1)
    'Sequência: -10, -9, -8, -7, -6, -5, -4, -3, -2. Soma: -54'
    >>> calcular_numeros_no_intervalo_e_somar(-1, -10)
    'Sequência: vazia. Soma: 0'

"""


def calcular_numeros_no_intervalo_e_somar(inicio: int, fim: int) -> str:
    """Escreva aqui em baixo a sua solução"""

    auxilio = inicio
    soma = 0
    print("'Sequência: ",sep='',end='')
    while inicio <= auxilio < fim: 
        soma = soma + auxilio
        if auxilio != (fim - 1):
            print(auxilio, end=', ')
            auxilio = auxilio + 1
            continue
        else:
            print(auxilio, end='. ')            
            print("Soma: %.0f'"%soma)
            break
    else:
        print("vazia. Soma: %.0f'"%soma,sep='',end='')
