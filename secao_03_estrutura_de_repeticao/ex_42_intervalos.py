"""
Exercício 42 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.

    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-1, 10, 15, 20, 50, 13, 78, 22, 14, 16]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    7 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[14, -5, 10, 2, 80, 99]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    2 número(s) entre o intervalo de zero a 25
    2 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[-55, 144, 5, 32, 18, 43, 12, 26, 76]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    3 número(s) entre o intervalo de zero a 25
    3 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 76 a 100
    >>> from secao_03_estrutura_de_repeticao import  ex_42_intervalos
    >>> numeros_para_avaliacao=[3, 5, 100, -5, 70, 88, 28, 12]
    >>> ex_42_intervalos.input = lambda k: numeros_para_avaliacao.pop()
    >>> ex_42_intervalos.listar_numeros_para_avaliacao()
    1 número(s) entre o intervalo de zero a 25
    1 número(s) entre o intervalo de 26 a 50
    1 número(s) entre o intervalo de 51 a 75
    1 número(s) entre o intervalo de 76 a 100

"""


def listar_numeros_para_avaliacao():
    """Escreva aqui em baixo a sua solução"""
    numeros=[]    
    numeros.append((input('Insira um numero entre 0 e 100')))
    numeros_zero_a_25 = 0
    numeros_26_a_50 = 0
    numeros_51_a_75 = 0
    numeros_76_a_100 = 0
    while numeros[0] >= 0:
        if numeros[0] > 0 and numeros[0] <= 25:
            numeros_zero_a_25 += 1
        elif numeros[0] > 25 and numeros[0] <= 50:
            numeros_26_a_50 += 1
        elif numeros[0] > 50 and numeros[0] <= 75:
            numeros_51_a_75 += 1
        elif numeros[0] > 75 and numeros[0] <= 100:
            numeros_76_a_100 += 1
        
        numeros.insert(0,(int(input('Insira um numero entre 0 e 100'))))
    if numeros_zero_a_25 >= 1:
        print('%.0f número(s) entre o intervalo de zero a 25'%numeros_zero_a_25)
    if numeros_26_a_50 >= 1:   
        print('%.0f número(s) entre o intervalo de 26 a 50'%numeros_26_a_50)
    if numeros_51_a_75 >= 1:
        print('%.0f número(s) entre o intervalo de 51 a 75'%numeros_51_a_75)
    if numeros_76_a_100 >= 1:
     print('%.0f número(s) entre o intervalo de 76 a 100'%numeros_76_a_100)
