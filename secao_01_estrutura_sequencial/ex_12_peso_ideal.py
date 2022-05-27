"""
Exercício 12 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte
fórmula: (72.7*altura) - 58
Mostrar a área com 1 casa decimal.

    >>> from secao_01_estrutura_sequencial import ex_12_peso_ideal
    >>> ex_12_peso_ideal.input = lambda k: '1.62'
    >>> ex_12_peso_ideal.calcular_peso_ideal()
    Seu peso ideal é 59.8 kg
    >>> ex_12_peso_ideal.input = lambda k: '1.80'
    >>> ex_12_peso_ideal.calcular_peso_ideal()
    Seu peso ideal é 72.9 kg

"""


def calcular_peso_ideal():
    """Escreva aqui em baixo a sua solução"""
    altura = float(input("Digite sua altura atual: "))
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é {peso_ideal:.1f} kg")
