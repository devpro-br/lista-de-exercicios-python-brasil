"""
Exercício 45 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma com uma casa decimal.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

    >>> corrigir(('Renzo','A','B','C','D','E','E','D','C','B','A' ))
    Aluno                 Nota
    Renzo                 10
    ---------------------------
    Média geral: 10.0
    Maior nota: 10
    Menor nota: 10
    Total de Alunos: 1
    >>> corrigir(
    ... ('Renzo','A','B','C','D','E','E','D','C','B','A' ),
    ... ('Fulano','A','B','C','D','E','E','D','C','B','B' ),
    ... )
    Aluno                 Nota
    Renzo                 10
    Fulano                 9
    ---------------------------
    Média geral: 9.5
    Maior nota: 10
    Menor nota: 9
    Total de Alunos: 2
"""


from re import I


def corrigir(*provas):
    """Escreva aqui em baixo a sua solução"""
    contador = 0
    contador_2 = 0
    nota = 0
    maior_nota = 0
    menor_nota = 0
    soma = 0
    print('Aluno                 Nota')
    while len(provas) > contador:
        prova = list(provas[contador])
        aluno = prova[0]
        prova.pop(0)
        if prova[0] == 'A':
            nota += 1
        if prova[1] == 'B':
            nota += 1
        if prova[2] == 'C':
            nota += 1
        if prova[3] == 'D':
            nota += 1
        if prova[4] == 'E':
            nota += 1
        if prova[5] == 'E':
            nota += 1
        if prova[6] == 'D':
            nota += 1
        if prova[7] == 'C':
            nota += 1
        if prova[8] == 'B':
            nota += 1
        if prova[9] == 'A':
            nota += 1
        print('%s                 %.0f'%(aluno, nota))
        soma = soma + nota
        if len(provas) > 1:
            if nota > maior_nota:
                menor_nota = maior_nota
                maior_nota = nota
            else:
                menor_nota = nota
        else: 
            maior_nota = nota
            menor_nota = nota
        contador += 1        
        nota = 0
    
    total_alunos = int(len(provas))
    media = (soma)/total_alunos
    print('---------------------------')
    print('Média geral: %.1f'%media)
    print('Maior nota: %.0f'%maior_nota)
    print('Menor nota: %.0f'%menor_nota)
    print('Total de Alunos: %.0f'%total_alunos)
        

