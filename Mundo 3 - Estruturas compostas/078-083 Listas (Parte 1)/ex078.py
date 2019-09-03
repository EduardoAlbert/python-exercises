listNums = []

for pos in range(0, 5):

    listNums.append(int(input(f'Digite um valor para a Posição {pos}: ')))

print(f'Você digitou os valores {listNums}')
print(f'O maior valor digitado foi {max(listNums)} nas posições ', end='')

for posMaior, num in enumerate(listNums):
    if num == max(listNums):
        print(f'{posMaior}...', end=' ')

print(f'\nO menor valor digitado foi {min(listNums)} nas posições', end=' ')

for posMenor, num in enumerate(listNums):
    if num == min(listNums):
        print(f'{posMenor}...', end=' ')
