"""
Exercício 01 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Tamanho de strings. Faça um programa que compare 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings


    >>> comparar('Brasil Hexa 2006', 'Brasil! Hexa 2006!')
    String 1: Brasil Hexa 2006
    String 2: Brasil! Hexa 2006!
    Tamanho de "Brasil Hexa 2006": 16 caracteres
    Tamanho de "Brasil! Hexa 2006!": 18 caracteres
    As duas strings são de tamanhos diferentes.
    As duas strings possuem conteúdo diferente.
    >>> comparar('Igual', 'Igual')
    String 1: Igual
    String 2: Igual
    Tamanho de "Igual": 5 caracteres
    Tamanho de "Igual": 5 caracteres
    As duas strings possuem  mesmo tamanho.
    As duas strings possuem conteúdo igual.

"""


def comparar(s1: str, s2: str):
    """Escreva aqui em baixo a sua solução"""
