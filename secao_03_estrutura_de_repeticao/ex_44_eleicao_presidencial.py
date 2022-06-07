"""
Exercício 44 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:

O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.


    >>> apurar_votos('1')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1     100.0%
    2                   Luladrão          0       0.0%
    3                   Dilmanta          0       0.0%
    4                   FHC Isentão       0       0.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      50.0%
    2                   Luladrão          1      50.0%
    3                   Dilmanta          0       0.0%
    4                   FHC Isentão       0       0.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      33.3%
    2                   Luladrão          1      33.3%
    3                   Dilmanta          1      33.3%
    4                   FHC Isentão       0       0.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3', '4')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      25.0%
    2                   Luladrão          1      25.0%
    3                   Dilmanta          1      25.0%
    4                   FHC Isentão       1      25.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       0       0.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3', '4', '5')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      20.0%
    2                   Luladrão          1      20.0%
    3                   Dilmanta          1      20.0%
    4                   FHC Isentão       1      20.0%
    -------------------------------------------------------------------
    5                   Votos Nulos       1      20.0%
    6                   Votos Brancos     0       0.0%
    >>> apurar_votos('1', '2', '3', '4', '5', '6')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1      16.7%
    2                   Luladrão          1      16.7%
    3                   Dilmanta          1      16.7%
    4                   FHC Isentão       1      16.7%
    -------------------------------------------------------------------
    5                   Votos Nulos       1      16.7%
    6                   Votos Brancos     1      16.7%
    >>> apurar_votos('1', '2', '3', '4', '5', '6', '5', '6', '5', '6', '5', '6', '5', '6', '5', '6', '5', '6')
    Código do Candidato Nome do Candidato Votos Porcentagem sobre total
    1                   Bostonaro         1       5.6%
    2                   Luladrão          1       5.6%
    3                   Dilmanta          1       5.6%
    4                   FHC Isentão       1       5.6%
    -------------------------------------------------------------------
    5                   Votos Nulos       7      38.9%
    6                   Votos Brancos     7      38.9%


"""
from collections import Counter


def apurar_votos(*votos):
    """Escreva aqui em baixo a sua solução"""
    contador = 0
    bolso = 0
    lula = 0
    dilma = 0
    fhc = 0
    nulo = 0
    branco = 0
    while contador < len(votos):
        if votos[contador] == '1':
            bolso = bolso + 1
            contador = contador + 1
        elif votos[contador] == '2':
            lula = lula + 1
            contador = contador + 1
        elif votos[contador] == '3':
            dilma = dilma + 1
            contador = contador + 1
        elif votos[contador] == '4':
            fhc = fhc + 1
            contador = contador + 1
        elif votos[contador] == '5':
            nulo = nulo + 1
            contador = contador + 1
        elif votos[contador] == '6':
            branco = branco + 1
            contador = contador + 1

    total_votos = len(votos)
    porcentagem_bozo = (bolso/total_votos)*100
    porcentagem_lula = (lula/total_votos)*100
    porcentagem_dilma = (dilma/total_votos)*100
    porcentagem_fhc = (fhc/total_votos)*100
    porcentagem_nulo = (nulo/total_votos)*100
    porcentagem_branco = (branco/total_votos)*100
    print('Código do Candidato Nome do Candidato Votos Porcentagem sobre total')
    print('1                   Bostonaro         %.0f     %5.1f'%(bolso,porcentagem_bozo),'%',sep="")
    print('2                   Luladrão          %.0f      %4.1f'%(lula,porcentagem_lula),'%',sep="")
    print('3                   Dilmanta          %.0f      %4.1f'%(dilma,porcentagem_dilma),'%',sep="")
    print('4                   FHC Isentão       %.0f      %4.1f'%(fhc,porcentagem_fhc),'%',sep="")
    print('-------------------------------------------------------------------')
    print('5                   Votos Nulos       %.0f      %4.1f'%(nulo,porcentagem_nulo),'%',sep="")
    print('6                   Votos Brancos     %.0f      %4.1f'%(branco,porcentagem_branco),'%',sep="")
    
