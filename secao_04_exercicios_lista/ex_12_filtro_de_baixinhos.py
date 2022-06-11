"""
Exercício 12 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Foram anotados os nomes, as idades e alturas de de vários alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses
alunos.

Mostre a média com uma casa decimal.

    >>> calcular_baixinhos_com_mais_de_13_anos(('Renzo', 39, 162))
    Média de altura: 162.0 centímetros.
    Não há nenhum aluno abaixo da média
    >>> calcular_baixinhos_com_mais_de_13_anos(('Renzo', 39, 162), ('Priscila', 33, 158))
    Média de altura: 160.0 centímetros.
    Existe(m) 1 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Priscila, com 158 centímetros e 33 ano(s) de idade
    >>> calcular_baixinhos_com_mais_de_13_anos(('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210))
    Média de altura: 176.7 centímetros.
    Existe(m) 2 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Renzo, com 162 centímetros e 39 ano(s) de idade
    2. Priscila, com 158 centímetros e 33 ano(s) de idade
    >>> calcular_baixinhos_com_mais_de_13_anos(
    ...     ('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210), ('Criança', 7, 100)
    ... )
    Média de altura: 157.5 centímetros.
    Não há nenhum aluno abaixo da média
    >>> calcular_baixinhos_com_mais_de_13_anos(
    ...     ('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210),
    ...     ('Criança', 7, 100), ("Shaquille O'Neal", 25, 216)
    ... )
    Média de altura: 169.2 centímetros.
    Existe(m) 2 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Renzo, com 162 centímetros e 39 ano(s) de idade
    2. Priscila, com 158 centímetros e 33 ano(s) de idade

"""
from statistics import mean


def calcular_baixinhos_com_mais_de_13_anos(*alunos):
    """Escreva aqui em baixo a sua solução"""
    alunos = [*alunos]
    nome, idade, altura = zip(*alunos)
    media_de_altura = mean(altura)
    alunos_abaixo_da_media = 0
    lista_alunos_abaixo_da_media = []
    for aluno in alunos:
        if aluno[1] <= 13:
            alunos.remove(aluno)
        if aluno[1] > 13 and aluno[2] < media_de_altura:
            alunos_abaixo_da_media+=1
            lista_alunos_abaixo_da_media.append(aluno[0:3])
    print(f'Média de altura: {media_de_altura:.1f} centímetros.')
    if alunos_abaixo_da_media > 0:
        print(f'Existe(m) {alunos_abaixo_da_media} aluno(s) com altura abaixo da média com mais de 13 anos:')
        nome, idade, altura = zip(*lista_alunos_abaixo_da_media)
        i = 1
        j = 0
        for aluno in lista_alunos_abaixo_da_media:
            print(f'{i}. {nome[j]}, com {altura[j]} centímetros e {idade[j]} ano(s) de idade')
            i+=1
            j+=1
    else:
        print('Não há nenhum aluno abaixo da média')