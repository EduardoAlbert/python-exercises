from random import randint


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')

    for i in range(0, 5):
        sorteado = randint(0, 10)
        lista.append(sorteado)

        print(sorteado, end=' ')
    print('PRONTO!')


def somaPar(lista):
    sp = 0

    for valor in lista:
        if valor % 2 == 0:
            sp += valor

    print(f'Somando os valores pares de {lista}, temos {sp}')


# Main Program
numeros = list()

sorteia(numeros)
somaPar(numeros)
