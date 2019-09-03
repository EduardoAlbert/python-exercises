def readInt(text):
    while True:
        try:
            num = int(input(text))
        except ValueError:
            print('\033[31m ERRO! Digite um número inteiro válido.\033[m')
        else:
            break
    return num


def readFloat(text):
    while True:
        try:
            num = float(input(text))
        except ValueError:
            print('\033[31m ERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            num = 0
            break
        else:
            break
    return num


# Main Program
valueInt = readInt('Digite um número Inteiro: ')
valueFloat = readFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {valueInt} e o real foi {valueFloat}')

