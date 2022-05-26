"""
Exercício 18 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
Arredonde o tempo em minutos

    >>> from secao_01_estrutura_sequencial import ex_18_tempo_de_download
    >>> numeros =['50', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 7 minuto(s)
    >>> numeros =['100', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 3 minuto(s)

"""


def calcular_tempo_de_download():
    """Escreva aqui em baixo a sua solução"""
    #1º passo: input para tamanho de um arquivo para download (em MB) e velocidade de um link de Internet (em Mbps)
    mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
    mbps = float(input("Digite a velocidade de um link de Internet (em Mbps): "))
    #2º passo: formula calculo tempo de download e conversao para minutos
    tempo_download = mb / (mbps/8)
    conversao_minutos = tempo_download / 60
    #3º passo: imprimir o tempo aproximado do Download ARREDONDADO
    print("O tempo aproximado do Download é:",round(conversao_minutos),"minuto(s)")