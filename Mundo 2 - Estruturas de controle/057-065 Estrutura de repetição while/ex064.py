c = soma = 0
pos = 1
valor = int(input('Digite o {}º Valor [999 para parar]: '.format(pos)))
while valor != 999:
    pos += 1
    c += 1
    soma += valor
    valor = int(input('Digite o {}º Valor [999 para parar]: '.format(pos)))

print('{} números foram digitados e a soma entre eles é {}'.format(c, soma))
