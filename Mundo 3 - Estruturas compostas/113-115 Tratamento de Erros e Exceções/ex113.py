def readInt(text):
    while True:
        try:
            num = int(input(text))
        except ValueError:
            print('\033[31m ERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31m Usuário preferiu não digitar esse número.\033m')
            return 0
        else:
            return num


def readFloat(text):
    while True:
        try:
            num = float(input(text))
        except ValueError:
            print('\033[31m ERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31m Usuário preferiu não digitar esse número.\033m')
            return 0
        else:
            return num


# Main Program
valueInt = readInt('Digite um número Inteiro: ')
valueFloat = readFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {valueInt} e o real foi {valueFloat}')

