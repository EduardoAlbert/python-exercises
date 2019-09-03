name = str(input('\033[34mDigite seu nome completo: '))
div = name.split()
print('\033[31mPrimeiro: {}'.format(div[0]))
print('\033[32mÚltimo: {}'.format(div[len(div)-1]))
