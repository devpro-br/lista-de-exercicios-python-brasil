"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça as 4 notas bimestrais e mostre a média.
    numeros =['7', '8','9','10']
    A média anual é 8.5

"""

def calcular_media(nota1, nota2, nota3, nota4):
    """Escreva aqui em baixo a sua solução"""
    return f"A média anual é {(nota1 + nota2 + nota3 + nota4) / 4}"

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(calcular_media, (7, 8, 9, 10), "A média anual é 8.5")
    