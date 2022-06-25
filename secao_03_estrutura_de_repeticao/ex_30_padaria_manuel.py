"""
Exercício 30 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um
sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1
até 50 pães, a partir do preço do pão informado pelo usuário

    >>> gerar_tabela_de_precos(1.99)
    Preço do pão: R$  1.99
    Panificadora Pão de Ontem - Tabela de preços
    1  - R$   1.99
    2  - R$   3.98
    3  - R$   5.97
    4  - R$   7.96
    5  - R$   9.95
    6  - R$  11.94
    7  - R$  13.93
    8  - R$  15.92
    9  - R$  17.91
    10 - R$  19.90
    11 - R$  21.89
    12 - R$  23.88
    13 - R$  25.87
    14 - R$  27.86
    15 - R$  29.85
    16 - R$  31.84
    17 - R$  33.83
    18 - R$  35.82
    19 - R$  37.81
    20 - R$  39.80
    21 - R$  41.79
    22 - R$  43.78
    23 - R$  45.77
    24 - R$  47.76
    25 - R$  49.75
    26 - R$  51.74
    27 - R$  53.73
    28 - R$  55.72
    29 - R$  57.71
    30 - R$  59.70
    31 - R$  61.69
    32 - R$  63.68
    33 - R$  65.67
    34 - R$  67.66
    35 - R$  69.65
    36 - R$  71.64
    37 - R$  73.63
    38 - R$  75.62
    39 - R$  77.61
    40 - R$  79.60
    41 - R$  81.59
    42 - R$  83.58
    43 - R$  85.57
    44 - R$  87.56
    45 - R$  89.55
    46 - R$  91.54
    47 - R$  93.53
    48 - R$  95.52
    49 - R$  97.51
    50 - R$  99.50
    >>> gerar_tabela_de_precos(2.97)
    Preço do pão: R$  2.97
    Panificadora Pão de Ontem - Tabela de preços
    1  - R$   2.97
    2  - R$   5.94
    3  - R$   8.91
    4  - R$  11.88
    5  - R$  14.85
    6  - R$  17.82
    7  - R$  20.79
    8  - R$  23.76
    9  - R$  26.73
    10 - R$  29.70
    11 - R$  32.67
    12 - R$  35.64
    13 - R$  38.61
    14 - R$  41.58
    15 - R$  44.55
    16 - R$  47.52
    17 - R$  50.49
    18 - R$  53.46
    19 - R$  56.43
    20 - R$  59.40
    21 - R$  62.37
    22 - R$  65.34
    23 - R$  68.31
    24 - R$  71.28
    25 - R$  74.25
    26 - R$  77.22
    27 - R$  80.19
    28 - R$  83.16
    29 - R$  86.13
    30 - R$  89.10
    31 - R$  92.07
    32 - R$  95.04
    33 - R$  98.01
    34 - R$ 100.98
    35 - R$ 103.95
    36 - R$ 106.92
    37 - R$ 109.89
    38 - R$ 112.86
    39 - R$ 115.83
    40 - R$ 118.80
    41 - R$ 121.77
    42 - R$ 124.74
    43 - R$ 127.71
    44 - R$ 130.68
    45 - R$ 133.65
    46 - R$ 136.62
    47 - R$ 139.59
    48 - R$ 142.56
    49 - R$ 145.53
    50 - R$ 148.50


"""


def gerar_tabela_de_precos(preco_por_pao: float):
    """Escreva aqui em baixo a sua solução"""
