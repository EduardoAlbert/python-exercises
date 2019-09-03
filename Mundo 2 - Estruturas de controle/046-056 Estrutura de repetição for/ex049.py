num = int(input('Digite um número para ver sua tabuada: '))

print('Tabuada do Número', num)
for x in range(1, 11):
    print(num, 'X', x, '=', num*x)
