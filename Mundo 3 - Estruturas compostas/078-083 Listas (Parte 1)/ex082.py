nums = []
pairs = []
odd = []

while True:

    nums.append(int(input('Digite um número: ')))

    option = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if option == 'N':
        break

for num in nums:

    if num % 2 == 0:
        pairs.append(num)
    else:
        odd.append(num)

print(f'A lista completa é {nums}')
print(f'A lista de pares é {pairs}')
print(f'A lista de ímpares é {odd}')
