"""
Exercício 21 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é
divisível somente por ele mesmo e por 1.

    >>> eh_primo(0)
    False
    >>> eh_primo(1)
    False
    >>> eh_primo(2)
    True
    >>> eh_primo(3)
    True
    >>> eh_primo(4)
    False
    >>> eh_primo(5)
    True
    >>> eh_primo(6)
    False
    >>> eh_primo(7)
    True
    >>> eh_primo(8)
    False
    >>> eh_primo(9)
    False
    >>> eh_primo(10)
    False
    >>> eh_primo(11)
    True
    >>> eh_primo(547)
    True
    >>> eh_primo(548)
    False

"""


def eh_primo(n: int) -> bool:
    """Escreva aqui em baixo a sua solução"""
    # if n / n == 0 and n % 1 == 0 and n / 2 != 0:
    #     print(True)
    # else:
    #     print(False)

    # for i in range(2, n+1):
    #     if n / n == 0 and n % i == 0 and n / 2 != 0:
    #         print(True)
    #     else:
    #         print(False)
        
    mult=0

    for i in range(1,n+1):
        if (n % i == 0):
            mult += 1

    if mult == 2:
        print("True")
    else:
        print("False")
