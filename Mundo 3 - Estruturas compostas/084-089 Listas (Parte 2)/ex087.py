matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

somaPares = somaTerceiraColuna = 0
segundaLinha = list()

for linha in range(0, 3):
    for coluna in range(0, 3):

        matriz[linha][coluna] = int(input(f'Digite um valor para {[linha, coluna]}: '))

        if matriz[linha][coluna] % 2 == 0:          # A soma de todos os valores pares
            somaPares += matriz[linha][coluna]

        if coluna == 2:            # A soma de todos os valores da terceira coluna
            somaTerceiraColuna += matriz[linha][coluna]

        if linha == 1:             # O maior valor da segunda linha
            segundaLinha.append(matriz[linha][coluna])

print('-='*15, end='')
for linhas in matriz:
    print()
    for colunas in linhas:
        print(f'[{colunas:^5}]', end='')
print('\n', '-='*15)

print(f'\nA soma de todos os valores pares é {somaPares}')
print(f'A soma de todos os valores da terceira coluna é {somaTerceiraColuna}')
print(f'O maior valor da segunda linha é {max(segundaLinha)}')
