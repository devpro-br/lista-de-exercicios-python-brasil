"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""




from math import floor


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    if valor >= 1 and valor <=600:
        if valor < 10:
            notas_de_5 = floor(valor / 5)
            notas_de_1 = valor % 5
            if valor < 5:
                return str(notas_de_1) + ' ' + 'nota de R$ 1'                
            elif valor == 5:
                return str(notas_de_5) + ' ' + 'nota de R$ 5'
            elif valor == 6:
                return str(notas_de_1) + ' ' + 'nota de R$ 5' + ' ' + str(notas_de_1) + ' ' + 'nota de R$ 1'
            else:
                return str(notas_de_1) + ' ' + 'nota de R$ 5' + ' ' + str(notas_de_1) + ' ' + 'notas de R$ 1'
        elif valor == 10:
            notas_de_10 = floor(valor/10)
            return str(notas_de_10) + ' ' + 'nota de R$ 10'        
        elif valor > 10 and valor < 50 and valor not in [11, 21, 31, 41]:
            notas_de_10 = floor(valor/10)
            notas_de_5 = floor(valor % 10)/5
            notas_de_1 = notas_de_5 % 5
            if notas_de_5 >= 1 and notas_de_1 == 1 and notas_de_10 == 1: #
                return  str(notas_de_10) + ' ' + 'nota de R$ 10' + ' ' + 'e' + ' ' + str(notas_de_1) + ' ' + 'nota de R$ 5' + ' ' + 'e' + ' ' + str(notas_de_1) + ' ' + 'nota de R$ 1'
            elif notas_de_5 == 5: 
                return  str(notas_de_10) + ' ' + 'nota de R$ 10' + ' ' + 'e' + ' ' + str(notas_de_1) + ' ' + 'nota de R$ 5'
            elif notas_de_10 == 1 and notas_de_5 >=1:
                return  str(notas_de_10) + ' ' + 'nota de R$ 10' + ' ' + 'e' + ' ' + str(notas_de_1) + ' ' + 'nota de R$ 5' + ' ' + 'e' + ' ' + str(notas_de_1) + ' ' + 'notas   de R$ 1'
        elif valor == 11:
            notas_de_10 = floor(valor/10)
            notas_de_5 = valor % 10
            notas_de_1 = notas_de_5 % 5
            return str(notas_de_10) + ' ' + 'nota de R$ 10' + ' ' + 'e' + ' ' + str(notas_de_1) + ' ' + 'nota de R$ 1'
        elif valor >= 100:
            notas_de_100 = floor(valor / 100)
            notas_de_50 = floor((valor%100)/50)
            notas_de_10 = floor(((valor%100)-50)/10)
            notas_de_5 = floor((valor-(notas_de_100*100)-(notas_de_50*50)-(notas_de_10*10))/5)
            notas_de_1 = (valor-(notas_de_100*100)-(notas_de_50*50)-(notas_de_10*10)-(notas_de_5*5))
            if notas_de_50 == 1 and notas_de_10 > 1 and notas_de_5 == 1 and notas_de_1 > 1:
                return str(notas_de_100) + ' notas de R$ 100, ' + str(notas_de_50) + ' nota de R$ 50, ' + str(notas_de_10) + ' notas de R$ 10, ' + str(notas_de_5) + ' nota de R$ 5 e ' + str(notas_de_1) + ' notas de R$ 1'
            else:
                return str(notas_de_100) + ' notas de R$ 100, ' + str(notas_de_50) + ' nota de R$ 50, ' + str(notas_de_5) + ' nota de R$ 5 e ' + str(notas_de_1) + ' nota de R$ 1'



            
        #elif valor in [21, 31, 41]:
        #    notas_de_10 = floor(valor/10)
        #    notas_de_5 = valor % 10
        #    notas_de_1 = notas_de_5 % 5
        #    return str(notas_de_10) + ' ' + 'notas de R$ 10' + ' ' + 'e' + ' ' + str(notas_de_1) + ' ' + 'nota de R$ 1'
        
        
            
              

