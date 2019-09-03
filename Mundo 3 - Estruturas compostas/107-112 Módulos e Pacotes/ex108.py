from ex108module import coin

price = float(input('Digite o preço: R$'))
print(f'A metade de {coin.coin(price)} é {coin.coin(coin.half(price))}')
print(f'O dobro de {coin.coin(price)} é {coin.coin(coin.double(price))}')
print(f'Aumentando 10%, temos {coin.coin(coin.increase(price, 10))}')
print(f'Reduzindo 13%, temos {coin.coin(coin.decrease(price, 13))}')
