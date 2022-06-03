"""
Exercício 26 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

uma eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar
 e ao final mostrar o número de votos de cada candidato.

    >>> calcular_votos()
    Votantes: 0
    Votos no candidato corrupto: 0
    Votos no candidato mentiroso: 0
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto')
    Votantes: 1
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 0
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto', 'mentiroso')
    Votantes: 2
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 1
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto', 'mentiroso', 'rouba, mas faz')
    Votantes: 3
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 1
    Votos no candidato rouba, mas faz: 1
    >>> calcular_votos('corrupto', 'mentiroso', 'rouba, mas faz', 'corrupto', 'mentiroso', 'rouba, mas faz')
    Votantes: 6
    Votos no candidato corrupto: 2
    Votos no candidato mentiroso: 2
    Votos no candidato rouba, mas faz: 2

"""


def calcular_votos(*votos):
    """Escreva aqui em baixo a sua solução"""
    contador = 0
    corrupto = 0
    mentiroso = 0
    rouba = 0
    invalido = 0
    while contador < len(votos):
        if votos[contador] == 'corrupto':
            corrupto = corrupto + 1
            contador = contador + 1
        elif votos[contador] == 'mentiroso':
            mentiroso = mentiroso + 1
            contador = contador + 1
        elif votos[contador] == 'rouba, mas faz':
            rouba = rouba + 1
            contador = contador + 1
        else:
            invalido = invalido + 1
            contador = contador + 1

    print('Votantes: %.0f'% len(votos))
    print('Votos no candidato corrupto: %.0f'%corrupto)
    print('Votos no candidato mentiroso: %.0f'%mentiroso)
    print('Votos no candidato rouba, mas faz: %.0f'%rouba)
        

