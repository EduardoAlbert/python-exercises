from ex107module import coin

price = float(input('Digite o preço: R$ '))
print(f'A metade de R${price} é R${coin.half(price)}')
print(f'O dobro de {price} é {coin.double(price)}')
print(f'Aumentando 10%, temos {coin.increase(price, 10)}')
print(f'Reduzindo 13%, temos {coin.decrease(price, 13)}')
