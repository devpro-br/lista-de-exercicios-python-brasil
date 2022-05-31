"""
Exercício 05 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que converta metros para centímetros.

    >>> from secao_01_estrutura_sequencial import ex_05_metros_para_centimetros
    >>> ex_05_metros_para_centimetros.input = lambda k: '1'
    >>> ex_05_metros_para_centimetros.converter_metros_para_centrimetros()
    Transformando para centímetros dá 100.0 cm
    >>> ex_05_metros_para_centimetros.input = lambda k: '3.621'
    >>> ex_05_metros_para_centimetros.converter_metros_para_centrimetros()
    Transformando para centímetros dá 362.1 cm

"""
# conversão feita do m vezes 100
def conversao (m):
    return 100* m

  
    # imput pedindo a quantidade de metros
    print ('Transformando para centímetros dá: {(conversao (m))}cm')
    # o 'f' do inicio garante a formatação usada, a conversao 'def' precisa 
    # estar entre chaves e o : .1f limita as casas decimais para apenas uma, arredondando as que sobram.

def converter_metros_para_centrimetros():
    """Escreva aqui em baixo a sua solução"""
    m = float(input('Digite a quantidade de metros para conversão:'))
    print(f'Transformando para centímetros dá{(conversao (m)): .1f} cm')


