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
    nome, altura = zip(*alunos)
    lista_de_nomes = list(nome)
    lista_de_alturas = list(altura)
    altura_maior_aluno = max(lista_de_alturas)
    altura_menor_aluno = min(lista_de_alturas)
    nome_maior_aluno = lista_de_nomes[lista_de_alturas.index(max(lista_de_alturas))]
    nome_menor_aluno = lista_de_nomes[lista_de_alturas.index(min(lista_de_alturas))]
    print(f"'O maior aluno é o {nome_maior_aluno} com {altura_maior_aluno} cm. O menor aluno é o {nome_menor_aluno} com {altura_menor_aluno} cm'")

calcular_aluno_mais_baixo_e_mais_alto(('Renzo', 162), ('Clara', 165), ('Oscar', 199))