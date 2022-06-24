"""
    Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e
    no qual a soma das linhas, colunas e diagonais é a mesma.
    Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

    8  3  4
    1  5  9
    6  7  2

    Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
    Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
    Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

    >>> from secao_05_exercicios_funcoes import ex_14_quadro_magico
    >>> ex_14_quadro_magico.quadro_magico(sua_funcao)
    'sua funcao está ok'



"""


def quadro_magico(sua_funcao):
    if callable(sua_funcao):
        linhas_colunas = sua_funcao()
        if sum((linhas_colunas[0][0], linhas_colunas[1][0], linhas_colunas[2][0])) \
                == sum((linhas_colunas[0][1], linhas_colunas[1][1], linhas_colunas[2][1])) \
                == sum((linhas_colunas[0][2], linhas_colunas[1][2], linhas_colunas[2][2])):
            return 'sua funcao está ok'
        else:
            return 'sua funcao está errada'
    else:
            return 'isso não é uma função'


from typing import List

def sua_funcao() -> [List[int], List[int], List[int]]:
    """Escreva aqui em baixo a sua solução"""

