altura = float(input('Qual sua altura em metros? (ex.: 1.78) '))
sexo = input('Qual seu sexo? (M = mulher; H = homem) ')
peso = 0
if sexo == 'm' or sexo == 'M':
    peso = (62.1 * altura) - 44.7
if sexo == 'h' or sexo == 'H':
    peso = (72.7 * altura) - 58
print(f'{int(peso)} kg é o seu peso ideal')