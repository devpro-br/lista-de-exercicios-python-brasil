"""
Exercício 01 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosFuncoes

Faça um programa para imprimir:

  1
  2   2
  3   3   3
  .....
  n   n   n   n   n   n  ... n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

"""
def imprimir_linhas(n):
    """Escreva aqui em baixo a sua solução"""
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end=' ')

        print()

imprimir_linhas(7)