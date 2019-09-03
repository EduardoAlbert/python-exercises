def readMoney(text):
    value2 = []
    valid = False
    while not valid:
        value = str(input(text)).replace(',', '.').strip()
        if value.isalpha() or value == '':
            print(f'\033[31mERRO: "{value}" é um preço inválido!\033[m')
        else:
            valid = True
            return float(value)
