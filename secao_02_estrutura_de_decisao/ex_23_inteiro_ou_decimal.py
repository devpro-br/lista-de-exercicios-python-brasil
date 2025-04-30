"""
Exercício 23 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento.

    >>> decidir_se_eh_inteiro_ou_decimal('256')
    'Inteiro'
    >>> decidir_se_eh_inteiro_ou_decimal('1.0')
    'Inteiro'
    >>> decidir_se_eh_inteiro_ou_decimal('2.0000')
    'Inteiro'
    >>> decidir_se_eh_inteiro_ou_decimal('2.00001')
    'Decimal'
    >>> decidir_se_eh_inteiro_ou_decimal('11.2')
    'Decimal'
    >>> decidir_se_eh_inteiro_ou_decimal('3.1415')
    'Decimal'
"""


def decidir_se_eh_inteiro_ou_decimal(valor: str) -> str:
    """Determina se o número informado é inteiro ou decimal."""
    try:
        numero = float(valor)
        arredondado = round(numero)
        if numero == arredondado:
            return "Inteiro"
        else:
            return "Decimal"
    except ValueError:
        return "Entrada inválida."

valor = input("Insira um valor: ")
print(decidir_se_eh_inteiro_ou_decimal(valor))

