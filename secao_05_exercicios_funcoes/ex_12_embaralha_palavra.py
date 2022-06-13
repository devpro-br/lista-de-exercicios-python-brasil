"""
Exercício 12 da seção de funções da Python Brasil:
https://wiki.python.org.br/ExerciciosFuncoes

Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. 
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, 
de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, 
independentemente de como foram digitados.

    >>> resultado = embaralha_palavra('Python')
    >>> if resultado == 'Python' or resultado == 'python' or len(resultado) != 6 or sorted(resultado) != ['h', 'n', 'o', 'p', 't', 'y'] or resultado.isupper() and resultado.islower() == False:
    ...     False
    >>> resultado2 = embaralha_palavra('Python')
    >>> if resultado2 == resultado:
    ...     False

    OBS: USE RETURN AO INVÉS DE PRINT COMO RETORNO DA FUNÇÃO!
"""
import random

def embaralha_palavra(palavra:str):
    palavra = palavra.lower()
    lista_palavra = []
    lista_palavra[:0] = palavra
    random.shuffle(lista_palavra)
    nova_palavra = ''.join(map(str, lista_palavra))
    return nova_palavra