from random import randint
from time import sleep

num = randint(0, 5)
print('{}-=-{}'.format('\033[33m', '\033[m') * 18)
print('\033[34mVou pensar em um número de 0 a 5, tente adivinhar...\033[m ')
print('\033[33m-=-\033[m' * 18)
resp = int(input('Em que número eu pensei? '))
print('\33[35mPROCESSANDO...\033[m')
sleep(2)
if resp == num:
    print('\033[32mVocê venceu! Eu pensei no número {}!\033[m'.format(resp))
else:
    print('\033[31mVocê perdeu! Eu pensei no número {} e não no {}!\033[m'.format(num, resp))

