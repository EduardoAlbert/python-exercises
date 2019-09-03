num = int(input('Digite um número: '))
antecessores = num
fatorial = 1

print('{}! = '.format(num), end='')
while antecessores > 0:
    print('{}'.format(antecessores), end='')
    print(' x ' if antecessores > 1 else ' =', end='')
    fatorial *= antecessores
    antecessores -= 1

print(' {}'.format(fatorial))
