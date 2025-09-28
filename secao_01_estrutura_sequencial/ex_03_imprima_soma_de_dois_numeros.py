"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça dois números inteiros e imprima a soma.

    >>> from secao_01_estrutura_sequencial import ex_03_imprima_soma_de_dois_numeros
    >>> numeros =['42', '43']
    >>> ex_03_imprima_soma_de_dois_numeros.input = lambda k: numeros.pop()
    >>> ex_03_imprima_soma_de_dois_numeros.imprima_a_soma_de_dois_numeros()
    A soma dos dois números informados é 85

"""


def imprima_a_soma_de_dois_numeros():
    """Escreva aqui em baixo a sua solução"""
    # try:
    #     primeiro_numero = int(input("Digite o primeiro numero: "))
    #     segundo_numero = int(input("Digite o segundo numero: "))
    #     soma = primeiro_numero + segundo_numero
    #     print(f"A soma dos dois números informados é {soma}")
    # except ValueError:
    #     print("Erro: Digite apenas números inteiros")
    primeiro_numero = int(input("Digite o primeiro numero: "))
    segundo_numero = int(input("Digite o segundo numero: "))
    soma = primeiro_numero + segundo_numero
    print(f"A soma dos dois números informados é {soma}")

if __name__ == "__main__":
    imprima_a_soma_de_dois_numeros()

