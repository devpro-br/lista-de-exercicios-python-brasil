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
def gabarito(*lista_de_respostas):
    gabarito = ('A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A')
    nota = 0
    for par in zip(gabarito, lista_de_respostas):
        if par[0] == par[1]:
            nota+=1
    return nota


def corrigir(*provas):
    """Escreva aqui em baixo a sua solução"""
    provas = [*provas]
    lista_de_nomes = []
    lista_de_respostas = []
    print('Aluno                 Nota')
    for prova in provas:
        lista_de_nomes.append(prova[0])
        lista_de_respostas.append(prova[1:])
    nota1 = gabarito(*lista_de_respostas[0])
    nome1 = lista_de_nomes[0]
    if len(lista_de_nomes) > 1:
        total_de_alunos = 2
        nota2 = gabarito(*lista_de_respostas[1])
        nome2 = lista_de_nomes[1]
        print(f'{nome1}                 {nota1}')
        print(f'{nome2}                 {nota2}')
        media_geral = (nota1 + nota2) / 2
        if nota1 > nota2:
            maior_nota = nota1
            menor_nota = nota2
        else:
            maior_nota = nota2
            menor_nota = nota1
    else:
        total_de_alunos = 1
        print(f'{nome1}                 {nota1}')
        media_geral = nota1
        maior_nota = nota1
        menor_nota = nota1
    print('---------------------------')
    print(f'Média geral: {media_geral:.1f}')
    print(f'Maior nota: {maior_nota}')
    print(f'Menor nota: {menor_nota}')
    print(f'Total de Alunos: {total_de_alunos}')