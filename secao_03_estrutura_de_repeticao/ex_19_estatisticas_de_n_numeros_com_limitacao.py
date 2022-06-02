"""
Exercício 19 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

    >>> calcular_estatisticas()
    'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    >>> calcular_estatisticas(1)
    'Maior valor: 1. Menor valor: 1. Soma: 1'
    >>> calcular_estatisticas(1, 2)
    'Maior valor: 2. Menor valor: 1. Soma: 3'
    >>> calcular_estatisticas(1, 2, -1)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, -10)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1001)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1198)
    'Somente números de 0 a 1000 são permitidos'

"""
def calcular_estatisticas(*numeros) -> str:
    """Escreva aqui em baixo a sua solução"""
    n = [*numeros]
    if n == []:
        print("'Maior valor: não existe. Menor valor: não existe. Soma: 0'")
    else:
        procede = True
        for i in range(0, len(n)):
            if n[i] < 0 or n[i] > 1000:
                print("'Somente números de 0 a 1000 são permitidos'")
                i+=1
                procede = False
        if procede == True:
            n.sort()
            print(f"'Maior valor: {n[-1]}. Menor valor: {n[0]}. Soma: {sum(n)}'")