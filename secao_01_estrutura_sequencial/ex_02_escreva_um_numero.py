"""
Exercício 02 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

    >>> from secao_01_estrutura_sequencial import ex_02_escreva_um_numero
    >>> ex_02_escreva_um_numero.input = lambda k: '42'
    >>> ex_02_escreva_um_numero.escreva_um_numero()
    O número informado foi 42

"""

def escreva_um_numero():
    """Escreva aqui em baixo a sua solução"""
    n = input("Digite um número: ")
    print("O número informado foi "+(n))
