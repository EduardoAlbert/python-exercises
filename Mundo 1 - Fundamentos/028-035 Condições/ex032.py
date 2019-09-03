from datetime import date
ano = int(input('\033[36mQual ano quer analisar? \033[31mDigite 0 para analisar o ano atual:\n'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[32mO ano de {} é BISSEXTO.'.format(ano))
else:
    print('O ano de {} não é BISSEXTO.'.format(ano))

