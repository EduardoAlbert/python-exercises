listaValores = []
pos = 0

while True:

    pos += 1
    valor = int(input(f'Digite o {pos} valor: '))

    if valor not in listaValores:
        listaValores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor já existente! Ele não será adicionado!')

    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if escolha == 'N':
        break

listaValores.sort()
print('-='*30)
print(f'Valores adicionados: {listaValores}')

