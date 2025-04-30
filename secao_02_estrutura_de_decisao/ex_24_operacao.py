"""
Exercício 24 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

    >>> fazer_operacao_e_classificar(2, 3, '+')
    Resultado: 5.00
    Número é impar, positivo e inteiro.
    >>> fazer_operacao_e_classificar(-4, 2, '/')
    Resultado: -2.00
    Número é par, negativo e inteiro.
    >>> fazer_operacao_e_classificar(0, 2, '*')
    Resultado: 0.00
    Número é par, neutro e inteiro.
    >>> fazer_operacao_e_classificar(-3.14, 2, '*')
    Resultado: -6.28
    Número é negativo e decimal.
    >>> fazer_operacao_e_classificar(3.14, 2, '-')
    Resultado: 1.14
    Número é positivo e decimal.

"""


def fazer_operacao_e_classificar(n_1: float, n_2: float, operacao: str):
  """Escreva aqui em baixo a sua solução"""
  match (operacao):
    case 'Soma'|'soma':
      resultado = n_1 + n_2
    case 'Subtração'|'subtração':
      resultado = n_1 - n_2
    case 'Multiplicação'|'multiplicação':
      resultado = n_1 * n_2
    case 'Divisão'|'divisão':
      resultado = n_1 / n_2
    case _:
      print("Operação inválida!")
      
  def par_ou_impar(resultado):
    if resultado % 2 == 0:
      return 'par'
    else:
      return 'ímpar'
    
  def positivo_ou_negativo(resultado):
    if resultado > 0:
      return 'positivo'
    elif resultado < 0:
      return 'negativo'
    else:
      return 'netro'
    
  def inteiro_ou_decimal(resultado):
    if resultado == round(resultado):
      return 'inteiro'
    else:
      return 'decimal'
  
  print(f"Resultado: {resultado:.2f}\nNúmero é {par_ou_impar(resultado)}, {positivo_ou_negativo(resultado)} e {inteiro_ou_decimal(resultado)}.")
    
while True:
  try:
    n1 = float(input("Insira o primeiro número: "))
    n2 = float(input("Insira o segundo número: "))
    break
  
  except ValueError:
    print("Insira um número válido!")

operacao = input("Escolha uma operação (soma, subtração, multiplicação, ou divisão): ")
fazer_operacao_e_classificar(n1, n2, operacao)

