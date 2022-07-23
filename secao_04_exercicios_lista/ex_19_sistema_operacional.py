"""
Exercício 19 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

    >>> from secao_04_exercicios_lista import ex_19_sistema_operacional
    >>> entradas = ['0', '2', '2', '6','6', '2', '1','5', '2', '1','2', '2', '4','2', '2', '1','2', '2', '1',]
    >>> ex_19_sistema_operacional.input = lambda k: entradas.pop()
    >>> ex_19_sistema_operacional.rodar_senso()
    Sistema Operacional       Votos    %
    -------------------       -----  -----
    Windows Server               4   22.2%
    Unix                        10   55.6%
    Linux                        0    0.0%
    Netware                      1    5.6%
    Mac OS                       1    5.6%
    Outro                        2   11.1%
    -------------------       -----
    Total                       18
    >>> entradas = ['0', '3', '2', '1']
    >>> ex_19_sistema_operacional.input = lambda k: entradas.pop()
    >>> ex_19_sistema_operacional.rodar_senso()
    Sistema Operacional       Votos    %
    -------------------       -----  -----
    Windows Server               1   33.3%
    Unix                         1   33.3%
    Linux                        1   33.3%
    Netware                      0    0.0%
    Mac OS                       0    0.0%
    Outro                        0    0.0%
    -------------------       -----
    Total                        3
    >>> entradas = ['0', '2', '1']
    >>> ex_19_sistema_operacional.input = lambda k: entradas.pop()
    >>> ex_19_sistema_operacional.rodar_senso()
    Sistema Operacional       Votos    %
    -------------------       -----  -----
    Windows Server               1   50.0%
    Unix                         1   50.0%
    Linux                        0    0.0%
    Netware                      0    0.0%
    Mac OS                       0    0.0%
    Outro                        0    0.0%
    -------------------       -----
    Total                        2
    >>> entradas = ['0', '2', '7']
    >>> ex_19_sistema_operacional.input = lambda k: entradas.pop()
    >>> ex_19_sistema_operacional.rodar_senso()
    Sistema Operacional       Votos    %
    -------------------       -----  -----
    Windows Server               0    0.0%
    Unix                         1   100.0%
    Linux                        0    0.0%
    Netware                      0    0.0%
    Mac OS                       0    0.0%
    Outro                        0    0.0%
    -------------------       -----
    Total                        1
    

   
"""


def rodar_senso():
    """Escreva aqui em baixo a sua solução"""
    entradas = []

    while True:
        inp = input('Digite o nome: ')
        if inp == '0':
            break
        entradas.append(inp)
     
    server = entradas.count('1')
    unix = entradas.count('2')
    linux = entradas.count('3')
    netware = entradas.count('4')
    mac = entradas.count('5')
    outros = entradas.count('6')

    total = server + unix + linux + netware + mac + outros

    porc_server = server / total * 100
    porc_unix = unix / total * 100
    porc_linux = linux / total * 100
    porc_netware = netware / total * 100
    porc_mac = mac / total * 100
    porc_outros = outros / total * 100
    


    print(f'Sistema Operacional       Votos    %')
    print(f'-------------------       -----  -----')
    print(f'Windows Server'.ljust(25), f'{server:4}   {porc_server:4.1f}%')
    print(f'Unix'.ljust(25), f'{unix:4}   {porc_unix:4.1f}%')
    print(f'Linux'.ljust(25), f'{linux:4}   {porc_linux:4.1f}%')
    print(f'Netware'.ljust(25), f'{netware:4}   {porc_netware:4.1f}%')
    print(f'Mac OS'.ljust(25), f'{mac:4}   {porc_mac:4.1f}%')
    print(f'Outro'.ljust(25), f'{outros:4}   {porc_outros:4.1f}%')
    print(f'-------------------'.ljust(25), f'-----')
    print(f'Total'.ljust(25), f'{total:4}')




