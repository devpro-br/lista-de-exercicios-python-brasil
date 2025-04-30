"""
Exercício 04 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

    >>> vogal_ou_consoante("F")
    'consoante'
    >>> vogal_ou_consoante("a")
    'vogal'
    >>> vogal_ou_consoante('c')
    'consoante'
    >>> vogal_ou_consoante('U')
    'vogal'
"""


def vogal_ou_consoante(letra):
    """Escreva aqui em baixo a sua solução"""
    vogais = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'o', 'u']
    if letra in vogais:
        print("Vogal")
    else:
        print("Consoante")

while True:
    letra = input("Insira uma letra: ")
    if letra.isalpha():
        break
    else:
        print("Insira uma letra válida!")
vogal_ou_consoante(letra)
