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

    quantidade_numeros = len(numeros)    
    contador = 0
    while quantidade_numeros > contador and quantidade_numeros != 0:
        if numeros[contador] in range(0, 1000):
            if len(numeros) >= 2:
                if len(numeros) > contador:
                    if (contador+1) < len(numeros):
                        if contador == 0:
                            if numeros[contador] > numeros[contador+1]:
                                maior = numeros[contador]
                                menor = numeros[contador+1]
                                soma = numeros[contador] + numeros[contador+1]
                                contador = contador + 1
                            else:
                                maior = numeros[contador+1]
                                menor = numeros[contador]
                                soma = numeros[contador] + numeros[contador+1]
                                contador = contador + 1
                        else:
                            if numeros[contador+1] > menor:                            
                                if numeros[contador+1] > maior:                                
                                    maior = numeros[contador+1]
                                    soma = soma + numeros[contador+1]
                                    contador = contador + 1                        
                            else:
                                menor = numeros[contador+1]
                                soma = soma + numeros[contador+1]                            
                                contador = contador + 1
                    else:                    
                        print('\'Maior valor: %.0f. Menor valor: %.0f. Soma: %.0f\''%(maior,menor,soma))
                        break
            else:
                maior = numeros[0]
                menor = numeros[0]
                soma = numeros[0]
                print('\'Maior valor: %.0f. Menor valor: %.0f. Soma: %.0f\''%(maior,menor,soma))
                break
        else:
            print('\'Somente números de 0 a 1000 são permitidos\'')
            break
    else:
        print('\'Maior valor: não existe. Menor valor: não existe. Soma: 0\'')