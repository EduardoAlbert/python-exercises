def readInt(text):
    num = input(text)

    while not num.isnumeric():
        print('\033[31m ERRO! Digite um número inteiro válido.\033[m')
        num = input(text)

    number = int(num)
    return number


# Main Program
value = readInt('Digite um número: ')
print(f'Você acabou de digitar o número {value}')
