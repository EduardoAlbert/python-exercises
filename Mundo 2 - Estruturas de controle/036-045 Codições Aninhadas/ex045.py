from random import choice
from time import sleep
print('Jokenpô')

jogadas = ['Pedra', 'Papel', 'Tesoura']

print('[ 0 ]PEDRA\n[ 1 ]PAPEL\n[ 2 ]TESOURA')
jogadaPlayer = int(input('Qual é a sua jogada? '))  # Jogada do Player
jogadaPlayer = jogadas[jogadaPlayer]
jogadaPc = choice(jogadas)  # Jogada do Pc

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')

print('-='*11)
print('Você jogou:', jogadaPlayer)
print('O PC jogou:', jogadaPc)
print('-='*11)
# Vítorias do Player
if(jogadaPlayer == 'Pedra') and (jogadaPc == 'Tesoura'):
    status = 'Você Venceu!'

elif(jogadaPlayer == 'Papel') and (jogadaPc == 'Pedra'):
    status = 'Você Venceu!'

elif(jogadaPlayer == 'Tesoura') and (jogadaPc == 'Papel'):
    status = 'Você Venceu!'
# Empate
elif jogadaPlayer == jogadaPc:
    status = 'Empate...'
# Derrota
else:
    status = 'Você Perdeu!'
print(status)
