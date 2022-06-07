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
from itertools import islice

def corrigir(*provas):
    """Escreva aqui em baixo a sua solução"""
    gabarito = ('A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A')

    def corrigir_prova(prova):
        aluno = prova[0]
        nota = sum(1 for resposta_certa, reposta in zip(gabarito, islice(prova, 1, None)) if reposta == resposta_certa)
        return aluno, nota

    correcoes = dict(map(corrigir_prova, provas))
    print(f'Aluno                 Nota')
    for aluno, nota in correcoes.items():
        print(f'{aluno:21s} {nota:2d}')
    print(f'---------------------------')
    print(f'Média geral: 10.0')
    print(f'Maior nota: 10')
    print(f'Menor nota: 10')
    print(f'Total de Alunos: 10')
