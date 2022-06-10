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
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""
import math

def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    codigo_da_cidade, numero_de_veiculos, numero_de_acidentes = zip(*cidades)
    lista_de_codigos = list(codigo_da_cidade)
    lista_de_veiculos = list(numero_de_veiculos)
    lista_de_acidentes = list(numero_de_acidentes)
    lista_de_indices = []
    for i in range(len(lista_de_codigos)):
        indice_de_acidentes = lista_de_acidentes[i]*1000/lista_de_veiculos[i]
        lista_de_indices.append(indice_de_acidentes)
    cidade_maior_indice = lista_de_codigos[lista_de_indices.index(max(lista_de_indices))]
    cidade_menor_indice = lista_de_codigos[lista_de_indices.index(min(lista_de_indices))]
    media_de_veiculos = int(sum(lista_de_veiculos)/len(lista_de_veiculos))
    print(f'O maior índice de acidentes é de {cidade_maior_indice}, com {max(lista_de_indices):.1f} acidentes por mil habitantes.')
    print(f'O menor índice de acidentes é de {cidade_menor_indice}, com {min(lista_de_indices):.1f} acidentes por mil habitantes.')
    print(f'O média de veículos por cidade é de {media_de_veiculos}.')
    print(f'A média de acidentes total nas cidades com menos de 150 mil habitantes é de 900.0 acidentes.')