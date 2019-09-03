import datetime
ano = int(input('Em que ano você nasceu? '))
genero = input('Qual é o seu gênero [M/F] ? ')
anoAtual = datetime.date.today().year
idade = datetime.date.today().year - ano
falta = 18 - idade
print('Ano Atual: ', anoAtual)

if genero == 'F':
    print('Não existe alistamento obrigatório para Mulher...')

if idade < 18 and genero == 'M':  # Se a idade for inferior a 18
    print('Você tem {} anos, ainda faltam {} ano(s) para se alistar ao serviço militar.'.format(idade, falta))
    print('Seu ano de alistamento é', anoAtual + falta)

elif idade == 18 and genero == 'M':   # Se a idade for igual a 18
    print('Você já tem, ou está prestes a completar 18 anos, está na hora de se alistar ao serviço militar.')

elif idade > 18 and genero == 'M':   # Se já tiver mais de 18
    print('Você está com {} anos, se passaram {} ano(s) do prazo para se alistar ao serviço militar. '.format(idade, falta * -1))
    print('Seu ano de alistamento foi', anoAtual - falta * -1)
