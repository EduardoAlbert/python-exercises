pos = mais18 = totalHomens = totalMulheresMenosDe20 = 0

while True:
    pos += 1

    print('-' * 30)
    print(f'     CADASTRE A {pos}ª PESSOA')
    print('-' * 30)

    idade = int(input('Idade: '))

    if idade > 18:
        mais18 += 1

    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    if sexo == 'M':
        totalHomens += 1

    elif sexo == 'F' and idade < 20:
        totalMulheresMenosDe20 += 1

    opcao = ' '

    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if opcao == 'N':
        break

print('=' * 6, 'FIM DO PROGRAMA', '=' * 6)
print(f'''Total de pessoas com mais de 18 anos: {mais18}
Ao todo temos {totalHomens} homens cadastrados
E tempos {totalMulheresMenosDe20} mulheres com menos de 20 anos''')
