"""
Exercício 06 da seção de funções da Python Brasil:
https://wiki.python.org.br/ExerciciosFuncoes

Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
A entrada é dada em dois inteiros. 
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
Registre a informação A.M./P.M. como um valor 'A' para A.M. e 'P' para P.M. 
Assim, a função para efetuar as conversões terá um parâmetro formal para 
registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário 
repita esse cálculo para novos valores de entrada todas as vezes que desejar.

    >>> from secao_05_exercicios_funcoes import ex_06_converte_horas
    >>> entradas = [0, 25, 18, 42,17, 30,7] 
    >>> ex_06_converte_horas.input = lambda k: entradas.pop()
    >>> ex_06_converte_horas.converte_horas()
    7:30  --> 7:30 A.M.
    17:42  --> 5:42 P.M.
    18:25  --> 6:25 P.M.
    >>> entradas = [0] 
    >>> ex_06_converte_horas.input = lambda k: entradas.pop()
    >>> ex_06_converte_horas.converte_horas()
    >>> entradas = [0, 18, 19, 25,50, 60,17, 4,18] 
    >>> ex_06_converte_horas.input = lambda k: entradas.pop()
    >>> ex_06_converte_horas.converte_horas()
    18:04  --> 6:04 P.M.
    Minutos inválidos.
    17:50  --> 5:50 P.M.
    Hora inválida.
    19:18  --> 7:18 P.M.
    >>> entradas = [0, 25,19, 4,18, 40,18] 
    >>> ex_06_converte_horas.input = lambda k: entradas.pop()
    >>> ex_06_converte_horas.converte_horas()
    18:40  --> 6:40 P.M.
    18:04  --> 6:04 P.M.
    19:25  --> 7:25 P.M.
    >>> entradas = [0, 25,4, 3,6, 10,7] 
    >>> ex_06_converte_horas.input = lambda k: entradas.pop()
    >>> ex_06_converte_horas.converte_horas()
    7:10  --> 7:10 A.M.
    6:03  --> 6:03 A.M.
    4:25  --> 4:25 A.M.
"""


 

