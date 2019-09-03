from random import randint

numTuple = tuple(randint(1, 10) for times in range(0, 6))

print('Os valores sorteados foram:', end=' ')
for nums in numTuple:
    print(nums, end=' ')

print(f'\nO maior valor sorteado foi {max(numTuple)}')
print(f'O menor valor sorteado foi {min(numTuple)}')
