"""
Exercício 13 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosFuncoes

Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. 
Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.
Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

>>> from secao_05_exercicios_funcoes import ex_13_desenha_moldura
>>> entradas = {'linhas':3,'colunas':7}
>>> ex_13_desenha_moldura.input = lambda k: entradas.get('linhas')
>>> ex_13_desenha_moldura.input = lambda k: entradas.get('colunas')
>>> ex_13_desenha_moldura.desenha_moldura()
+-------+
|       |
|       |
|       |
+-------+
>>> entradas = {'linhas':0,'colunas':3}
>>> ex_13_desenha_moldura.input = lambda k: entradas.get('linhas')
>>> ex_13_desenha_moldura.input = lambda k: entradas.get('colunas')
>>> ex_13_desenha_moldura.desenha_moldura()
O número mínimo de linhas é 1, a quantidade de linhas foi alterada para 1.
+---+
|   |
+---+
>>> entradas = {'linhas':2,'colunas':0}
>>> ex_13_desenha_moldura.input = lambda k: entradas.get('linhas')
>>> ex_13_desenha_moldura.input = lambda k: entradas.get('colunas')
>>> ex_13_desenha_moldura.desenha_moldura()
O número mínimo de colunas é 1, a quantidade de colunas foi alterada para 1.
+-+
| |
| |
+-+
>>> entradas = {'linhas':25,'colunas':30}
>>> ex_13_desenha_moldura.input = lambda k: entradas.get('linhas')
>>> ex_13_desenha_moldura.input = lambda k: entradas.get('colunas')
>>> ex_13_desenha_moldura.desenha_moldura()
O número máximo de linhas é 20, a quantidade de linhas foi alterada para 20.
O número máximo de colunas é 20, a quantidade de colunas foi alterada para 20.
+--------------------+
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
|                    |
+--------------------+
"""
