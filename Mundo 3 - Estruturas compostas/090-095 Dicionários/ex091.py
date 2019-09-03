from random import randint
from operator import itemgetter
from time import sleep

pos = 0
resultados = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6),
              'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}

for jogador, valor in resultados.items():

    print(f'O {jogador} tirou {valor}')

    sleep(1)

for jogador, valor in sorted(resultados.items(), key=itemgetter(1), reverse=True):

    pos += 1
    
    print(f'{pos}º lugar: {jogador} com {valor}')

    sleep(1)
