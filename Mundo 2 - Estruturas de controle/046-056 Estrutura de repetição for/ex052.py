num = int(input('Digite um número: '))

divisores = 0
for x in range(1, num+1):
    if num % x == 0:
        print('\033[33m{}'.format(x), end=' ')
        divisores += 1
    else:
        print('\033[31m{}\033[m'.format(x), end=' ')

print('\nO número {} foi divisível {} vezes'.format(num, divisores))
if divisores == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
