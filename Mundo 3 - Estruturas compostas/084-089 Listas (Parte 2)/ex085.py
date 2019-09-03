num = [[], []]

for cont in range(1, 9):

    value = int(input(f'Digite o {cont}º Valor: '))

    if value % 2 == 0:
        num[0].append(value)

    else:
        num[1].append(value)

print(f'Os valores Pares digitados foram: {sorted(num[0])}')
print(f'Os valores Ímpares digitados foram: {sorted(num[1])}')
