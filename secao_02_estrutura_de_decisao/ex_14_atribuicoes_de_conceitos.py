"""
Exercício 14 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for
A, B ou C ou “REPROVADO” se o conceito for D ou E.05

Mostar valores com uma casa decimal.

    >>> calcular_conceito(10, 9)
    Notas: 10.0 e 9.0.
    Média: 9.5
    Conceito: A
    Status: APROVADO
    >>> calcular_conceito(8.5, 7.5)
    Notas: 8.5 e 7.5.
    Média: 8.0
    Conceito: B
    Status: APROVADO
    >>> calcular_conceito(7, 6)
    Notas: 7.0 e 6.0.
    Média: 6.5
    Conceito: C
    Status: APROVADO
    >>> calcular_conceito(6.2, 4)
    Notas: 6.2 e 4.0.
    Média: 5.1
    Conceito: D
    Status: REPROVADO
    >>> calcular_conceito(2.2, 1.2)
    Notas: 2.2 e 1.2.
    Média: 1.7
    Conceito: E
    Status: REPROVADO

"""


def calcular_conceito(nota_1: float, nota_2: float):
    nota_01 = float(input('Digite a primeira nota: '))
    nota_02 = float(input('Digite a segunda nota: '))
    media = (nota_01 + nota_02)/2
    conceito = 'E'
    condicao = "REPROVADO"

    if 0 >= media < 4:
        conceito = 'E'
        condicao = "REPROVADO"

    elif 4 <= media <6:
        conceito = 'D'
        condicao = "REPROVADO"

    elif 6 <= media < 7.5:
        conceito = 'C'
        condicao = "APROVADO"

    elif 7.5 <= media < 9:
        conceito = 'B'
        condicao = "APROVADO"

    elif 9 <= media:
        conceito = 'A'
        condicao = "APROVADO"

    print(f'Notas: {nota_01:,.1f} e {nota_02:,.1f}.')
    print(f'Média: {media:,.1f}')
    print(f'Conceito: {conceito}')
    print(f'Status: {condicao}')


