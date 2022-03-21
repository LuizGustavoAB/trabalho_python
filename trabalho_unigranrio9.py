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
print(30 * '-=')
for y,z in enumerate(contador):
    if y == 8:
        print(f'A quantidade de funcionários com salários maio que 1000 é: {z}')
    else:
        print(f'A quantidade de funcionários entre {y + 2}00 - {y + 2}99 é: {z}')
