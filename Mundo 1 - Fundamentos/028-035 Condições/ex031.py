dist = float(input('\033[7;37mQual é a distância da sua viajem em \033[4;31mKm\033[m?\n'))
if dist > 200:
    print('\033[31mSua viagem é mais longa e vai custar R${}'.format(dist*0.45))
else:
    print('\033[35mO preço da passagem é: R${}'.format(dist*0.50))
