def factorial(number, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param number: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n.
    """
    fact = 1
    for cont in range(number, 0, -1):
        fact *= cont
        if show:
            print(f'{cont} x' if cont != 1 else f'{cont} =', end=' ')
    return fact


# Main Program
print('-'*30)
print(factorial(5, show=True))
help(factorial)
