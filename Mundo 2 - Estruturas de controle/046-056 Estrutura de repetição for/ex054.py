from datetime import date

anoAtual = date.today().year
somaMenorIdade = 0
somaMaiorIdade = 0

for pessoa in range(1, 8):
    anoDeNascimento = int(input('Ano de nascimento da {}ª pessoa: '.format(pessoa)))
    idade = anoAtual - anoDeNascimento

    if idade < 21:
        somaMenorIdade += 1
    else:
        somaMaiorIdade += 1

print(somaMenorIdade, 'pessoas ainda não atingiram a Maior Idade')
print(somaMaiorIdade, 'pessoas já são Maiores de Idade')
