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


def calcular_tempo_de_download(tam_MB, velo_Mbps):
    #tam_MB = int(input('Informe o tamanho do arquivo MB: '))
    #velo_Mbps = int(input('Informe a velocidade em Mbps: '))

    #tempo_down_minutos = math.ceil((tam_MB /(velo_Mbps/8))/60)
    tam_MB = int(tam_MB)
    velo_Mbps = int(velo_Mbps)
    tempo_down_minutos = ((tam_MB /(velo_Mbps/8))/60)
    print(f'O tempo aproximado do Download é: {tempo_down_minutos:.0f} minuto(s)')
   

