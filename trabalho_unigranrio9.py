contador = [0] * 9
salarios = []
sal = float(input('Qual seu salário semanal? R$ '))
while sal > 199:
    salarios.append(sal)
    sal = float(input('Qual seu salário semanal? R$ '))
for x in salarios:
    if x >= 1000:
        contador[8] += 1
    else:
        contador[int(x/100) - 2] += 1
print(44 * '-=')
print(contador)