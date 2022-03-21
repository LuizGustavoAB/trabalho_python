salario = float(input('Qual seu salário? (ex.: 279.99) '))
if salario > 0:
    if salario <= 280.00:
        aumento = 1.2
        print(f'O seu salário com o aumento foi para {salario*aumento} reais!')
    elif salario > 280.00 and salario <= 700.00:
        aumento = 1.15
        print(f'O seu salário com o aumento foi para {salario*aumento} reais!')
    elif salario > 700.00 and salario <= 1500.00:
        aumento = 1.1
        print(f'O seu salário com o aumento foi para {salario * aumento} reais!')
    else:
        aumento = 1.05
        print(f'O seu salário com o aumento foi para {salario * aumento} reais!')
else:
    print('Salário inválido!')
