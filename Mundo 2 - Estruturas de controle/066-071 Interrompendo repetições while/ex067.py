while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num} X {cont} = {num*cont}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

