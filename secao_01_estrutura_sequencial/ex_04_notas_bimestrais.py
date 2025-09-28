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

# Utilizando list comprehension
# def calcular_media():
#     """Abordagem funcional com list comprehension"""
#     notas = [float(input(f"Digite a {i+1}º nota: ")) for i in range(4)]
#     media = sum(notas) / len(notas)
#     print(f"A média anual é {media}")

def calcular_media():
    """Escreva aqui em baixo a sua solução"""
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a {i+1}º nota: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    print(media)

calcular_media()

