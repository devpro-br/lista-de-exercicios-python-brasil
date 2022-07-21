"""
Exercício 02 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma
mensagem de erro e voltando a pedir as informações.

    >>> from secao_03_estrutura_de_repeticao import ex_02_validador_de_senha
    >>> credenciais = ['senha', 'meu_login']
    >>> ex_02_validador_de_senha.input = lambda k: credenciais.pop()
    >>> ex_02_validador_de_senha.validar_senha()
    'Cadastro realizado com suceso, seu login é meu_login'
    >>> credenciais = ['outra_senha', 'outro_login', 'igual', 'igual']
    >>> ex_02_validador_de_senha.input = lambda k: credenciais.pop()
    >>> ex_02_validador_de_senha.validar_senha()
    Senha deve ser diferente do login
    'Cadastro realizado com suceso, seu login é outro_login'

"""


def validar_senha():
    """Escreva aqui em baixo a sua solução"""
    while True:
        login = input('Login: ')
        senha = input('Senha: ')
        if senha != login:
            break
        else:
            print('Senha deve ser diferente do login')
            pass
    print(f"'Cadastro realizado com suceso, seu login é {login}'")
