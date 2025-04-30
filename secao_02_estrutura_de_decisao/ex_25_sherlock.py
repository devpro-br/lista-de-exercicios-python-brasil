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
  respostas = [telefonou, estava_no_local, mora_perto, devia, trabalhou]
  positivos = respostas.count('Sim')
  
  if positivos == 5:
    return 'Assassino'
  elif 3 <= positivos <= 4:
    return 'Cúmplice'
  elif positivos == 2:
    return 'Suspeito'
  elif positivos == 1:
    return 'Inocente'
  elif positivos == 0:
    return 'Inocente'

telefonou = input("Telefonou para a vítima? ")
estava_no_local = input("Esteve no local do crime? ")
mora_perto = input("Mora perto da vítima? ")
devia = input("Devia para a vítima? ")
trabalhou = input("Já trabalhou com a vítima? ")
print(investigar(telefonou, estava_no_local, mora_perto, devia, trabalhou))