opcao = 0
v1 = int(input('Valor 1: '))
v2 = int(input('Valor 2: '))

while opcao != 5:

    # Menu
    print('-='*15)
    print('       MENU')
    print('''    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA''')
    print('-=' * 15)
    opcao = int(input('Escolha uma das opções: '))

    # Erro
    if opcao > 5:
        while opcao > 5:
            opcao = int(input('Opção Inválida! Tente Novamento: '))

    # [1]Somar
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(v1, v2, v1+v2))

    # [2]Multiplicar
    elif opcao == 2:
        print('O produto de {} e {} é {}'.format(v1, v2, v1*v2))

    # [3]Maior
    elif opcao == 3:
        if v1 > v2:
            print('{} é maior que {}'.format(v1, v2))
        else:
            print('{} é maior que {}'.format(v2, v1))

    # [4]Novos números
    elif opcao == 4:
        v1 = int(input('Valor 1: '))
        v2 = int(input('Valor 2: '))

print('Até mais, Volte Sempre!')




