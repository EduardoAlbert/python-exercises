valor = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')

opcao = int(input('Sua opção:'))

if opcao == 1:
    print('{} convertido para BINÁRIO  HEXADECIMAL é igual a {}'.format(valor, bin(valor[2:])))

elif opcao == 2:
    print('{} convertido para OCTAL é igual {}'.format(valor, oct(valor[2:])))

elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(valor, hex(valor[2:])))

else:
    print('Opção Inválida')
