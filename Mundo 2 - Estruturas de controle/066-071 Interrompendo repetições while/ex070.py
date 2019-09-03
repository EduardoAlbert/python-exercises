print('-' * 20)
print('Mercadão da Galera')
print('-' * 20)

cont = maisBarato = somaPreco = maisDe1000 = 0
nomeProdutoMaisBarato = ''


while True:
    cont += 1
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))

    somaPreco += preco

    if preco > 1000:
        maisDe1000 += 1

    if cont == 1 or preco < maisBarato:
        maisBarato = preco
        nomeProdutoMaisBarato = nome

    opcao1 = ' '

    while opcao1 not in 'SN':
        opcao1 = str(input('Quer continuar? ')).upper().strip()

    if opcao1 == 'N':
        break

print(f'O total da compra foi {somaPreco:.2f}')
print(f'Temos {maisDe1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeProdutoMaisBarato} que custa {maisBarato}')
