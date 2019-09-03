def coin(value):
    return f'R${value:>.2f}'.replace('.', ',')


def double(x, formatCoin=False):
    result = x * 2

    if formatCoin:
        return coin(result)
    else:
        return result


def half(x, formatCoin=False):
    result = x / 2

    if formatCoin:
        return coin(result)
    else:
        return result


def increase(x, inc, formatCoin=False):
    i = x / 100 * inc
    result = x + i

    if formatCoin:
        return coin(result)
    else:
        return result


def decrease(x, dec, formatCoin=False):
    d = x / 100 * dec
    result = x - d

    if formatCoin:
        return coin(result)
    else:
        return result


def resume(value, inc, dec):
    print('-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado:  \t{coin(value)}')
    print(f'Dobro do preço:   \t{double(value, True)}')
    print(f'Metade do preço:  \t{half(value, True)}')
    print(f'{inc}% de aumento: \t{increase(value, inc, True)}')
    print(f'{dec}% de aumento: \t{decrease(value, dec, True)}')
