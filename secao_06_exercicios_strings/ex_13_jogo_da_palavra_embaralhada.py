"""
Exercício 13 da seção de strings da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Jogo da palavra embaralhada. 
Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. 
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador terá seis tentativas para adivinhar a palavra. 
Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

Importante: use o arquivo "ex_13_lista_palavras.txt" para importar a lista de palavras a ser usada no jogo.

    >>> from secao_06_exercicios_strings import ex_13_jogo_da_palavra_embaralhada
    >>> entradas = ['trocar', 'troca', 'traco', 'ortacr', 'atcorr', 'tranco']
    >>> ex_13_jogo_da_palavra_embaralhada.input = lambda k: entradas.pop()
    >>> import random
    >>> random.seed(1)
    >>> ex_13_jogo_da_palavra_embaralhada.adivinhe_a_palavra()
    A palavra certa é trocar. Você ganhou!
    >>> entradas = ['trocar']
    >>> ex_13_jogo_da_palavra_embaralhada.input = lambda k: entradas.pop()
    >>> import random
    >>> random.seed(1)
    >>> ex_13_jogo_da_palavra_embaralhada.adivinhe_a_palavra()
    A palavra certa é trocar. Você ganhou!
    >>> entradas = ['troco', 'tronco', 'trocos', 'awdewqf', 'a', 'troco']
    >>> ex_13_jogo_da_palavra_embaralhada.input = lambda k: entradas.pop()
    >>> import random
    >>> random.seed(1)
    >>> ex_13_jogo_da_palavra_embaralhada.adivinhe_a_palavra()
    Você perdeu! Usou todas as suas tentativas! A palavra certa era trocar

"""
def adivinhe_a_palavra():
    """Escreva aqui em baixo a sua solução"""