from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1

    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
            sleep(0.5)
        print('FIM!')
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ')
            sleep(0.5)
        print('FIM!')


# Main Program
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)

pers_inicio = int(input('Agora é sua vez de personalizar a contagem!\nInício:'))
pers_fim = int(input('Fim: '))
pers_passo = int(input('Passo: '))

contador(pers_inicio, pers_fim, pers_passo)
