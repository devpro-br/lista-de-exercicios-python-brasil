"""
Exercício 08 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.

    >>> from secao_04_exercicios_lista import ex_08_imprimir_idade_altura

    >>> ex_08_imprimir_idade_altura.inverter_idade_altura()
    ''

    >>> idade_altura = [25, 175, 25, 185, 22, 110, 27, 171, 155]
    >>> ex_08_imprimir_idade_altura.input = lambda k: idade_altura.pop()
    >>> ex_08_imprimir_idade_altura.inverter_idade_altura()
    É necessário informar cinco idades. 

     >>> idade_altura = [25, 175, 25, 22, 110, 27, 171, 23, 155]
    >>> ex_08_imprimir_idade_altura.input = lambda k: idade_altura.pop()
    >>> ex_08_imprimir_idade_altura.inverter_idade_altura()
    É necessário informar cinco alturas.

    >>> idade_altura = [25, 175, 25, 185, 22, 110, 27, 171, 23, 155]
    >>> ex_08_imprimir_idade_altura.input = lambda k: idade_altura.pop()
    >>> ex_08_imprimir_idade_altura.inverter_idade_altura()
    idade   altura
    23      155
    27      171
    22      110
    25      185
    25      175

    >>> idade_altura = [5, 100, 25, 185, 105, 162, 77, 151, 23, 155]
    >>> ex_08_imprimir_idade_altura.input = lambda k: idade_altura.pop()
    >>> ex_08_imprimir_idade_altura.inverter_idade_altura()
    idade   altura
    23      155
    77      151
    105     162
    25      185
    5       100
    
"""

def inverter_idade_altura():
    """Escreva aqui em baixo a sua solução"""
