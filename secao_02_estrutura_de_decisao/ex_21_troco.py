"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
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



def quant_nota(notas: list, valor_saque: int, valor_nota: int) -> int:
    valor = 0
    if valor_saque >= valor_nota:
        notas.append(f'{valor_saque // valor_nota} nota')
        if valor_saque // valor_nota > 1:
            notas[-1] += 's'
        notas[-1] += f' de R$ {valor_nota}'

        valor_saque -= (valor_saque // valor_nota) * valor_nota
    return valor_saque

def calcular_troco(valor: int):
    """Escreva aqui em baixo a sua solução"""
    notas = []
 #---------------------------------------
    valor = quant_nota(notas, valor, 100)
    valor = quant_nota(notas, valor, 50)
    valor = quant_nota(notas, valor, 10)
    valor = quant_nota(notas, valor, 5)
    valor = quant_nota(notas, valor, 1)





    

#--------------------------------------------------
    if len(notas) == 5:
        print(f"'{notas[0]}, {notas[1]}, {notas[2]}, {notas[3]} e {notas[4]}'")
    if len(notas) == 4:
        print(f"'{notas[0]}, {notas[1]}, {notas[2]} e {notas[3]}'")
    if len(notas) == 3:
        print(f"'{notas[0]}, {notas[1]} e {notas[2]}'")
    if len(notas) == 2:
        print(f"'{notas[0]} e {notas[1]}'")
    if len(notas) == 1:
        print(f"'{notas[0]}'")










