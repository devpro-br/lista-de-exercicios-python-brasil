"""
Exercício 07 da seção de funções da Python Brasil:
https://wiki.python.org.br/ExerciciosFuncoes

Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

    >>> valorPagamento(5250,20)
    5407.52
    >>> valorPagamento(7450,35)
    7673.535
    >>> valorPagamento(1289,20)
    1327.69
    >>> valorPagamento(0,0)
    0.0

"""

def valorPagamento(p,d):
    """Escreva aqui em baixo a sua solução"""

    return p*1.03 + 0.001*d

    while True:
        p = float(input('Valor da prestação: '))
        if p == 0:
            print(f'Total: {t}. Quantidade: {c} ')
            break
        d = int(input('Dia em atraso: '))
        print(f'Valor a ser pago: {valorPagamento(p, d) :.2f}')
        print('-+-'*10)
        c += 1
        t += valorPagamento(p, d)