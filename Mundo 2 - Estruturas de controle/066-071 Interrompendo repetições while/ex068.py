from random import randint

print('=-' * 32)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 32)
c = 0
while True:
    playerGanha = False
    parOuImpar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    jogadaPlayer = int(input('Diga um valor: '))
    jogadaPc = randint(0, 10)
    soma = jogadaPlayer + jogadaPc
    if soma % 2 == 0:
        result = 'PAR'
    else:
        result = 'ÍMPAR'
    print(f'Você jogou {jogadaPlayer} e o computador {jogadaPc}. Total de {soma} DEU {result}')

    # Vitórias do Player
    if result == 'PAR' and parOuImpar == 'P' or \
            result == 'ÍMPAR' and parOuImpar == 'I':
        playerGanha = True
        c += 1
    if not playerGanha:
        break
print(f'GAME OVER! Você venceu {c} vezes.')
