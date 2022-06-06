"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def substitui_ultimo(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

def trata_string(numero, unidade):
    retorno = ''
    if numero == 1:
        retorno = f'1 nota de R$ {unidade}'
    elif numero > 1:
        retorno = f'{numero} notas de R$ {unidade}'
    return retorno


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    # 1, 5, 10, 50 e 100 reais

    valor_aux = valor
    notas_100, valor_aux = divmod(valor_aux, 100)
    notas_50, valor_aux = divmod(valor_aux, 50)
    notas_10, valor_aux = divmod(valor_aux, 10)
    notas_5, valor_aux = divmod(valor_aux, 5)
    notas_1, valor_aux = divmod(valor_aux, 1)

    result_array = [notas_100, notas_50, notas_10, notas_5, notas_1]
    notas_array = ['100', '50', '10', '5', '1']
    result_string = ''


    for i in range(len(result_array)):
        nota = result_array[i]
        if (nota) is not None and nota > 0:
            result_string += trata_string(result_array[i], notas_array[i])
            if i < 4 and sum(result_array) > 1:
                result_string += ', '


    result_string = substitui_ultimo(result_string, ', ', ' e ', 1)
    print(f"'{result_string}'")
