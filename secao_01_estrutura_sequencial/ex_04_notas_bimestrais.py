"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

    >>> from secao_01_estrutura_sequencial import ex_04_notas_bimestrais
    >>> numeros =['7', '8','9','10']
    >>> ex_04_notas_bimestrais.input = lambda k: numeros.pop()
    >>> ex_04_notas_bimestrais.calcular_media()
    A média anual é 8.5

"""


def calcular_media(notas):
    """Escreva aqui em baixo a sua solução"""
    return sum(notas) / len(notas)

while True:
    try:
        n1 = float(input("Insira a nota do primeiro bimestre: "))
        n2 = float(input("Insira a nota do segundo bimestre: "))
        n3 = float(input("Insira a nota do terceiro bimestre: "))
        n4 = float(input("Insira a nota do quarto bimestre: "))
        break
    except ValueError:
        print("Insira notas válidas!")

notas = [n1, n2, n3, n4]
media = calcular_media(notas)
print(f"A média anual é {media:.1f}")


