listOfPrices = ('Lápis', 1.75,
                'Borracha', 2.00,
                'Caderno', 15.90,
                'Estojo', 25.00,
                'Transferidor', 4.20,
                'Compasso', 9.99,
                'Mochila', 120.32,
                'Canetas', 22.30,
                'Livro', 34.90)

print('-'*40)
print('          LISTAGEM DE PREÇOS')
print('-'*40)

for itens in range(0, len(listOfPrices), 2):
    print(f'{listOfPrices[itens]:.<30}R$ '
          f'{listOfPrices[(itens+1)]:>6.2f}', end='\n')

print('-'*40)
