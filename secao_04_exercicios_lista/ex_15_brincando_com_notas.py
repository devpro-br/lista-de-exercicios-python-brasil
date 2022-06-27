"""
Exercício 15 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Faça um programa que leia um número indeterminado de valores, correspondentes a notas (números reais com uma casa após a vírgula),
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
Após esta entrada de dados, faça:
1)Mostre a quantidade de valores que foram lidos;
2)Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
3)Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
4)Calcule e mostre a soma dos valores;
5)Calcule e mostre a média dos valores;
6)Calcule e mostre a quantidade de valores acima da média calculada;
7)Calcule e mostre a quantidade de valores abaixo de sete;
8)Encerre o programa com uma mensagem;

    >>> from secao_04_exercicios_lista import ex_15_brincando_com_notas
    >>> notas = ['-1', '9.5', '6', '6', '10', '6']
    >>> ex_15_brincando_com_notas.input = lambda k: notas.pop()
    >>> ex_15_brincando_com_notas.brincar_com_notas()
    Quantidade de valores recebidos: 5
    6.0, 10.0, 6.0, 6.0, 9.5
    ------------------------------------------------------------------
    9.5
    6.0
    6.0
    10.0
    6.0
    ------------------------------------------------------------------
    Soma: 37.5
    Média: 7.5
    Valores acima dessa média: 2
    Valores abaixo de 7: 3
    ------------------------------------------------------------------
    O programa foi encerrado :)

    >>> from secao_04_exercicios_lista import ex_15_brincando_com_notas
    >>> notas = ['-1', '3.5', '2.7']
    >>> ex_15_brincando_com_notas.input = lambda k: notas.pop()
    >>> ex_15_brincando_com_notas.brincar_com_notas()
    Quantidade de valores recebidos: 2
    2.7, 3.5
    ------------------------------------------------------------------
    3.5
    2.7
    ------------------------------------------------------------------
    Soma: 6.2
    Média: 3.1
    Valores acima dessa média: 1
    Valores abaixo de 7: 2
    ------------------------------------------------------------------
    O programa foi encerrado :)
  

"""


def brincar_com_notas():
    """Escreva aqui em baixo a sua solução"""
