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
