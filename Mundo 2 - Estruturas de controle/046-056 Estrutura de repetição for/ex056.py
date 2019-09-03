somaIdade = 0
mediaIdade = 0
homemMaisVelho = str
idadeMaisVelho = 0
mulheresMenosDe20 = 0

for i in range(1, 5):
    print("-----{}ª PESSOA -----".format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M|F]: ')).strip()

    # Média de Idade
    somaIdade += idade
    mediaIdade = somaIdade / i
    # Homem mais velho
    if sexo in 'Mf' and idade > idadeMaisVelho:
        idadeMaisVelho = idade
        homemMaisVelho = nome
    # Mulheres com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        mulheresMenosDe20 += 1

print('A média de Idade do Grupo é de', mediaIdade, 'anos.')
print('O homem mais velho tem {} anos e se chama {}'.format(idadeMaisVelho, homemMaisVelho))
print(mulheresMenosDe20, 'mulheres tem menos de 20 anos.')
