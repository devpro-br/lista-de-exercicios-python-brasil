"""
Exercício 20 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno
e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.

    >>> calcular_status(10, 4, 10)
    'Aprovado'
    >>> calcular_status(0, 10, 0)
    'Reprovado'
    >>> calcular_status(5, 8, 0)
    'Reprovado'
    >>> calcular_status(10, 10, 10)
    'Aprovado com Distinção'
"""
def calcular_status(nota_1, nota_2, nota_3):
    """Escreva aqui em baixo a sua solução"""
    media = (nota_1 + nota_2 + nota_3)/3
    if media == 10:
        print("'Aprovado com Distinção'")
    elif media >= 7:
        print("'Aprovado'")
    else:
        print("'Reprovado'")