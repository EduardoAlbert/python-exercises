from random import randint


print('{}-=-{}'.format('\033[33m', '\033[m') * 18)
print('\033[34mVou pensar em um número de 0 a 10, tente adivinhar...\033[m ')
print('\033[33m-=-\033[m' * 18)
num = randint(0, 10)

resp = int(input('Em que número eu pensei? '))
tentativas = 1
while resp != num:
    if resp < num:
        resp = int(input('Mais... Tente novamente: '))
    else:
        resp = int(input('Menos... Tente novamente: '))
    tentativas += 1
print('\033[32mVocê venceu! Eu pensei no número {}!\033[m'.format(resp))
print('Você precisou de {} palpite(s) para acertar.'.format(tentativas))

