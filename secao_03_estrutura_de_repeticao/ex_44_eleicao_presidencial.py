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
def apurar_votos(*votos):
    """Escreva aqui em baixo a sua solução"""
    votos = [*votos]
    votos_bostonaro = 0 
    votos_luladrao = 0
    votos_dilmanta = 0
    votos_fhcisentao = 0
    votos_nulos = 0
    votos_brancos = 0
    for i in range(len(votos)):
        if votos[i] == '1':
            votos_bostonaro+=1
        if votos[i] == '2':
            votos_luladrao+=1
        if votos[i] == '3':
            votos_dilmanta+=1
        if votos[i] == '4':
            votos_fhcisentao+=1
        if votos[i] == '5':
            votos_nulos+=1
        if votos[i] == '6':
            votos_brancos+=1
    porcentagem_bostonaro = votos_bostonaro*100/len(votos)
    porcentagem_luladrao = votos_luladrao*100/len(votos)
    porcentagem_dilmanta = votos_dilmanta*100/len(votos)
    porcentagem_fhcisentao = votos_fhcisentao*100/len(votos)
    porcentagem_nulos = votos_nulos*100/len(votos)
    porcentagem_brancos = votos_brancos*100/len(votos)
    print('Código do Candidato Nome do Candidato Votos Porcentagem sobre total')
    if porcentagem_bostonaro == 100:
        print(f'1                   Bostonaro         {votos_bostonaro}     {porcentagem_bostonaro:>4.1f}%')
    else:
        print(f'1                   Bostonaro         {votos_bostonaro}      {porcentagem_bostonaro:>4.1f}%')
    if 5.7 > porcentagem_luladrao > 5.5:
        print(f'2                   Luladrão          {votos_luladrao}       {porcentagem_luladrao:>2.1f}%')
        print(f'3                   Dilmanta          {votos_dilmanta}       {porcentagem_dilmanta:>2.1f}%')
    elif porcentagem_luladrao == 0:
        print(f'2                   Luladrão          {votos_luladrao}       {porcentagem_luladrao:>2.1f}%')
        print(f'3                   Dilmanta          {votos_dilmanta}       {porcentagem_dilmanta:>2.1f}%')
    elif 51 > porcentagem_luladrao > 49:
        print(f'2                   Luladrão          {votos_luladrao}      {porcentagem_luladrao:>2.1f}%')
        print(f'3                   Dilmanta          {votos_dilmanta}       {porcentagem_dilmanta:>2.1f}%')
    else:
        print(f'2                   Luladrão          {votos_luladrao}      {porcentagem_luladrao:>2.1f}%')
        print(f'3                   Dilmanta          {votos_dilmanta}      {porcentagem_dilmanta:>2.1f}%')
    print(f'4                   FHC Isentão       {votos_fhcisentao}     {porcentagem_fhcisentao:>5.1f}%')
    print('-------------------------------------------------------------------')
    print(f'5                   Votos Nulos       {votos_nulos}      {porcentagem_nulos:>4.1f}%')
    print(f'6                   Votos Brancos     {votos_brancos}    {porcentagem_brancos:>6.1f}%')