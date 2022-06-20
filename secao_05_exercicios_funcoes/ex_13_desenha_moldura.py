"""
Exercício 13 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosFuncoes

Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. 
Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.
Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

>>> desenha_moldura (5, 7)
+-----+
|     |
|     |
|     |
+-----+
>>> desenha_moldura (0, 3)
Não é possivel construir uma moldura sem linhas, a quantidade de linhas foi alterada para 1.
+-+
>>> desenha_moldura (5, 0)
Não é possivel construir uma moldura sem colunas, a quantidade de colunas foi alterada para 1.
+
|
|
|
+
>>> desenha_moldura (25, 30)
O numero maximo de linhas é 20, a quantidade de linhas foi alterado para 20.
O numero maximo de colunas é 20, a quantidade de colunas foi alterado para 20.
+------------------+
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
+------------------+
"""

