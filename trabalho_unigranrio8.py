notas = []
nota = float(input('Coloque sua nota: '))
while nota != -1:
    notas.append(nota)
    nota = float(input('Coloque sua nota: '))
print(30 * '-=')
print(f'{len(notas)} notas cadastradas')
print(30 * '-=')
frase_notas = 'Essa é a sequência de notas: '
for x in notas:
    frase_notas = frase_notas + f'{x},'
print(frase_notas)
print(30 * '-=')
for x in reversed(notas):
    print(x)
print(30 * '-=')
soma_notas = sum(notas)
print(f'O somatório das notas é: {soma_notas}')
print(30 * '-=')
media_notas = (sum(notas))/len(notas)
print(f'A média das notas obtidas é de: {media_notas}')
print(30 * '-=')
maiores = []
for y in notas:
    if y > media_notas:
        maiores.append(y)
print(f'Os valores acima da média são: {maiores}')
print(30 * '-=')
menores = []
for z in notas:
    if z < media_notas:
        menores.append(z)
print(f'Os valores menores que a média são: {menores}')
print(30 * '-=')
print('Obrigado por utilizar de nosso programa!\nCaso precise de suporte técnico entrar em contato:\nTelefone: (21) 99756-4060\nE-mail: suporte.trabalho@unigranrio.com')