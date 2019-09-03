n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
if n1 > n2:
    print('\033[33mO primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')