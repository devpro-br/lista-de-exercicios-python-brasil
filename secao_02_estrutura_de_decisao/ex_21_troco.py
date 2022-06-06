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
def quantas_notas( lista_qnt_nota: list,valor:int, nota:int):
    if valor >= nota:
        lista_qnt_nota.append(f"{valor // nota} nota")
        if valor // nota > 1:
            lista_qnt_nota[-1] += 's'
        lista_qnt_nota[-1] += f' de R$ {nota}'
        valor = valor % nota
    return valor



def calcular_troco(valor: int):
    """Escreva aqui em baixo a sua solução"""
<<<<<<< HEAD

    lista_qnt_nota = []
    valor = quantas_notas(lista_qnt_nota, valor, 100)
    valor = quantas_notas(lista_qnt_nota, valor, 50)
    valor = quantas_notas(lista_qnt_nota, valor, 10)
    valor = quantas_notas(lista_qnt_nota, valor, 5)
    valor = quantas_notas(lista_qnt_nota, valor, 1)

    if len(lista_qnt_nota) == 5:
        print(f"'{lista_qnt_nota[0]}, {lista_qnt_nota[1]}, {lista_qnt_nota[2]}, {lista_qnt_nota[3]} e {lista_qnt_nota[4]}'")

    if len(lista_qnt_nota) == 4:
        print(f"'{lista_qnt_nota[0]}, {lista_qnt_nota[1]}, {lista_qnt_nota[2]} e {lista_qnt_nota[3]}'")
    if len(lista_qnt_nota) == 3:
        print(f"'{lista_qnt_nota[0]}, {lista_qnt_nota[1]} e {lista_qnt_nota[2]}'")
    if len(lista_qnt_nota) == 2:
        print(f"'{lista_qnt_nota[0]} e {lista_qnt_nota[1]}'")
    if len(lista_qnt_nota) == 1:
        print(f"'{lista_qnt_nota[0]}'")
=======
>>>>>>> main
