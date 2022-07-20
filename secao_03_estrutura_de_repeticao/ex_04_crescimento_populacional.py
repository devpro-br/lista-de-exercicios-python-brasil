"""
Exercício 04 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento.

    >>> calcular_ano_ultrapassagem_populacional()
    'População de A, depois de 63 ano(s) será de 515033 pessoas, superando a de B, que será de 510964 pessoas'


"""


def calcular_ano_ultrapassagem_populacional() -> str:
    """Escreva aqui em baixo a sua solução"""
    anos = 0
    pais_a = 80000 
    pais_b = 200000

    porcentos_a = 0.03
    porcentos_b = 0.015

    
    while pais_a < pais_b:
        crescimento_a = pais_a * porcentos_a
        crescimento_b = pais_b * porcentos_b
        pais_a += crescimento_a
        pais_b += crescimento_b        
        anos += 1
    
    print(f"'População de A, depois de {anos} ano(s) será de {pais_a:.0f} pessoas, superando a de B, que será de {pais_b:.0f} pessoas'")
        