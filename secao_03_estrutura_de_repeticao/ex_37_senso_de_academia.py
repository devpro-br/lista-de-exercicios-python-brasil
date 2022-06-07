"""
Exercício 37 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_37_senso_de_academia
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_37_senso_de_academia.input = lambda k: entradas.pop()
    >>> ex_37_senso_de_academia.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""


def rodar_senso():
    """Escreva aqui em baixo a sua solução"""
    #Criando listas para cada informação# 
    lista_nome = []
    lista_peso = []
    lista_altura = []
    lista_nome.append(input('Insira o nome do aluno ou digite 0 para encerrar: '))
    while lista_nome[0].isdigit() == False:
        lista_altura.insert(0,int((input('Insira a altura do aluno:'))))
        lista_peso.insert(0,int((input('Insira o peso do aluno:'))))
        lista_nome.insert(0,(input('Insira o nome do proximo aluno ou digite 0 para terminar:')))
        if lista_nome[0].isdigit() == True:
            lista_nome.pop(0)
            break
        else:
            continue
    
    nome_maior_aluno = lista_nome[lista_altura.index(max(lista_altura))]
    maior_aluno = int(max(lista_altura))
    nome_menor_aluno = lista_nome[lista_altura.index(min(lista_altura))]
    menor_aluno = int(min(lista_altura))
    nome_mais_gordo = lista_nome[lista_peso.index(max(lista_peso))]
    mais_gordo = int(max(lista_peso))
    nome_mais_magro = lista_nome[lista_peso.index(min(lista_peso))]
    mais_magro = int(min(lista_peso))

    print('Cliente mais alto: %s, com %.0f centímetros'%(nome_maior_aluno, maior_aluno))
    print('Cliente mais baixo: %s, com %.0f centímetros'%(nome_menor_aluno, menor_aluno))
    print('Cliente mais magro: %s, com %.0f kilos'%(nome_mais_magro, mais_magro))
    print('Cliente mais gordo: %s, com %.0f kilos'%(nome_mais_gordo, mais_gordo))

    #USAR ISSO
    lista_altura.index(max(lista_altura))

    

