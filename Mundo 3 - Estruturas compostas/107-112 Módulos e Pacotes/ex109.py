from ex109module import coin

price = float(input('Digite o preço: R$'))
print(f'A metade de {coin.coin(price)} é {coin.half(price, True)}')
print(f'O dobro de {coin.coin(price)} é {coin.double(price, True)}')
print(f'Aumentando 10%, temos {coin.increase(price, 10, True)}')
print(f'Reduzindo 13%, temos {coin.decrease(price, 13, True)}')
