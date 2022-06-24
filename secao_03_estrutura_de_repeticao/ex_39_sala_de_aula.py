"""
Exercício 39 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o nome do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o nome do aluno mais alto
 e o número do aluno mais baixo, junto com suas alturas.
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162))
    'O maior aluno é o Renzo com 162 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165))
    'O maior aluno é o Clara com 165 cm. O menor aluno é o Renzo com 162 cm'
    >>> calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165), ('Oscar', 199))
    'O maior aluno é o Oscar com 199 cm. O menor aluno é o Renzo com 162 cm'

"""


def calcular_aluno_mais_baixo_e_mais_alto(*alunos) -> str:
    """Escreva aqui em baixo a sua solução"""
    alunos_lista = list(alunos)
    maior = alunos_lista[0][1]
    menor = alunos_lista[0][1]
    aluno_mais_alto = alunos_lista[0][0]
    aluno_mais_baixo = alunos_lista[0][0]
    for aluno in alunos_lista:
        if aluno[1] > maior:
            maior = aluno[1]
            aluno_mais_alto = aluno[0]
        if aluno[1] < menor:
            menor = aluno[1]
            aluno_mais_baixo = aluno[0]

    return f'O maior aluno é o {aluno_mais_alto} com {maior} cm. O menor aluno é o {aluno_mais_baixo} com {menor} cm'