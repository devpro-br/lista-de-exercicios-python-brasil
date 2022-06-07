"""
Exercício 24 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

A partir de uma simulação de lançamento de dados 
foram armazenados os valores de cada lançamento.
Mostre quantas vezes cada valor foi conseguido.

    >>> lancar_dados(2, 2, 2, 5, 3, 3, 1, 3, 4, 2, 6, 4, 3, 4, 4, 2, 6, 3, 6, 3, 4,
    ... 3, 5, 5, 5, 1, 2, 1, 6, 5, 6, 3, 1, 6, 1, 1, 6, 5, 1, 6, 1, 1, 2, 1, 1, 2, 2,
    ... 4, 4, 4, 2, 1, 4, 6, 6, 4, 2, 4, 4, 2, 5, 3, 6, 1, 2, 5, 4, 4, 5, 3, 4, 6, 6, 
    ... 6, 2, 4, 1, 5, 2, 5, 6, 5, 2, 5, 1, 4, 1, 1, 3, 6, 1, 5, 3, 1, 2, 6, 6, 5, 4, 
    ... 2)
    O número 1 caiu 19 vezes
    O número 2 caiu 18 vezes
    O número 3 caiu 12 vezes
    O número 4 caiu 18 vezes
    O número 5 caiu 15 vezes
    O número 6 caiu 18 vezes

    >>> lancar_dados(6, 6, 2, 5, 4, 5, 3, 3, 5, 1, 1, 4, 5, 4, 4, 2, 4, 6, 3, 6, 1,
    ... 6, 6, 6, 6, 5, 5, 6, 6, 3, 5, 5, 1, 5, 5, 5, 2, 6, 4, 5, 5, 1, 3, 2, 3, 3,
    ... 6, 3, 4, 3, 4, 1, 5, 6, 3, 1, 1, 2, 2, 2, 4, 4, 6, 3, 1, 2, 6, 2, 5, 2, 2,
    ... 2, 2, 3, 2, 1, 3, 5, 3, 4, 5, 6, 3, 5, 2, 2, 3, 5, 6, 1, 4, 2, 3, 1, 3, 6, 
    ... 5, 3, 2, 5)
    O número 1 caiu 12 vezes
    O número 2 caiu 18 vezes
    O número 3 caiu 19 vezes
    O número 4 caiu 12 vezes
    O número 5 caiu 21 vezes
    O número 6 caiu 18 vezes

"""


def lancar_dados(*valor_lancamentos):
    """Escreva aqui em baixo a sua solução"""
    lista = sorted(valor_lancamentos)
    lista_quantidades = []
    i = 0
    valor = 0

    lados_do_dado = 6
    for lado in range(lados_do_dado):
        while i < len(lista) and lista[i] == lado+1:
            i += 1
            valor += 1
        lista_quantidades.append(valor)
        valor = 0
        print(f'O número {lado + 1} caiu {lista_quantidades[lado]} vezes')
        lado += 1