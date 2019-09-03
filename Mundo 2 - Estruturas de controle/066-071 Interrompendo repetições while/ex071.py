valor = int(input('Que valor você quer sacar? '))

nota = 100
totalNotas = 0

while True:
    if valor >= nota:
        valor -= nota
        totalNotas += 1
    else:
        if totalNotas > 0:
            print(f'Total de {totalNotas} cédulas de R${nota}')

        if nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1

        totalNotas = 0

        if valor == 0:
            break
