sexo = str(input('Sexo {M|F}: ')).strip().upper()[0]

while sexo not in 'MF':
    print('Sexo Inválido! Tente Novamente...')
    sexo = str(input('Sexo{M|F}: ')).strip().upper()[0]

if sexo in 'F':
    print('Seu sexo é Feminino')
elif sexo in 'M':
    print('Seu sexo é Masculino')
