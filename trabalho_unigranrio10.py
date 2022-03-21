def valorpagamento1(atraso, prestacao):
    juros = 1.001 ** atraso
    multa = 0
    if atraso > 0:
        multa = 0.03
    total_prestacao = prestacao * juros + prestacao * multa
    print(f'O total a ser pago é de: R$ {total_prestacao}')
    return total_prestacao

pagamentos1 = []
atraso1 = int(input('De quantos dias é seu atraso? '))
prestacao1= float(input('Quanto é a sua prestação? R$ '))
while prestacao1 != 0:
    f1 = valorpagamento1(atraso1, prestacao1)
    pagamentos1.append(f1)
    atraso1 = int(input('De quantos dias é seu atraso? '))
    prestacao1 = float(input('Quanto é a sua prestação? R$ '))
print('-=' * 50)
print(f'Os pagamentos realizados no dia foram: {pagamentos1}')
print('-=' * 50)
print(len(f'O total de pagamentos feitos no dia é de: {pagamentos1}'))
print('-=' * 50)
print(f'A soma de todas as prestações pagas no dia é de: {sum(pagamentos1)}')