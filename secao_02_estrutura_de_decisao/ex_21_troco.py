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
    notas_100 = valor // 100
    valor %= 100

    notas_50 = valor // 50
    valor %= 50

    notas_10 = valor // 10
    valor %= 10

    notas_5 = valor // 5
    valor %= 5

    notas_1 = valor

    print("\nNotas fornecidas:")
    if notas_100:
        print(f"{int(notas_100)} nota(s) de R$100")
    if notas_50:
        print(f"{int(notas_50)} nota(s) de R$50")
    if notas_10:
        print(f"{int(notas_10)} nota(s) de R$10")
    if notas_5:
        print(f"{int(notas_5)} nota(s) de R$5")
    if notas_1:
        print(f"{int(notas_1)} nota(s) de R$1")
    
while True:
    try:
        valor_saque = float(input("Valor do saque: R$"))
        
        if 1 <= valor_saque <= 600:
            break
        else:
            print("O valor mínimo é de 1 real e o máximo de 600 reais.")
    except ValueError:
        print("Insira um valor válido!")
calcular_troco(valor_saque)
