nota1 = int(input('Nota1: '))
nota2 = int(input('Nota2: '))
media = (nota1 + nota2)/2
if (nota1 >= 0 and nota1 <=10) and (nota2 >= 0 and nota2 <=10):
    if nota1 == 10 and nota2 == 10:
        print('Aprovado com Dinstinção!!!')
    elif media >= 7:
        print('Aprovado!')
    elif media < 7:
        print('Reprovado!')
else:
    print('Notas não existem!')