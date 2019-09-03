opcao = ''
c = 0
soma = 0
lista = []
media = 0

while opcao in 'S':
    valor = int(input('\033[36mDigite um número: '))
    lista.append(valor)
    c += 1
    soma += valor
    opcao = str(input('\033[30mQuer continuar [S|N]? ')).strip().upper()[0]

media = soma / c
print('\033[31mA média entre todos o valores é {}'.format(media))
print('\033[33mO maior valor é {}'.format(max(lista)))
print('\033[34mO menor valor é {}'.format(min(lista)))
