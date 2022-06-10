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


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    notas = [100, 50, 10, 5, 1]
    qtd_notas = {}
    output = []
    for nota in notas:
        while valor >= nota:
            nota_key = nota
            nota_value = valor // nota
            qtd_notas[nota_key] = nota_value
            valor = valor - (nota * nota_value)

    for qtds in qtd_notas:

        if qtd_notas[qtds] > 0:
            if qtd_notas[qtds] == 1:
                output.append(f'{qtd_notas[qtds]} nota de R$ {qtds}')
                qtd_notas[qtds] = 0
            else:    
                output.append(f'{qtd_notas[qtds]} notas de R$ {qtds}')
                qtd_notas[qtds] = 0

    if len(output) < 2:
        print(f"'{output[0]}'")
    elif len(output) < 3:
        print(f"'{output[0]} e {output[1]}'")
    elif len(output) < 4:
        print(f"'{output[0]}, {output[1]} e {output[2]}'")
    elif len(output) < 5:
        print(f"'{output[0]}, {output[1]}, {output[2]} e {output[3]}'")
    else:
        print(f"'{output[0]}, {output[1]}, {output[2]}, {output[3]} e {output[4]}'")