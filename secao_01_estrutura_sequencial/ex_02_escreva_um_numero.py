"""
Exercício 02 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
    O número informado foi 42
"""

def escreva_um_numero(numero):
    """Escreva aqui em baixo a sua solução"""

    return f"O número informado foi {numero}"

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
    test(escreva_um_numero, 42, "O número informado foi 42")
    