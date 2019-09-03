def coin(value):
    return f'R${value}'.replace('.', ',')


def increase(x, inc):
    result = x + (x * inc/100)
    return result


def decrease(x, dec):
    result = x - (x * dec/100)
    return result


def double(x):
    result = x * 2
    return result


def half(x):
    result = x / 2
    return result



