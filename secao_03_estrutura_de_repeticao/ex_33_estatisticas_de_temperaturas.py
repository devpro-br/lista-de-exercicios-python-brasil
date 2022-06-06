"""
Exercício 33 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

Mostre a média com uma casa decimal.

    >>> calcular_estatisticas()
    'Maior temperatura: não existe. Menor temperatura: não existe. Média: não existe'
    >>> calcular_estatisticas(1)
    'Maior temperatura: 1. Menor temperatura: 1. Média: 1.0'
    >>> calcular_estatisticas(1, 2)
    'Maior temperatura: 2. Menor temperatura: 1. Média: 1.5'
    >>> calcular_estatisticas(1, 2, -1)
    'Maior temperatura: 2. Menor temperatura: -1. Média: 0.7'


"""


def calcular_estatisticas(*temperaturas) -> str:
    """Escreva aqui em baixo a sua solução"""

    quantidade_numeros = len(temperaturas)    
    contador = 0
    while quantidade_numeros > contador and quantidade_numeros != 0:
        if len(temperaturas) >= 2:
                if (contador+1) < len(temperaturas):
                    if contador == 0:
                        if temperaturas[contador] > temperaturas[contador+1]:
                            maior = temperaturas[contador]
                            menor = temperaturas[contador+1]
                            soma = temperaturas[contador] + temperaturas[contador+1]
                            contador = contador + 1
                        else:
                            maior = temperaturas[contador+1]
                            menor = temperaturas[contador]
                            soma = temperaturas[contador] + temperaturas[contador+1]
                            contador = contador + 1
                    else:
                        if temperaturas[contador+1] > menor:                            
                            if temperaturas[contador+1] > maior:                                
                                maior = temperaturas[contador+1]
                                soma = soma + temperaturas[contador+1]
                                contador = contador + 1                        
                        else:
                            menor = temperaturas[contador+1]
                            soma = soma + temperaturas[contador+1]                            
                            contador = contador + 1
                else:       
                    media = soma/len(temperaturas)             
                    print('\'Maior temperatura: %.0f. Menor temperatura: %.0f. Média: %.1f\''%(maior,menor,media))
                    break
        else:
            maior = temperaturas[0]
            menor = temperaturas[0]
            soma = temperaturas[0]
            media = soma/len(temperaturas)  
            print('\'Maior temperatura: %.0f. Menor temperatura: %.0f. Média: %.1f\''%(maior,menor,soma))
            break
    else:
        print('\'Maior temperatura: não existe. Menor temperatura: não existe. Média: não existe\'')
