from time import sleep


def printCustom(text, backgroundColor='default'):
    colorsBackground = {'red': '\033[30;41m',
                        'green': '\033[30;42m',
                        'yellow': '\033[30;43m',
                        'blue': '\033[30;44m',
                        'purple': '\033[30;45m',
                        'default': '\033[m'}

    size = len(text) + 4

    print(colorsBackground[backgroundColor], end='')
    print('~' * size)
    print(f'  {text}')
    print('~' * size)
    print(colorsBackground['default'], end='')

    sleep(1)


# Main Program
while True:
    printCustom('SISTEMA DE AJUDA PyHELP', backgroundColor='green')
    command = str(input('\033[mFunção ou Biblioteca > '))

    if command == 'fim':
        break

    printCustom(f"Acessando o manual do comando '{command}'", backgroundColor='blue')

    print('\033[37;40m', end='')

    help(command)

printCustom('ATÉ LOGO!', backgroundColor='red')