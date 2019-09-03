valor_casa = float(input('Qual é o valor da casa: '))
salario = float(input('Qual é o seu salário? '))
anosFinanciamento = float(input('Em quantos anos quer pagar?'))
meses = anosFinanciamento * 12
prestacao = valor_casa / meses
pcentsal = salario * 30 / 100
if prestacao < pcentsal:
    print('A Prestação Mensal será de R${:.2f}...'.format(prestacao))
    print('EMPRÉSTIMO ACEITO!')
else:
    print('A Prestação Mensal será de R${:.2f}, esse valor excede 30% do seu salário...'.format(prestacao))
    print('EMPRÉSTIMO NEGADO!')

