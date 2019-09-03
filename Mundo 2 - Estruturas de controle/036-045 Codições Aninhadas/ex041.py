from datetime import date

ano = int(input('Ano de nascimento do atleta: '))
idade = date.today().year - ano

if idade <= 9:
    print('A categoria do atleta é : Mirim.')
elif idade <= 14:
    print('A categoria do Atleta é: Infantil.')
elif idade <= 19:
    print('A categoria do Atleta é: Junior.')
elif idade <= 25:
    print('A categoria do Atleta é: Sênior.')
elif idade > 25:
    print('A categoria do Atleta é : Master.')
