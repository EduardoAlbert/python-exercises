numTuple = (int(input('Digite um número: ')),
            int(input('Digite outro número: ')),
            int(input('Digite mais um número: ')),
            int(input('Digite o último número: ')))

print(f'Você digitou os valores {numTuple}')

print(f'O valor 9 apareceu {numTuple.count(9)} vezes')

if 3 in numTuple:
    print(f'O valor 3 apareceu na {numTuple.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram', end=' ')

for nums in numTuple:
    if nums % 2 == 0:
        print(nums, end=' ')

