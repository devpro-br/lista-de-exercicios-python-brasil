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
    """Escreva aqui em baixo a sua solução"""

    media = (nota_1 + nota_2) / 2
    
#  Entre 9.0 e 10.0        A
  # Entre 7.5 e 9.0         B
  # Entre 6.0 e 7.5         C
  # Entre 4.0 e 6.0         D
  # Entre 4.0 e zero        E

    if media >= 9.0:
        print(f'Notas: {nota_1:.1f} e {nota_2:.1f}.')
        print(f'Média: {media:.1f}')
        print(f'Conceito: A')
        print(f'Status: APROVADO')

    elif media >= 7.5 and media < 9.0:
        print(f'Notas: {nota_1:.1f} e {nota_2:.1f}.')
        print(f'Média: {media:.1f}')
        print(f'Conceito: B')
        print(f'Status: APROVADO')

    elif media >= 6.0 and media < 7.5 :
        print(f'Notas: {nota_1:.1f} e {nota_2:.1f}.')
        print(f'Média: {media:.1f}')
        print(f'Conceito: C')
        print(f'Status: APROVADO')

    elif media >= 4.0 and media < 6.0  :
        print(f'Notas: {nota_1:.1f} e {nota_2:.1f}.')
        print(f'Média: {media:.1f}')
        print(f'Conceito: D')
        print(f'Status: REPROVADO')

    elif media >= 0 and media < 4.0:
        print(f'Notas: {nota_1:.1f} e {nota_2:.1f}.')
        print(f'Média: {media:.1f}')
        print(f'Conceito: E')
        print(f'Status: REPROVADO')
    
