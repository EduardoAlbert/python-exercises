def register(name, age):
    arquive = open('database.txt', 'r')
    newRegistry = arquive.readlines()
    newRegistry.append(f'{name:<48}{age} anos\n')

    arquive = open('database.txt', 'w')
    arquive.writelines(newRegistry)
    arquive.close()


def select_option(option):
    if option == 1:
        print('-' * 60)
        print('PESSOAS CADASTRADAS'.center(60))
        print('-' * 60)
        database = open('database.txt', 'r')
        print(database.read())
        database.close()

    elif option == 2:
        print('-' * 60)
        print('NOVO CADASTRO'.center(60))
        print('-' * 60)
        name = str(input('Nome: '))
        while True:
            try:
                age = int(input('Idade: '))
            except ValueError:
                print('\033[31mERRO: por favor, digite um número inteiro válido!\033[m')
            else:
                register(name, age)
                print(f'Novo registro de {name} adicionado.')
                break
