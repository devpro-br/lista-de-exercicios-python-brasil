""" 
Exercício 4 da seção 6 da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

    >>> leia_n('m', 'a', 'r', 'c', 'o', 's')
    m
    ma
    mar
    marc
    marco
    marcos
    >>> leia_n('c', 'l', 'a', 'r', 'a')
    c
    cl
    cla
    clar
    clara
    >>> leia_n('m', 'a', 'u', 'r', 'a' , 'o' )
    m
    ma
    mau
    maur
    maura
    maurao


"""

def leia_n(*valores):
    nome = []