frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
fraseNormal = ''.join(palavras)
fraseInversa = ''
for letras in range(len(fraseNormal) - 1, -1, -1):
    fraseInversa += fraseNormal[letras]

print('O inverso de {} é {}'.format(fraseNormal, fraseInversa))

if fraseNormal == fraseInversa:
    print('Essa frase é um Palíndromo!')
else:
    print('Essa frase não é um Palíndromo...')
