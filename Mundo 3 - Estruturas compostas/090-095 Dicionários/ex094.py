data = dict()
peoples = list()
womans = list()
ageAboveAverage = list()
somaIdade = 0

while True:
    data.clear()

    data['nome'] = str(input('Nome: '))
    data['sexo'] = str(input('Sexo [M|F]: ')).strip().upper()[0]

    while data['sexo'] not in 'MF':

        print('ERRO! Por favor, digite apenas M ou F.')
        data['sexo'] = str(input('Sexo [M|F]: ')).strip().upper()[0]

    data['idade'] = int(input('Idade: '))
    somaIdade += data['idade']

    if data['sexo'] == 'F':

        womans.append(data['nome'])

    peoples.append(data.copy())

    option = str(input('Quer continuar? [S|N]')).upper().strip()[0]

    while option not in 'SN':

        print('ERRO ! Responda apenas S ou N.')
        option = str(input('Quer continuar? [S|N]')).upper().strip()[0]

    if option == 'N':
        break

print(f'- O grupo tem {len(peoples)} pessoas.')
print(f'- A média de idade é de {somaIdade / len(peoples):5.2f} anos.')
print(f'- As mulheres cadastradas foram: {womans}')
print('- Lista de pessoas com idade acima da média: ')

for people in peoples:

    if people['idade'] > somaIdade / len(peoples):

        print(f"nome = {people['nome']}; sexo = {people['sexo']}; idade = {people['idade']}")


