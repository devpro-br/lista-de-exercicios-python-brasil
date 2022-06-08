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
    """Escreva aqui em baixo a sua solução"""
    #Convertendo para binario
    if telefonou == 'Sim':
      telefonou = 1
    else:
      telefonou = 0
    #Convertendo para binario
    if estava_no_local == 'Sim':
      estava_no_local = 1
    else:
      estava_no_local = 0
    #Convertendo para binario
    if mora_perto == 'Sim':
      mora_perto = 1
    else:
      mora_perto = 0
    #Convertendo para binario
    if devia == 'Sim':
      devia = 1
    else:
      devia = 0
    #Convertendo para binario
    if trabalhou == 'Sim':
      trabalhou = 1
    else:
      trabalhou = 0
    #Auxilio Teste#    
    teste = telefonou + estava_no_local + mora_perto + devia + trabalhou

    if teste == 5:
      return 'Assassino'
    elif teste >= 3:
      return 'Cúmplice'
    elif teste >=2:
      return 'Suspeito'
    else:
      return 'Inocente'
