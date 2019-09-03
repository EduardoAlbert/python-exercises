nums = []

while True:

    nums.append(int(input('Digite um valor: ')))

    option = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if option == 'N':
        break

print(f'Você digitou {len(nums)} elementos.')
nums.sort(reverse=True)
print(f'Os valores em ordem decrescente são {nums}')

if 5 in nums:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
