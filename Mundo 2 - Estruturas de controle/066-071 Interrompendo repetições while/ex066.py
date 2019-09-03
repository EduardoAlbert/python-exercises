valor = cont = soma = 0

while True:
    valor = int(input('Digite um valor (999 para parar): '))

    if valor == 999:
        break

    soma += valor
    cont += 1

print(f'A soma dos {cont} valores foi {soma} ')
