"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia e valide as seguintes informações:

  Nome: maior que 3 caracteres;
  Idade: entre 0 e 150;
  Salário: maior que zero;
  Sexo: 'f' ou 'm';
  Estado Civil: 's', 'c', 'v', 'd';

    >>> cadastrar_usuario('Renzo', 39, 2000, 'm', 'c')
    Cadastro realizado com sucesso
    >>> cadastrar_usuario('Gil', 1, 2000.05, 'f', 's')
    Cadastro realizado com sucesso
    >>> cadastrar_usuario('Gi', 150, 2000.05, 'f', 'v')
    Erro: o nome precisa ter 3 letras ou mais, não pode ser Gi
    >>> cadastrar_usuario('Ti', -1, 2000.05, 'f', 'v')
    Erro: o nome precisa ter 3 letras ou mais, não pode ser Ti
    Erro: a idade precisa estar entre 0 e 150, não pode ser -1
    >>> cadastrar_usuario('Mi', 151, 0, 'f', 'v')
    Erro: o nome precisa ter 3 letras ou mais, não pode ser Mi
    Erro: a idade precisa estar entre 0 e 150, não pode ser 151
    Erro: o salário precisa ser positivo, não pode ser 0
    >>> cadastrar_usuario('Mi', 151, 0, 'z', 'v')
    Erro: o nome precisa ter 3 letras ou mais, não pode ser Mi
    Erro: a idade precisa estar entre 0 e 150, não pode ser 151
    Erro: o salário precisa ser positivo, não pode ser 0
    Erro: o sexo precisa ser "m" ou "f", não pode ser "z"
    >>> cadastrar_usuario('Mi', 151, 0, 't', 'p')
    Erro: o nome precisa ter 3 letras ou mais, não pode ser Mi
    Erro: a idade precisa estar entre 0 e 150, não pode ser 151
    Erro: o salário precisa ser positivo, não pode ser 0
    Erro: o sexo precisa ser "m" ou "f", não pode ser "t"
    Erro: o estado civil precisa ser "s", "c", "v" ou "d", não pode ser "p"

"""


def cadastrar_usuario(nome: str, idade: int, salario: float, sexo: str, estado_civil: str):
    """Escreva aqui em baixo a sua solução"""
    ok = 0

    str_ok = 'Cadastro realizado com sucesso'
    str_usuario = 'Erro: o nome precisa ter 3 letras ou mais, não pode ser '
    str_idade = 'Erro: a idade precisa estar entre 0 e 150, não pode ser '
    str_salario = 'Erro: o salário precisa ser positivo, não pode ser '
    str_sexo = 'Erro: o sexo precisa ser "m" ou "f", não pode ser '
    str_estado = 'Erro: o estado civil precisa ser "s", "c", "v" ou "d", não pode ser '

    if len(nome) >= 3:
       ok +=1
    else:
        print(f"{str_usuario}{nome}")

    if idade in range(0, 151):
        ok +=1
    else:
        print(f"{str_idade}{idade}")

    if salario > 0:
        ok += 1
    else:
        print(f"{str_salario}{salario}")

    if sexo.lower() in ('f', 'm'):
        ok += 1
    else:
        print(f'{str_sexo}"{sexo}"')

    if estado_civil.lower() in ('s', 'c', 'v', 'd'):
        ok += 1
    else:
        print(f'{str_estado}"{estado_civil}"')

    if ok == 5:
        print(str_ok)
