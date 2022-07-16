"""
Exercício 25 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

  "Telefonou para a vítima?"
  "Esteve no local do crime?"
  "Mora perto da vítima?"
  "Devia para a vítima?"
  "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

    >>> investigar('Sim','Sim','Sim','Sim','Sim')
    'Assassino'
    >>> investigar('Sim','Sim','Sim','Sim','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Sim','Não','Não')
    'Cúmplice'
    >>> investigar('Sim','Sim','Não','Não','Não')
    'Suspeito'
    >>> investigar('Sim','Não','Não','Não','Não')
    'Inocente'
    >>> investigar('Não','Não','Não','Não','Não')
    'Inocente'

"""


def investigar(telefonou: str, estava_no_local: str, mora_perto: str, devia: str, trabalhou: str, ):
    

    #perguntas = [ "Telefonou para a vítima? ", "Esteve no local do crime? ",
    #"Mora perto da vítima? ", "Devia para a vítima? ", "Já trabalhou com a vítima? "]
    respostas_positivas = 0

    #for a in range(5):
     #   resposta = ''
      #  while resposta != 'sim' and resposta != 'não':
       #     print(perguntas[a], end='')
        #    resposta = input().lower()
            #if resposta == 'sim':
             #   respostas_positivas +=1

    if telefonou == 'Sim':
        respostas_positivas +=1
    if estava_no_local == 'Sim':
        respostas_positivas +=1
    if mora_perto == 'Sim':
        respostas_positivas +=1
    if devia == 'Sim':
        respostas_positivas +=1
    if trabalhou == 'Sim':
        respostas_positivas +=1


    if respostas_positivas == 5:
        classificacao = "'Assassino'"

    elif respostas_positivas == 3 or respostas_positivas == 4:
        classificacao = "'Cúmplice'"

    elif respostas_positivas == 2:
        classificacao = "'Suspeito'"

    elif respostas_positivas < 2:
        classificacao = "'Inocente'"

    print (classificacao)

