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


def imprima_a_soma_de_dois_numeros(x, y):
    """Escreva aqui em baixo a sua solução"""
    return print(f"A soma dos dois números informados é {x+y}")
    
while True:
    try:
        num1 = int(input("Insira um número inteiro: "))
        num2 = int(input("Insira outro número inteiro: "))
        break
            
    except ValueError:
            print("Insira um número inteiro válido")
imprima_a_soma_de_dois_numeros(num1, num2)