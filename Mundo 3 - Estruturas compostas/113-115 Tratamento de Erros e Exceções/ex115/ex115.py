from ex115module import select_option

while True:
    print('-' * 60)
    print('MENU PRINCIPAL'.center(60))
    print('-' * 60)
    print('\033[33m1 -\033[m \033[34mVer pessoas cadastradas\n'
          '\033[33m2 -\033[m \033[34mCadastrar nova Pessoa\n'
          '\033[33m3 -\033[m \033[34mSair do Sistema\033[m')
    print('-' * 60)

    try:
        option = int(input('\033[33mSua Opção: \033[m'))
        if option > 3 or option <= 0:
            print('\033[31mERRO! Digite um opção válida!\033[m')
            continue

    except ValueError:
        print('\033[31mERRO! Digite um opção válida!\033[m')

    else:
        if option == 1 or option == 2:
            select_option(option)
        elif option == 3:
            break

print('-' * 60)
print('Saindo do sistema... Até logo!'.center(60))
print('-' * 60)
