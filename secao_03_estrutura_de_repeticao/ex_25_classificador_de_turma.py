"""
Exercício 25 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma
varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
calculada.

Mostre a média de idade com uma casa decimal.

    >>> classifcar_turma(20)
    'A turma é jovem, pois a média é de 20.0 anos'
    >>> classifcar_turma(20, 30)
    'A turma é jovem, pois a média é de 25.0 anos'
    >>> classifcar_turma(20, 30, 95)
    'A turma é adulta, pois a média é de 48.3 anos'
    >>> classifcar_turma(20, 30, 95, 95)
    'A turma é idosa, pois a média é de 60.0 anos'
    >>> classifcar_turma(20, 30, 95, 95, 95)
    'A turma é idosa, pois a média é de 67.0 anos'

"""


def classifcar_turma(*idades) -> str:
    """Escreva aqui em baixo a sua solução"""
