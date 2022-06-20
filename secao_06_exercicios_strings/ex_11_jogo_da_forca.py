"""
Exercício 11 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador poderá errar 6 vezes antes de ser enforcado.

Dica de frase:
'É uma linguagem de programação muito famosa, muito utilizada para automatização de tarefas'

    >>> adivinhar_frase()
    Que pena, você errou todas.

     >>> adivinhar_frase(['P'],['Y'],['T'],['H'])
     Você errou pela 2ª vez, tente novamente.

    >>> adivinhar_frase (['P'],['Y'],['H'],['O'],['N'])
    Que pena, você errou 6 vezes, mas quase acertou.
    Seu chute foi:
      P  Y      H  O  N
     -- --  -- -- -- --
    >>> adivinhar_frase(['P'],['Y'],['T'],['H'],['O'],['N'])
    Parabéns, você acertou a frase secreta.
    a frase secreta é:
      P  Y  T  H  O  N
     -- -- -- -- -- --

"""


def adivinhar_frase(*letras):
    """Escreva aqui em baixo a sua solução"""
