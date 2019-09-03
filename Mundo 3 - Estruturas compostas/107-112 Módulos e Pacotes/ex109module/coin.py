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
