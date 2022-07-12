"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    
    import calendar

    def ver_bissexto(ano):
        mensagem = ''
        bissexto = calendar.isleap(ano)
        if bissexto == True:
            mensagem = 'bissexto'

        return mensagem


    while True:
        try:
            aviso = "'Data válida'"
            aaaa = ''
            data = input('Entre com uma data dd/mm/aaaa: ')
            tamanho = len(data)
            #print(f'tamanho: {tamanho}')
            if tamanho < 8 or tamanho > 10: #or data[2] != "/" or data[5] != "/":
                print("'Data inválida'")
                break
            cont = tamanho -1
            while cont >= 0:
                if cont > tamanho - 5:
                    aaaa = data[cont] + aaaa
                cont-=1
            if tamanho == 8:
                mm = data[2]
                dd = data[0]

            if tamanho == 9 and data[2] == '/':
                dd = data[0] + data[1]
                mm = data[3]
            if tamanho == 9 and data[1] == '/':

                dd = data[0]
                mm = data[2] + data[3]
            
            if tamanho == 10:
                dd = data[0] + data[1]
                mm = data[3] + data[4]


            dd = int(dd)
            mm = int(mm)
            aaaa = int(aaaa)
            mensagem = ver_bissexto(aaaa)


            if mm < 1 or mm > 12 or dd < 1:
                aviso = "'Data inválida'"

            elif mm == 2 and mensagem != "bissexto" and dd > 28:
                aviso = "'Data inválida'"

            elif mm == 2 and mensagem == "bissexto" and dd > 29:
                aviso = "'Data inválida'"

            elif mm % 2 == 0 and mm != 2 and dd > 30:
                aviso = "'Data inválida'"

            elif mm % 2 != 0 and dd >31:
                aviso = "'Data inválida'"

            print(aviso)

            break

        except ValueError:
            print('Entrada inválida!!!')
        
