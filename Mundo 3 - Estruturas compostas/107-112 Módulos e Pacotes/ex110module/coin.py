def coin(value):
    return f'R${value:>.2f}'.replace('.', ',')


def half(x, formatCoin=False):
    result = x / 2

    return coin(result) if formatCoin else result


def double(x, formatCoin=False):
    result = x * 2

    return coin(result) if formatCoin else result


def increase(x, inc, formatCoin=False):
    result = x + (x * inc/100)

    return coin(result) if formatCoin else result


def decrease(x, dec, formatCoin=False):
    result = x - (x * dec / 100)

    return coin(result) if formatCoin else result


def resume(value, inc, dec):
    print('-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado:  \t{coin(value)}')
    print(f'Dobro do preço:   \t{double(value, True)}')
    print(f'Metade do preço:  \t{half(value, True)}')
    print(f'{inc}% de aumento: \t{increase(value, inc, True)}')
    print(f'{dec}% de aumento: \t{decrease(value, dec, True)}')
