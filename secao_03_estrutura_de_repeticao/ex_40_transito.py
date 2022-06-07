"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil habitantes.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil habitantes.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil habitantes é de 900.0 acidentes.
"""


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    #VARIAVEIS#
    cidade, numero_veiculos, numero_acidentes = zip(*cidades)      
    soma_veiculos = 0
    soma_acidentes = 0
    quantidade_cidade = 0

    #MEDIA DE VEICULOS#
    contador_1 = 0
    while contador_1 < len(numero_veiculos):
        soma_veiculos = numero_veiculos[contador_1] + soma_veiculos
        contador_1 += 1

    media_veiculos = soma_veiculos/(len(numero_veiculos))
    
    #MEDIA DE NUMERO DE ACIDENTES PARA CIDADE COM MENOS DE 150.000 VEICULOS#
    contador_2 = 0
    while contador_2 < len(numero_acidentes):
        if numero_veiculos[contador_2] <= 150000:
            soma_acidentes = numero_acidentes[contador_2] + soma_acidentes
            contador_2 += 1 
            quantidade_cidade +=1
        else:
            contador_2 += 1
    
    media_acidentes = soma_acidentes/quantidade_cidade 

    #Calculo índice de acidentes#
    contador = 0
    indice = []
    while contador < len(numero_acidentes):
        indice_acidentes = numero_acidentes[contador]/numero_veiculos[contador]
        indice.append(indice_acidentes)
        contador += 1

    maior_indice_acidentes = cidade[indice.index(max(indice))]
    menor_indice_acidentes = cidade[indice.index(min(indice))]
    quantidade_maior = max(indice)*1000    
    quantidade_menor = min(indice)*1000         

    print('O maior índice de acidentes é de %s, com %.1f acidentes por mil habitantes.'%(maior_indice_acidentes,quantidade_maior))
    print('O menor índice de acidentes é de %s, com %.1f acidentes por mil habitantes.'%(menor_indice_acidentes,quantidade_menor))
    print('O média de veículos por cidade é de %.0f.'%(media_veiculos))
    print('A média de acidentes total nas cidades com menos de 150 mil habitantes é de %.1f acidentes.'%(media_acidentes))

    
    
    
    
    
    
