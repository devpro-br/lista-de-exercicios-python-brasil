"""
Exercício 07 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
Mostrar a área com 2 casas decimais.

    
    lado 2
    A área do quadrado com esse lado é: 4.00
    O dobro da aŕea do quadrado é: 8.00
    lado 2.5
    A área do quadrado com esse lado é: 6.25
    O dobro da aŕea do quadrado é: 12.50

"""


def calcular_area_de_quadrado(lado):
    """Escreva aqui em baixo a sua solução"""
    

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(calcular_area_de_quadrado, 2, "A área do quadrado com esse lado é: 4.00\nO dobro da área do quadrado é: 8.00")
    test(calcular_area_de_quadrado, 2.5, "A área do quadrado com esse lado é: 6.25\nO dobro da área do quadrado é: 12.50")
