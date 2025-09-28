"""
Exercício 19 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, 
e informe-o expresso no formato horas:minutos:segundos.

    >>> from secao_01_estrutura_sequencial import ex_19_conversao_de_tempo
    >>> ex_19_conversao_de_tempo.input = lambda k: '556'
    >>> ex_19_conversao_de_tempo.converter_tempo()
    0:9:16
    >>> ex_19_conversao_de_tempo.input = lambda k: '1'
    >>> ex_19_conversao_de_tempo.converter_tempo()
    0:0:1
    >>> ex_19_conversao_de_tempo.input = lambda k: '140153'
    >>> ex_19_conversao_de_tempo.converter_tempo()
    38:55:53

"""

def converter_tempo():
    """Escreva aqui em baixo a sua solução"""
    segundos = int(input())
    horas = segundos // 3600
    segundos_restantes = segundos % 3600

    minutos = segundos_restantes // 60
    segundos_finais = segundos_restantes % 60
    print(f"{horas}:{minutos:02}:{segundos_finais:02}")

if __name__ == "__main__":
    converter_tempo()