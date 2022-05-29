"""
Exercício 06 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. Mostrar a área com 4 casas decimais.
Observação: Use o valor de 3.1415 para o valor da constante π

    >>> from secao_01_estrutura_sequencial import ex_06_area_circulo
    >>> ex_06_area_circulo.input = lambda k: '1'
    >>> ex_06_area_circulo.calcular_area_de_circulo()
    A área do círculo com esse raio é: 3.1415
    >>> ex_06_area_circulo.input = lambda k: '2.5'
    >>> ex_06_area_circulo.calcular_area_de_circulo()
    A área do círculo com esse raio é: 19.6344

"""
def calcular_area_de_circulo():
    """Escreva aqui em baixo a sua solução"""
    raio_circulo = float(input('Digite o raio do círculo em metros: '))
    pi = 3.1415
    area_circulo = 3.1415 * raio_circulo**2
    print(f'A área do círculo com esse raio é: {area_circulo:.4f}')