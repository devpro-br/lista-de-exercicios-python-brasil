"""
Exercício 05 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que converta metros para centímetros.

    
    Entrada:
      1
    Saída:
      Transformando para centímetros dá 100.0 cm
    Entrada:
      3.621
    Saída: 
       Transformando para centímetros dá 362.1 cm

"""


def converter_metros_para_centimetros(metro):
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
    test(converter_metros_para_centimetros, 1, "Transformando para centímetros dá 100.0 cm")
    test(converter_metros_para_centimetros, 3.621, "Transformando para centímetros dá 362.1 cm")
