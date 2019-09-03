from random import randint
from time import sleep

print('-'*30)
print('{:^30}'.format('JOGO NA MEGA SENA'))
print('-'*30)

quantPalpites = int(input('Quantos jogos quer que eu sorteie? '))

cont = 0
jogo = list()
todosJogos = list()

for i in range(0, quantPalpites):
    for i2 in range(0, 6):

        sorteado = randint(1, 60)

        if sorteado not in jogo:
            jogo.append(sorteado)
        else:
            while sorteado in jogo:
                sorteado = randint(1, 60)
            jogo.append(sorteado)

    todosJogos.append(jogo[:])
    jogo.clear()

print('-='*3, f'SORTEANDO {quantPalpites} JOGOS', '-='*3)

for jogos in todosJogos:
    cont += 1
    print(f'Jogo {cont}: {jogos}')
    sleep(1)

print('-='*5, '< BOA SORTE! >', '-='*5)
